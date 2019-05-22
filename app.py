import datetime
import os
from multiprocessing import Process

from flask import Flask, jsonify, request
from flask_apscheduler import APScheduler
from scrapy.crawler import CrawlerRunner
from scrapy.utils.log import configure_logging
from scrapy.utils.project import get_project_settings
from twisted.internet import reactor

from log import Logger
from mongodb import query_by_type, get_strawberry_price_analyse, strawberry_query_by_date, get_natesc_newsList, \
    get_precipitation, get_latest_forecast_and_assessment, get_cfvin_newsList, apple_query_by_date, \
    get_apple_price_analyse, apple_futures_data, get_diseases_or_pests

log = Logger('agriculture.log', level='debug')
app = Flask(__name__)


def run_spider(s):
    configure_logging()
    runner = CrawlerRunner(get_project_settings())
    for ss in s:
        runner.crawl(ss)
    d = runner.join()
    d.addBoth(lambda _: reactor.stop())
    reactor.run()


def process():
    configure_logging()
    # 创建并启动子进程
    mp = Process(target=run_spider, args=(
        ["spider_mofcom", "spider_nmc_forecast_and_assessment", "spider_nmc_precipitation", "spider_natesc",
         "spider_cfvin", "spider_zhengzhou", "spider_agronet"]))
    mp.start()
    mp.join()


class Config(object):
    JOBS = [
        {
            'id': 'job1',
            'func': process,
            'trigger': 'interval',
            'hours': 1
        }
    ]

    SCHEDULER_API_ENABLED = True


@app.route('/api/apple/apple_futures_data', methods=['GET', 'POST'])
def apple_price():
    response = {}
    result = apple_futures_data()
    response['code'] = 0
    response['msg'] = '成功'
    response['data'] = result
    return jsonify(response)


@app.route('/api/strawberry/get_price_detail', methods=['GET'])
def strawberry_price_detail():
    response = {}
    try:
        sdate = request.values.get('sdate')
        edate = request.values.get('edate')
        page = int(request.values.get('page'))
        number = int(request.values.get('number'))
    except TypeError:
        response['code'] = 1
        response['msg'] = '参数不完整'
    else:
        sdate = datetime.datetime.strptime(sdate, '%Y-%m-%d')
        edate = datetime.datetime.strptime(edate, '%Y-%m-%d')
        result = strawberry_query_by_date(sdate, edate, page, number)
        response['code'] = 0
        response['msg'] = '成功'
        response['data'] = result['data']
        response['page_size'] = result['page_size']
        response['total_elements'] = result['total_elements']
    return jsonify(response)


@app.route('/api/apple/get_price_detail', methods=['GET'])
def apple_price_detail():
    response = {}
    try:
        sdate = request.values.get('sdate')
        if sdate == None:
            raise Exception
        edate = request.values.get('edate')
        if edate == None:
            raise Exception
        page = int(request.values.get('page'))
        number = int(request.values.get('number'))
    except Exception:
        response['code'] = 1
        response['msg'] = '参数不完整'
    else:
        sdate = datetime.datetime.strptime(sdate, '%Y-%m-%d')
        edate = datetime.datetime.strptime(edate, '%Y-%m-%d')
        result = apple_query_by_date(sdate, edate, page, number)
        response['code'] = 0
        response['msg'] = '成功'
        response['data'] = result['data']
        response['page_size'] = result['page_size']
        response['total_elements'] = result['total_elements']
    return jsonify(response)


@app.route('/api/strawberry/get_price_analyse', methods=['POST', 'GET'])
def price_analyse():
    response = {}
    result = get_strawberry_price_analyse()
    response['code'] = 0
    response['msg'] = '成功'
    response['data'] = result
    return jsonify(response)


@app.route('/api/apple/get_price_analyse', methods=['POST', 'GET'])
def apple_price_analyse():
    response = {}
    result = get_apple_price_analyse()
    response['code'] = 0
    response['msg'] = '成功'
    response['data'] = result
    return jsonify(response)


