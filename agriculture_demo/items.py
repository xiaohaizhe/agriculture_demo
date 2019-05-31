# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class AgricultureDemoItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class MofcomItem(scrapy.Item):
    # 日期
    date = scrapy.Field()
    # 产品名
    name = scrapy.Field()
    # 价格
    price = scrapy.Field()
    # 价格单位
    measurement_unit = scrapy.Field()
    # 市场
    market = scrapy.Field()
    # 省份
    province = scrapy.Field()


# 图片
class ImageItem(scrapy.Item):
    # 文件夹名称
    file_name = scrapy.Field()
    # 图片下载地址
    image_url = scrapy.Field()
    # 图片名称
    image_name = scrapy.Field()


class NmcItem(scrapy.Item):
    # 时间
    date = scrapy.Field()
    # 作者
    author = scrapy.Field()
    # 标题
    title = scrapy.Field()
    # 二级标题
    subhead = scrapy.Field()
    # 内容
    content = scrapy.Field()
    # 类型
    type = scrapy.Field()
    # 图片地址
    image_urls = scrapy.Field()


# 病虫害新闻
class NatescItem(scrapy.Field):
    # 标题
    title = scrapy.Field()
    # 时间
    date = scrapy.Field()
    # 链接
    link = scrapy.Field()


# Precipitation(前30城市)
class Precipitation(scrapy.Field):
    image_url = scrapy.Field()
    date = scrapy.Field()
    data = scrapy.Field()


# 草莓行情新闻
class CfvinItem(scrapy.Field):
    # 标题
    title = scrapy.Field()
    # 日期
    date = scrapy.Field()
    # 新闻来源
    source = scrapy.Field()
    # 作者
    author = scrapy.Field()
    # 内容
    content = scrapy.Field()


# 苹果交易所价格
class AppleZhengzhouItem(scrapy.Item):
    # 时间
    date = scrapy.Field()
    # 品种月份
    variety_month = scrapy.Field()
    # 昨日结算价格
    settlement_price_yesterday = scrapy.Field()
    # 今日结算价格
    settlement_price_today = scrapy.Field()
    # 今日开盘价格
    opening_price = scrapy.Field()
    # 今日收盘价格
    closing_price = scrapy.Field()
    # 最高价
    top_price = scrapy.Field()
    # 最低价
    bottom_price = scrapy.Field()
    # 涨跌1 = closing_price - settlement_price_yesterday
    # 涨跌2 = settlement_price_today - settlement_price_yesterday
    # 成交量（手）
    number_of_transactions = scrapy.Field()
    # 空盘量
    open_interest = scrapy.Field()
    # 成交额
    turnover = scrapy.Field()


# 苹果价格
class AppleAgronetItem(scrapy.Item):
    # 日期
    date = scrapy.Field()
    # 品种
    variety = scrapy.Field()
    # 批发市场
    terminal_market = scrapy.Field()
    # 最高价
    top_price = scrapy.Field()
    # 最低价
    bottom_price = scrapy.Field()
    # 均价
    average_price = scrapy.Field()
    # 计量单位
    measurement_unit = scrapy.Field()
    # 省份
    province = scrapy.Field()


# 作物病虫害数据库
class DiseasesOrPests(scrapy.Item):
    # 一级目录
    first_level = scrapy.Field()
    # 二级目录
    second_level = scrapy.Field()
    # 病害/虫害
    type = scrapy.Field()
    # 病虫害名称
    name = scrapy.Field()
    # html详情
    html = scrapy.Field()


class Weather(scrapy.Item):
    # 省份
    province = scrapy.Field()
    # 城市
    name = scrapy.Field()
    # 温度值
    value = scrapy.Field()
    # 更新时间
    update_time = scrapy.Field()
