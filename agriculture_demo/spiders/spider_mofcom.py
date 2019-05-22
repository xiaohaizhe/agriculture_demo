# -*- coding: utf-8 -*-
from datetime import date, timedelta, datetime

import scrapy

from agriculture_demo.items import MofcomItem
from province_city import get_province

yesterday = (date.today() + timedelta(days=-1)).strftime('%Y-%m-%d')
global page
page = 1
starttime = yesterday


# starttime = "2019-04-28"
# yesterday = "2019-05-06"


class SpiderMofcomSpider(scrapy.Spider):
    name = 'spider_mofcom'
    allowed_domains = ['nc.mofcom.gov.cn']
    start_urls = ['http://nc.mofcom.gov.cn/channel/jghq2017/price_list.shtml?par_craft_index=13076&craft_index=13167'
                  '&par_p_index=&p_index=&startTime=' + starttime + '&endTime=' + yesterday + '&page=' + str(page)]

    def parse(self, response):
        global page
        result = response.xpath("//div//table//tr[position()>1]")
        flag = True
        for item in result:
            mofcom = MofcomItem()
            date = item.xpath(".//td[1]/text()").extract_first().strip()
            if date == "":
                flag = False
                yield scrapy.Request('http://nc.mofcom.gov.cn/channel/jghq2017/price_list.shtml?par_craft_index=13076'
                                     '&craft_index=13167&par_p_index=&p_index=&startTime=' + starttime
                                     + '&endTime=' + yesterday + '&page=' + str(page), callback=self.parse)
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
                                     '&craft_index=13167&par_p_index=&p_index=&startTime=' + starttime
                                     + '&endTime=' + yesterday + '&page=' + str(page), callback=self.parse)
