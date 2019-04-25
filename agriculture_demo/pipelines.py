# -*- coding: utf-8 -*-
import pymongo
from scrapy import Request
from scrapy.pipelines.images import ImagesPipeline

from agriculture_demo.items import MofcomItem, ImageItem, NmcItem, NatescItem, Precipitation, CfvinItem, \
    AppleZhengzhouItem
from agriculture_demo.settings import mongo_host, mongo_port, mongo_db_name


# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class AgricultureDemoPipeline(object):

    def process_item(self, item, spider):
        return item


class MofcomPipeline(object):
    def __init__(self):
        host = mongo_host
        port = mongo_port
        dbname = mongo_db_name
        collection = 'strawberry_price'
        client = pymongo.MongoClient(host=host, port=port)
        mydb = client[dbname]
        self.post = mydb[collection]

    def process_item(self, item, spider):
        if isinstance(item, MofcomItem):
            data = dict(item)
            self.post.insert(data)
        return item


class NmcPipeline(object):
    def __init__(self):
        host = mongo_host
        port = mongo_port
        dbname = mongo_db_name
        collection = 'nmc'
        client = pymongo.MongoClient(host=host, port=port)
        mydb = client[dbname]
        self.post = mydb[collection]

    def process_item(self, item, spider):
        if isinstance(item, NmcItem):
            data = dict(item)
            self.post.insert(data)
        return item


class NatescPipeline(object):
    def __init__(self):
        host = mongo_host
        port = mongo_port
        dbname = mongo_db_name
        collection = 'natesc'
        client = pymongo.MongoClient(host=host, port=port)
        mydb = client[dbname]
        self.post = mydb[collection]

    def process_item(self, item, spider):
        if isinstance(item, NatescItem):
            data = dict(item)
            self.post.insert(data)
        return item


class PrecipitationPipeline(object):
    def __init__(self):
        host = mongo_host
        port = mongo_port
        dbname = mongo_db_name
        collection = 'precipitation'
        client = pymongo.MongoClient(host=host, port=port)
        mydb = client[dbname]
        self.post = mydb[collection]

    def process_item(self, item, spider):
        if isinstance(item, Precipitation):
            data = dict(item)
            self.post.insert(data)
        return item


class CfvinPipeline(object):
    def __init__(self):
        host = mongo_host
        port = mongo_port
        dbname = mongo_db_name
        collection = 'strawberry_market_news'
        client = pymongo.MongoClient(host=host, port=port)
        mydb = client[dbname]
        self.post = mydb[collection]

    def process_item(self, item, spider):
        if isinstance(item, CfvinItem):
            data = dict(item)
            self.post.insert(data)
        return item


class AppleZhengzhouPipeline(object):
    def __init__(self):
        host = mongo_host
        port = mongo_port
        dbname = mongo_db_name
        collection = "apple_zhengzhou"
        client = pymongo.MongoClient(host=host, port=port)
        mydb = client[dbname]
        self.post = mydb[collection]

    def process_item(self, item, spider):
        if isinstance(item, AppleZhengzhouItem):
            data = dict(item)
            self.post.insert(data)
        return item


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
