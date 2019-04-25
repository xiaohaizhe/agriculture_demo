# -*- coding: utf-8 -*-
import datetime

import scrapy

from agriculture_demo.items import NatescItem


class SpiderNatescSpider(scrapy.Spider):
    name = 'spider_natesc'
    allowed_domains = ['natesc.org.cn']
    start_urls = ['https://www.natesc.org.cn/sites/cb/List_28092_151760.html']

    def parse(self, response):
        natesc1 = NatescItem()
        result = response.xpath("//body//form//font[@class='style1_361']//table")
        results_unique = result.xpath(".//tr[1]")
        date = results_unique.xpath("./td[3]/span/text()").extract_first()[1:-1] + ' 09:00:00'
        get_date = datetime.datetime.strptime(date.strip(), '%Y-%m-%d %H:%M:%S')
        if (datetime.datetime.now() - get_date).days == 0:
            title = results_unique.xpath("./td[2]/a/text()").extract_first()
            link = 'https://www.natesc.org.cn' + results_unique.xpath("./td[2]/a/@href").extract_first()[5:]

            natesc1['title'] = title
            natesc1['date'] = datetime.datetime.strptime(date, "%Y-%m-%d %H:%M:%S")
            natesc1['link'] = link
            yield natesc1
            results = result.xpath(".//tr[position()>1]")
            for item in results:
                date = item.xpath("./td[3]/span/text()").extract_first()[1:-1] + ' 09:00:00'
                get_date = datetime.datetime.strptime(date.strip(), '%Y-%m-%d %H:%M:%S')
                if (datetime.datetime.now() - get_date).days == 0:
                    natesc = NatescItem()
                    title = item.xpath("./td[2]/a/text()").extract_first()
                    link = 'https://www.natesc.org.cn' + item.xpath("./td[2]/a/@href").extract_first()[5:]
                    natesc['title'] = title
                    natesc['date'] = datetime.datetime.strptime(date, "%Y-%m-%d %H:%M:%S")
                    natesc['link'] = link
                    yield natesc
                else:
                    break