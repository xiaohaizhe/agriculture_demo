# -*- coding: utf-8 -*-
import datetime

import scrapy

from agriculture_demo.items import ImageItem, Precipitation

today = datetime.datetime.now().strftime('%Y-%m-%d')


class SpiderNmc1Spider(scrapy.Spider):
    name = 'spider_nmc_precipitation'
    allowed_domains = ['nmc.cn']
    start_urls = ['http://www.nmc.cn/publish/observations/24hour-precipitation-08.html']

    def parse(self, response):
        result = response.xpath("//body")
        precipitation = Precipitation()
        img_block = result.xpath(".//div[@id='maincontent']//div[@class='imgblock']")
        if img_block:
            image_url = img_block.xpath("./img/@src").extract_first()
            if '?' in image_url:
                imageItem = ImageItem()
                imageItem['file_name'] = 'precipitation'
                imageItem['image_url'] = image_url
                imageItem['image_name'] = today
                yield imageItem
                precipitation['image_url'] = image_url
        table = result.xpath(".//div[@id='text']/table//tr[position()>1]")
        precipitation['date'] = datetime.datetime.strptime(today, "%Y-%m-%d")
        data = []
        for tr in table:
            temp = {}
            # 序号
            temp['serial_number'] = tr.xpath("./td[1]/text()").extract_first()
            # 站点编号
            temp['portal_number'] = tr.xpath("./td[2]/text()").extract_first()
            # 站点名
            temp['portal_name'] = tr.xpath("./td[3]/a/text()").extract_first()
            # 所在地区
            temp['province'] = tr.xpath("./td[4]/a/text()").extract_first()
            # Precipitation（mm）
            temp['amount_of_precipitation'] = tr.xpath("./td[5]/text()").extract_first()
            data.append(temp)
        precipitation['data'] = data
        yield precipitation


