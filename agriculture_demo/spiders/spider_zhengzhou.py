# -*- coding: utf-8 -*-
import scrapy

from agriculture_demo.items import AppleZhengzhouItem


class SpiderZhengzhouSpider(scrapy.Spider):
    name = 'spider_zhengzhou'
    allowed_domains = ['app.czce.com.cn']
    start_urls = [
        'http://app.czce.com.cn/cms/cmsface/czce/newcms/calendarnewOne.jsp?curpath=/cn/sspz/pg/H770221index_1.htm&curpath1=']

    def parse(self, response):
        apples = response.xpath('//tbody//tr[position()<8]')
        date = response.xpath(
            "//div[@class='jysjtop']//div[@class='fr']/span/text()").extract_first().split()
        for apple in apples:
            item = AppleZhengzhouItem()
            print(response)
            item['date'] = date[0]
            item['variety_month'] = apple.xpath(".//td[1]/text()").extract_first()
            item['settlement_price_yesterday'] = apple.xpath(".//td[2]/text()").extract_first()
            item['settlement_price_today'] = apple.xpath(".//td[7]/text()").extract_first()
            item['opening_price'] = apple.xpath(".//td[3]/text()").extract_first()
            item['closing_price'] = apple.xpath(".//td[6]/text()").extract_first()
            item['top_price'] = apple.xpath(".//td[4]/text()").extract_first()
            item['bottom_price'] = apple.xpath(".//td[5]/text()").extract_first()
            item['number_of_transactions'] = apple.xpath(".//td[10]/text()").extract_first()
            item['open_interest'] = apple.xpath(".//td[11]/text()").extract_first()
            item['turnover'] = apple.xpath(".//td[13]/text()").extract_first()
            yield item
