# -*- coding: utf-8 -*-
from scrapy import Request
from scrapy.pipelines.images import ImagesPipeline

from agriculture_demo.items import MofcomItem, ImageItem, NmcItem, NatescItem, Precipitation, CfvinItem, \
    AppleZhengzhouItem, AppleAgronetItem, Weather
from agriculture_demo.dbhelper import DBHelper


# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class AgricultureDemoPipeline(object):

    def process_item(self, item, spider):
        return item


class MofcomPipeline(object):
    def process_item(self, item, spider):
        if isinstance(item, MofcomItem):
            db = DBHelper()
            db.vertify_and_insert(item, "strawberry_price", "date", "market")
        return item


class NmcPipeline(object):
    def process_item(self, item, spider):
        if isinstance(item, NmcItem):
            db = DBHelper()
            db.vertify_and_insert(item, "forecast_and_assessment", "date", "title")
        return item


class NatescPipeline(object):
    def process_item(self, item, spider):
        if isinstance(item, NatescItem):
            db = DBHelper()
            db.vertify_and_insert(item, "pest_news", "date", "title")
        return item


class PrecipitationPipeline(object):
    def process_item(self, item, spider):
        if isinstance(item, Precipitation):
            db = DBHelper()
            db.vertify_and_insert(item, "precipitation", "date")
        return item


class CfvinPipeline(object):
    def process_item(self, item, spider):
        if isinstance(item, CfvinItem):
            db = DBHelper()
            db.vertify_and_insert(item, "strawberry_market_news", "date", "title")
        return item


class AppleZhengzhouPipeline(object):
    def process_item(self, item, spider):
        if isinstance(item, AppleZhengzhouItem):
            db = DBHelper()
            db.vertify_and_insert(item, "apple_zhengzhou", "date", "variety_month")
        return item


class AppleAgronetPipeline(object):
    def process_item(self, item, spider):
        if isinstance(item, AppleAgronetItem):
            db = DBHelper()
            db.vertify_and_insert(item, "apple_price", "date", "variety", "terminal_market")
        return item


class WeatherPipeline():
    def process_item(self, item, spider):
        if isinstance(item, Weather):
            db = DBHelper()
            db.vertify_and_update(item, "weather", "name")
        return item


# class DiseasesOrPestsPipeline(object):
#     def process_item(self, item, spider):
#         if isinstance(item, DiseasesOrPests):
#             db = DBHelper()
#             db.vertify_and_insert(item, "diseases_or_pests", "first_level", "second_level", "type", "name")
#         return item


class ImagePipeline(ImagesPipeline):
    def get_media_requests(self, item, info):  # 请求下载图片
        if isinstance(item, ImageItem):
            image_url = item['image_url']
            if image_url:
                yield Request(image_url,
                              meta={'image_name': item['image_name'],
                                    'file_name': item['file_name']})  # 添加meta是为了下面重命名文件名使用

    def file_path(self, request, response=None, info=None):
        # start of deprecation warning block (can be removed in the future)
        def _warn():
            from scrapy.exceptions import ScrapyDeprecationWarning
            import warnings
            warnings.warn('ImagesPipeline.image_key(url) and file_key(url) methods are deprecated, '
                          'please use file_path(request, response=None, info=None) instead',
                          category=ScrapyDeprecationWarning, stacklevel=1)

        # check if called from image_key or file_key with url as first argument
        if not isinstance(request, Request):
            _warn()
            url = request
        else:
            url = request.url

        # detect if file_key() or image_key() methods have been overridden
        if not hasattr(self.file_key, '_base'):
            _warn()
            return self.file_key(url)
        elif not hasattr(self.image_key, '_base'):
            _warn()
            return self.image_key(url)
        # end of deprecation warning block
        image_name = request.meta['image_name']
        file_name = request.meta['file_name']
        return file_name + '/%s.jpg' % image_name
