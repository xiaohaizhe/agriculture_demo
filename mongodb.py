# -*- encoding: utf-8 -*-
import json
from datetime import datetime, date, timedelta
import pymongo
from bson import ObjectId
from dateutil.relativedelta import relativedelta
from flask import Flask
from flask_pymongo import PyMongo
import re
from province_city import province

'''
@File    :   mongodb.py    
@Contact :   puyuting@hiynn.com

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2019/4/12 17:34   Ting      1.0         None
'''
app = Flask(__name__)
app.config.update(
    MONGO_URI='mongodb://agri_demo_user:123456@127.0.0.1:27017/agriculture_demo'
)

mongo = PyMongo(app)
mofcom = mongo.db.strawberry_price
nmc = mongo.db.forecast_and_assessment
natesc = mongo.db.pest_news
precipitation = mongo.db.precipitation
cfvin = mongo.db.strawberry_market_news
apple_price = mongo.db.apple_price
apple_zhengzhou = mongo.db.apple_zhengzhou
dpdata = mongo.db.diseases_or_pests

today = datetime.now().strftime('%Y-%m-%d')


# 方法一:定义JSON编码器，重写default()方法
class JSONEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, ObjectId):
            return str(o)
        if isinstance(o, datetime):
            return o.strftime('%Y-%m-%d')
        return json.JSONEncoder.default(self, o)


def deal_with_results(results):
    r = []
    for result in results:
        # 方法一：使用编码器
        result = json.dumps(result, cls=JSONEncoder)
        result = json.loads(result)
        r.append(result)
    return r


# mofcom相关方法
'''根据日期查询'''


def strawberry_query_by_date(sdate, edate, page, number):
    result = {}
    elements_number = mofcom.find({"date": {'$gte': sdate, '$lte': edate}}).count()
    # print("总页：" + str(elements_number))
    page_size = 0
    if elements_number % number == 0:
        page_size = elements_number / number
    else:
        page_size = elements_number // number + 1
    results = mofcom.find({"date": {'$gte': sdate, '$lte': edate}}).sort('date', pymongo.DESCENDING).skip(
        (page - 1) * number).limit(number)
    r = deal_with_results(results)
    result['page_size'] = page_size
    result['total_elements'] = elements_number
    result['data'] = r
    return result


def get_strawberry_price_analyse():
    results = []
    results.append(strawberry_price_analyse(""))
    for pro in province:
        r = strawberry_price_analyse(pro)
        if r == None:
            continue
        results.append(r)
    return results


def strawberry_price_analyse(range):
    result = mofcom.find().sort('date', pymongo.DESCENDING).limit(1)
    result = json.dumps(result[0], cls=JSONEncoder)
    result = json.loads(result)
    date = result['date']
    print(date)
    date = datetime.strptime(date, '%Y-%m-%d')
    isValid = mofcom.find({"date": date, 'province': {'$regex': range}}).count()
    if isValid == 0:
        return None
    else:
        results1 = mofcom.find({"date": date, 'province': {'$regex': range}})
        # 全国昨日均价
        average_yesterday = get_average(results1)
        # print(range + "昨日均价:" + str(average_yesterday))
        # last_year = (date.today() + timedelta(days=-1) - relativedelta(months=12)).strftime('%Y-%m-%d')
        # last_year = datetime.strptime(last_year, '%Y-%m-%d')
        last_year = date - relativedelta(months=12)
        results2 = mofcom.find({"date": last_year, 'province': {'$regex': range}})
        # 全国昨日同比价格
        average_last_year = get_average(results2)
        # print("全国昨日同比价格:" + str(average_last_year))
        # day_before_yesterday = (date.today() + timedelta(days=-2)).strftime('%Y-%m-%d')
        # day_before_yesterday = datetime.strptime(day_before_yesterday, '%Y-%m-%d')
        day_before_yesterday = date + timedelta(days=-1)
        results3 = mofcom.find({"date": day_before_yesterday, 'province': {'$regex': range}})
        # 全国昨日环比价格
        average_day_before_yesterday = get_average(results3)
        # print("全国昨日环比价格:" + str(average_day_before_yesterday))
        # 环比增长(下降)率
        if average_day_before_yesterday == 0:
            day_on_day_rate = None
        else:
            day_on_day_rate = round((average_yesterday / average_day_before_yesterday - 1), 3)
        # 同比增长(下降)率
        if average_last_year == 0:
            year_on_year_rate = None
        else:
            year_on_year_rate = round((average_yesterday / average_last_year - 1), 3)

        result = {}
        if range == '':
            result['province'] = 'nationwide'
        else:
            result['province'] = range
        result['average_latest'] = average_yesterday
        result['day_on_day_rate'] = day_on_day_rate
        result['year_on_year_rate'] = year_on_year_rate
        return result


