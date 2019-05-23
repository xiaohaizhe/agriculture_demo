# -*- coding: utf-8 -*-
from datetime import datetime, timedelta
import scrapy
from agriculture_demo.items import CfvinItem
from agriculture_demo.dbhelper import DBHelper

get_today = datetime.now()
dbhelper = DBHelper()
date = dbhelper.get_latest_date("strawberry_market_news")
if date == None:
    starttime = (datetime.today() + timedelta(days=-30))
else:
    starttime = date
print(starttime)

'''
草莓行情新闻数据:
1.数据库中没有数据，爬取近30天内的数据
2.数据库中有数据，爬取数据库中最新数据到当前时间的数据
'''


class SpiderCfvinSpider(scrapy.Spider):
    name = 'spider_cfvin'
    allowed_domains = ['cfvin.com']
    start_urls = ['http://www.cfvin.com/caomei/']

    def parse(self, response):
        results = response.xpath("//ul[@id='list']//li")
        for result in results:
            link = result.xpath("./a/@href").extract_first()
            yield scrapy.Request(link, callback=self.parse_second)

    def parse_second(self, response):
        c = (get_today - starttime).days
        result = response.xpath("//body")
        article_title = result.xpath(".//div[@class='fl article-time']")
        date = article_title.xpath(".//span[1]/text()").extract_first()
        date = datetime.strptime(date, "%Y-%m-%d %H:%M:%S")
        if (datetime.now() - date).days <= c:
            cfvinItem = CfvinItem()
            cfvinItem['date'] = date
            cfvinItem['title'] = result.xpath(".//h1/text()").extract_first()
            cfvinItem['source'] = article_title.xpath(".//span[2]/text()").extract_first().split('：')[1]
            cfvinItem['author'] = article_title.xpath(".//span[3]/text()").extract_first().split('：')[1]
            cfvinItem['content'] = result.xpath(".//div[@class='article-conte-infor']/p/text()").extract()
            yield cfvinItem
        else:
            pass
