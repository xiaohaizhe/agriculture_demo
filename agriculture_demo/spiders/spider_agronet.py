# -*- coding: utf-8 -*-
import scrapy
import datetime
from datetime import timedelta
from agriculture_demo.items import AppleAgronetItem
from province_city import get_province

get_today = datetime.datetime.now()
from agriculture_demo.dbhelper import DBHelper

dbhelper = DBHelper()
date = dbhelper.get_latest_date("apple_price")
if date == None:
    starttime = (datetime.today() + timedelta(days=-365))
else:
    starttime = date
'''
苹果价格数据爬取：
1.数据库中为空时，爬取过去据今一年的数据
2.数据库中有数据，爬取数据库中最新日期到当前日期的数据
'''


class SpiderAgronetSpider(scrapy.Spider):
    name = 'spider_agronet'
    allowed_domains = ['agronet.com.cn']
    start_urls = ['http://www.agronet.com.cn/Price/List?page=1&siteID=7']

    def parse(self, response):
        c = (get_today - starttime).days
        items = response.xpath("//ul[@class='price_table']//li[position()>1]")
        date = None
        for item in items:
            date = item.xpath(".//span[1]/text()").extract_first()[1:-1]
            date = datetime.datetime.strptime(date, "%Y-%m-%d")
            variety = item.xpath(".//span[2]/text()").extract_first()[:-2]
            # print("相差天数："+str((get_today-date).days))
            if "苹果" in variety and (get_today - date).days <= c:
                fruit_agronet = AppleAgronetItem()
                fruit_agronet['date'] = date
                fruit_agronet['variety'] = variety
                fruit_agronet['terminal_market'] = item.xpath(".//span[3]/a/text()").extract_first().strip()
                fruit_agronet['top_price'] = float(item.xpath(".//span[5]/text()").extract_first().strip()[1:])
                fruit_agronet['bottom_price'] = float(item.xpath(".//span[4]/text()").extract_first().strip()[1:])
                fruit_agronet['average_price'] = float(item.xpath(".//span[6]/text()").extract_first().strip()[1:])
                fruit_agronet['measurement_unit'] = item.xpath(".//span[7]/text()").extract_first()
                fruit_agronet['province'] = get_province(fruit_agronet['terminal_market'])
                yield fruit_agronet
            else:
                continue
        next_link = response.xpath("//div[@class='Pager']//a[last()]/@href").extract_first()
        if (get_today - date).days <= c and next_link:
            # if next_link:
            yield scrapy.Request("http://www.agronet.com.cn" + next_link, callback=self.parse)