def get_average_apple(results):
    sum = 0
    count = 0
    for result in results:
        sum += result['average_price']
        count += 1
    if count == 0:
        return 0
    else:
        average = round(sum / count, 2)
        return average


def get_average(results):
    sum = 0
    count = 0
    for result in results:
        sum += result['price']
        count += 1
    if count == 0:
        return 0
    else:
        average = round(sum / count, 2)
        return average


'''根据市场名查询，使用模糊查询'''


def query_by_market(market, page, number):
    results = mofcom.find({"market": {'$regex': market}}).sort('date', pymongo.DESCENDING).skip(
        (page - 1) * number).limit(
        number)
    r = deal_with_results(results)
    print(len(r))
    return r


'''根据价格查询，价格大于'''


def query_by_price_gt(price, page, number):
    results = mofcom.find({"price": {'$gt': price}}).sort('date', pymongo.DESCENDING).skip((page - 1) * number).limit(
        number)
    r = deal_with_results(results)
    print(len(r))
    return r


'''根据价格查询，价格小于'''


def query_by_price_lt(price, page, number):
    results = mofcom.find({"price": {'$lt': price}}).sort('date', pymongo.DESCENDING).skip((page - 1) * number).limit(
        number)
    r = deal_with_results(results)
    print(len(r))
    return r


# nmc相关方法
'''根据类型查找相关报道'''


def query_by_type(type):
    results = nmc.find({"type": type})
    r = deal_with_results(results)
    print(len(r))
    return r


# 最新农业气象预报与评估
def get_latest_forecast_and_assessment():
    results = nmc.find().sort('date', pymongo.DESCENDING).limit(1)
    r = deal_with_results(results)
    return r


# 病虫害新闻列表
def get_natesc_newsList(page, number):
    result = {}
    elements_number = natesc.find().count()
    page_size = 0
    if elements_number % number == 0:
        page_size = elements_number / number
    else:
        page_size = elements_number // number + 1
    results = natesc.find().sort('date', pymongo.DESCENDING).skip(
        (page - 1) * number).limit(number)
    r = deal_with_results(results)
    result['page_size'] = page_size
    result['total_elements'] = elements_number
    result['data'] = r
    return result


# 降水量
def get_precipitation():
    date = datetime.strptime(today, "%Y-%m-%d")
    results = precipitation.find({'date': date})
    r = deal_with_results(results)
    return r


# 草莓价格市场新闻
def get_cfvin_newsList(page, number):
    result = {}
    elements_number = cfvin.find().count()
    page_size = 0
    if elements_number % number == 0:
        page_size = elements_number / number
    else:
        page_size = elements_number // number + 1
    results = cfvin.find().sort('date', pymongo.DESCENDING).skip(
        (page - 1) * number).limit(number)
    r = deal_with_results(results)
    result['page_size'] = page_size
    result['total_elements'] = elements_number
    result['data'] = r
    return result


# 苹果期货数据
def apple_futures_data():
    result = apple_zhengzhou.find().sort('date', pymongo.DESCENDING).limit(1)
    result = json.dumps(result[0], cls=JSONEncoder)
    result = json.loads(result)
    date = result['date']
    date = datetime.strptime(date, '%Y-%m-%d')
    result = apple_zhengzhou.find({"date": date})
    result = deal_with_results(result)
    return result


