# -*- coding: utf-8 -*-
from datetime import timedelta, datetime
import scrapy
from agriculture_demo.items import MofcomItem
from province_city import get_province
from agriculture_demo.dbhelper import DBHelper

global page, yesterday, starttime
yesterday = (datetime.today() + timedelta(days=-1))
page = 1
dbhelper = DBHelper()
date = dbhelper.get_latest_date("strawberry_price")
if date == None:
    starttime = (datetime.today() + timedelta(days=-90))
else:
    starttime = date
print(starttime)
headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate, sdch, br',
    'Accept-Language': 'zh-CN,zh;q=0.8',
    'Connection': 'keep-alive',
    'Host': 'nc.mofcom.gov.cn',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.157 Safari/537.36"}

'''
草莓价格网站最多一次爬取三个月数据
1.数据库中无草莓价格数据，爬取三个月数据
2.数据库中有草莓价格数据，爬取历史数据最新时间--当前昨日时间之间的数据
'''


class SpiderMofcomSpider(scrapy.Spider):
    name = 'spider_mofcom'
    allowed_domains = ['nc.mofcom.gov.cn']
    y = yesterday.strftime('%Y-%m-%d')
    start_urls = ['http://nc.mofcom.gov.cn/channel/jghq2017/price_list.shtml?par_craft_index=13076&craft_index=13167'
                  '&par_p_index=&p_index=&startTime=' + y + '&endTime=' + y + '&page=' + str(page)]

    def parse(self, response):
        print("进入第一次解析")
        global page, yesterday, starttime
        page = 1
        starttime = starttime.strftime('%Y-%m-%d')
        url = 'http://nc.mofcom.gov.cn/channel/jghq2017/price_list.shtml?par_craft_index=13076&craft_index=13167' \
              '&par_p_index=&p_index=&startTime=' + starttime + '&page=' + str(
            page)
        yield scrapy.Request(url=url, callback=self.second_parse, meta={"start": starttime})

    def second_parse(self, response):
        print("进入第二次解析")
        global page
        start = response.meta["start"]
        result = response.xpath("//div//table//tr[position()>1]")
        flag = True
        for item in result:
            mofcom = MofcomItem()
            date = item.xpath(".//td[1]/text()").extract_first().strip()
            if date == "" or date == None:
                flag = False
                yield scrapy.Request('http://nc.mofcom.gov.cn/channel/jghq2017/price_list.shtml?par_craft_index=13076'
                                     '&craft_index=13167&par_p_index=&p_index=&startTime=' + start
                                     + '&page=' + str(page), callback=self.second_parse,
                                     dont_filter=True, headers=headers, meta={"start": start})
                break
            else:
                mofcom['date'] = datetime.strptime(date, "%Y-%m-%d")
                mofcom['name'] = item.xpath(".//td[2]//span/text()").extract_first()
                price = item.xpath(".//td[3]/span/text()").extract_first()
                mofcom['price'] = float(price)
                mofcom['measurement_unit'] = item.xpath(".//td[3]/text()").extract_first()
                mofcom['market'] = item.xpath(".//td[4]/a/text()").extract_first()
                mofcom['province'] = get_province(mofcom['market'])
                yield mofcom
        if flag:
            script = response.xpath("//section//script[last()]/text()").extract_first().split(";")
            sum = script[0].split()[-1].strip()
            if page < int(sum):
                print("执行下一页")
                page += 1
                yield scrapy.Request('http://nc.mofcom.gov.cn/channel/jghq2017/price_list.shtml?par_craft_index=13076'
                                     '&craft_index=13167&par_p_index=&p_index=&startTime=' + start
                                     + '&page=' + str(page), callback=self.second_parse,
                                     dont_filter=True, headers=headers, meta={"start": start})
