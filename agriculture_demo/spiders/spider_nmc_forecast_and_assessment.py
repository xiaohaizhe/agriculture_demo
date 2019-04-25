# -*- coding: utf-8 -*-
import datetime

import scrapy

from agriculture_demo.items import NmcItem, ImageItem

today = datetime.datetime.now().strftime('%Y-%m-%d')


class SpiderNmcSpider(scrapy.Spider):
    name = 'spider_nmc_forecast_and_assessment'
    allowed_domains = ['nmc.cn']
    start_urls = ['http://www.nmc.cn/publish/crop/index.htm']

    def parse(self, response):
        result = response.xpath("//body")
        text = result.xpath(".//div[@id='maincontent']//div[@id='text']")
        title = result.xpath(".//ul[@class='dropdown-menu']//a[@class='actived']/text()").extract_first()
        if text:
            text_date = result.xpath(".//div[@class='author']/b/text()").extract()
            date_s = ''
            i = 0
            for d in text_date:
                if i < 2:
                    date_s += d + '-'
                else:
                    date_s += d + ' '
                i += 1
            get_date = datetime.datetime.strptime(date_s.strip(), '%Y-%m-%d')
            if (datetime.datetime.now() - get_date).days < 100:
                nmc_item = NmcItem()
                nmc_item['title'] = text.xpath(".//div[@class='title']/text()").extract_first().strip()
                nmc_item['author'] = text.xpath(".//div[@class='author']/text()").extract_first().strip()
                if text.xpath(".//div[@class='subhead']"):
                    subheads = text.xpath(".//div[@class='subhead']/text()").extract()
                    subheads_r = []
                    for subhead in subheads:
                        subheads_r.append(subhead.strip())
                    nmc_item['subhead'] = subheads_r
                nmc_item['content'] = text.xpath(".//div[@class='writing']/p/text()").extract()
                nmc_item['date'] = datetime.datetime.strptime(date_s.strip(), "%Y-%m-%d")
                image_urls = text.xpath(".//div[@class='writing']//img/@src").extract()
                image_urls_r = []
                count = 1
                for image_url in image_urls:
                    if '?' in image_url:
                        imageItem = ImageItem()
                        imageItem['file_name'] = 'forecast_and_assessment'
                        imageItem['image_url'] = image_url
                        imageItem['image_name'] = today + '_' + str(count)
                        count += 1
                        yield imageItem
                        image_urls_r.append(image_url)
                nmc_item['image_urls'] = image_urls_r
                nmc_item['type'] = title
                yield nmc_item