# 苹果价格
def apple_query_by_date(sdate, edate, page, number):
    result = {}
    elements_number = apple_price.find({"date": {'$gte': sdate, '$lte': edate}}).count()
    # print("总页：" + str(elements_number))
    page_size = 0
    if elements_number % number == 0:
        page_size = elements_number / number
    else:
        page_size = elements_number // number + 1
    results = apple_price.find({"date": {'$gte': sdate, '$lte': edate}}).sort('date', pymongo.DESCENDING).skip(
        (page - 1) * number).limit(number)
    r = deal_with_results(results)
    result['page_size'] = page_size
    result['total_elements'] = elements_number
    result['data'] = r
    return result


def get_apple_price_analyse():
    results = []
    results.append(apple_price_analyse(""))
    for pro in province:
        r = apple_price_analyse(pro)
        if r == None:
            continue
        results.append(r)
    return results


def apple_price_analyse(range):
    # 获取苹果价格最新数据日期
    result = apple_price.find().sort('date', pymongo.DESCENDING).limit(1)
    result = json.dumps(result[0], cls=JSONEncoder)
    result = json.loads(result)
    date = result['date']
    date = datetime.strptime(date, '%Y-%m-%d')
    isValid = apple_price.find({"date": date, 'province': {'$regex': range}}).count()
    print("isValid:"+str(isValid))
    if isValid == 0:
        return None
    else:
        results1 = apple_price.find({"date": date, 'province': {'$regex': range}})
        # 全国最新日期均价
        average_yesterday = get_average_apple(results1)
        # print(range + "最新日期均价:" + str(average_yesterday))
        last_year = date - relativedelta(months=12)
        results2 = apple_price.find({"date": last_year, 'province': {'$regex': range}})
        # 全国最新日期均价同比价格
        average_last_year = get_average_apple(results2)
        # print("全国最新日期均价同比价格:" + str(average_last_year))
        day_before_yesterday = date + timedelta(days=-1)
        results3 = apple_price.find({"date": day_before_yesterday, 'province': {'$regex': range}})
        # 全国最新日期均价环比价格
        average_day_before_yesterday = get_average_apple(results3)
        # print("全国昨日环比价格:" + str(average_day_before_yesterday))
        # 环比增长(下降)率
        if average_day_before_yesterday == 0:
            day_on_day_rate = None
        else:
            day_on_day_rate = round((average_yesterday / average_day_before_yesterday - 1), 3)
        # 同比增长(下降)率
        if average_last_year == 0:
            year_on_year_rate = None
        else:
            year_on_year_rate = round((average_yesterday / average_last_year - 1), 3)

        result = {}
        if range == '':
            result['province'] = 'nationwide'
        else:
            result['province'] = range
        result['average_latest'] = average_yesterday
        result['day_on_day_rate'] = day_on_day_rate
        result['year_on_year_rate'] = year_on_year_rate
        return result


# def deal_with_data():
#     s = "http://crop.agridata.cn/disease/16-贮粮/"
#     results = dpdata.find({"first_level": "贮粮"})
#     for result in results:
#         html = result["html"]
#         # print("原html:"+html)
#         if "img" in html and "src" in html:
#             shtml = html.split('img border="0" src=')
#             html = shtml[0]
#             for s1 in shtml[1:]:
#                 sss = s1.split("jpg")
#                 st = sss[0]
#                 s2 = st[0:1] + s + st[1:] + "jpg"
#                 s1 = s2
#                 for i in sss[1:]:
#                     s1 += i
#                 html += 'img border="0" src=' + s1
#         # print("修改过后的html:"+html)
#         condition = {'first_level': result['first_level'], 'type': result['type'], 'name': result['name'],
#                      'second_level': result['second_level']}
#         result['html'] = html
#         res = dpdata.update_one(condition, {'$set': result})
#         print(res)
