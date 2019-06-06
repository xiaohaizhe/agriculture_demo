# -*- coding: utf-8 -*-
import scrapy

from agriculture_demo.items import AppleZhengzhouItem
from datetime import datetime

'''
只能获取当前最新数据
且最新数据为有效数据
'''


class SpiderZhengzhouSpider(scrapy.Spider):
    name = 'spider_zhengzhou'
    allowed_domains = ['app.czce.com.cn']
    start_urls = [
        'http://app.czce.com.cn/cms/cmsface/czce/newcms/calendarnewOne.jsp?curpath=/cn/sspz/pg/H770221index_1.htm&curpath1=']

    def parse(self, response):
        apples = response.xpath('//tbody//tr[position()<8]')
        date = response.xpath(
            "//div[@class='jysjtop']//div[@class='fr']/span/text()").extract_first().split()
        date = datetime.strptime(date[0].strip(), "%Y-%m-%d")
        if (datetime.now() - date).days < 3:
            for apple in apples:
                item = AppleZhengzhouItem()
                item['date'] = date
                item['variety_month'] = apple.xpath(".//td[1]/text()").extract_first()
                item['settlement_price_yesterday'] = self.deal_with_s(apple.xpath(".//td[2]/text()").extract_first())
                item['settlement_price_today'] = self.deal_with_s(apple.xpath(".//td[7]/text()").extract_first())
                item['opening_price'] = self.deal_with_s(apple.xpath(".//td[3]/text()").extract_first())
                item['closing_price'] = self.deal_with_s(apple.xpath(".//td[6]/text()").extract_first())
                item['top_price'] = self.deal_with_s(apple.xpath(".//td[4]/text()").extract_first())
                item['bottom_price'] = self.deal_with_s(apple.xpath(".//td[5]/text()").extract_first())
                item['number_of_transactions'] = self.deal_with_s(apple.xpath(".//td[10]/text()").extract_first())
                item['open_interest'] = self.deal_with_s(apple.xpath(".//td[11]/text()").extract_first())
                item['turnover'] = self.deal_with_s(apple.xpath(".//td[13]/text()").extract_first())
                print(item)
                yield item
        else:
            pass

    def deal_with_s(self, s):
        if "," in s:
            s = s.replace(",", "")
        return float(s)