@app.route('/api/plant_diseases_and_insect_pests/newsList', methods=['GET'])
def get_plant_diseases_and_insect_pests_news():
    response = {}
    try:
        page = int(request.values.get('page'))
        number = int(request.values.get('number'))
    except TypeError:
        response['code'] = 1
        response['msg'] = '参数不完整'
    else:
        result = get_natesc_newsList(page, number)
        response['code'] = 0
        response['msg'] = '成功'
        response['data'] = result['data']
        response['page_size'] = result['page_size']
        response['total_elements'] = result['total_elements']
    return jsonify(response)


@app.route('/api/precipitation/list', methods=['GET'])
def precipitation():
    result = get_precipitation()
    response = {}
    response['code'] = 0
    response['msg'] = '成功'
    response['data'] = result
    return jsonify(response)


@app.route('/api/forecast_and_assessment/get_latest_forecast_and_assessment', methods=['GET'])
def latest_forecast_and_assessment():
    result = get_latest_forecast_and_assessment()
    response = {}
    response['code'] = 0
    response['msg'] = '成功'
    response['data'] = result
    return jsonify(response)


@app.route('/api/strawberry_market_news/newsList', methods=['GET'])
def cfvin_newsList():
    response = {}
    try:
        page = int(request.values.get('page'))
        number = int(request.values.get('number'))
    except TypeError:
        response['code'] = 1
        response['msg'] = '参数不完整'
    else:
        result = get_cfvin_newsList(page, number)
        response['code'] = 0
        response['msg'] = '成功'
        response['data'] = result['data']
        response['page_size'] = result['page_size']
        response['total_elements'] = result['total_elements']
    return jsonify(response)


@app.route('/api/diseases_or_pests/get_first_level', methods=['GET'])
def get_first_level():
    response = {}
    result = get_diseases_or_pests()
    response['code'] = 0
    response['msg'] = '成功'
    response['data'] = result
    return jsonify(response)


@app.route('/api/diseases_or_pests/get_second_level_or_names', methods=['GET'])
def get_second_level_or_names():
    response = {}
    try:
        first_level = request.values.get('first_level')
        if first_level == None:
            raise Exception
    except Exception:
        response['code'] = 1
        response['msg'] = '参数不完整'
    else:
        result = get_diseases_or_pests(first_level)
        response['code'] = 0
        response['msg'] = '成功'
        response['data'] = result
    return jsonify(response)


@app.route('/api/diseases_or_pests/get_names', methods=['GET'])
def get_names():
    response = {}
    try:
        first_level = (request.values.get('first_level'))
        if first_level == None:
            raise Exception
        second_level = (request.values.get('second_level'))
        if second_level == None:
            raise Exception
    except Exception:
        response['code'] = 1
        response['msg'] = '参数不完整'
    else:
        result = get_diseases_or_pests(first_level, second_level)
        response['code'] = 0
        response['msg'] = '成功'
        response['data'] = result
    return jsonify(response)


@app.route('/api/diseases_or_pests/get_details1', methods=['GET'])
def get_details1():
    response = {}
    try:
        first_level = (request.values.get('first_level'))
        if first_level == None:
            raise Exception
        second_level = (request.values.get('second_level'))
        if second_level == None:
            raise Exception
        name = (request.values.get('name'))
        if name == None:
            raise Exception
    except Exception:
        response['code'] = 1
        response['msg'] = '参数不完整'
    else:
        result = get_diseases_or_pests(first_level, second_level, name)
        response['code'] = 0
        response['msg'] = '成功'
        response['data'] = result
    return jsonify(response)


@app.route('/api/diseases_or_pests/get_details2', methods=['GET'])
def get_details2():
    response = {}
    try:
        first_level = (request.values.get('first_level'))
        if first_level == None:
            raise Exception
        name = (request.values.get('name'))
        if name == None:
            raise Exception
    except Exception:
        response['code'] = 1
        response['msg'] = '参数不完整'
    else:
        result = get_diseases_or_pests(first_level, name)
        response['code'] = 0
        response['msg'] = '成功'
        response['data'] = result
    return jsonify(response)


@app.route("/tomcat/test2")
def test():
    return "Hello,Apache!!!This is 8081."


if __name__ == '__main__':
    app.config.from_object(Config())
    if os.environ.get('WERKZEUG_RUN_MAIN') == 'true':
        scheduler = APScheduler()
        scheduler.api_enabled = True
        scheduler.init_app(app)
        scheduler.start()
    app.run(
        host='0.0.0.0',
        port=8081,
        debug=True
    )
