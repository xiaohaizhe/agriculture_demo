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
from mongodb import query_by_type, get_price_analyse, query_by_date, get_natesc_newsList, get_precipitation, \
    get_latest_forecast_and_assessment, get_cfvin_newsList

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
         "spider_cfvin"],))
    mp.start()
    mp.join()


class Config(object):
    JOBS = [
        {
            'id': 'job1',
            'func': process,
            'trigger': 'interval',
            'hours': 24
        }
    ]

    SCHEDULER_API_ENABLED = True


@app.route('/orders/<int:order_id>', methods=['GET'])
def get_order_id(order_id):
    print(type(order_id))
    # date = '2019-04-11'
    # result = query(date)
    # market = '江苏'
    # result = query_by_market(market)
    # sdate = datetime.datetime.strptime("2019-04-10", '%Y-%m-%d')
    # edate = datetime.datetime.strptime("2019-04-16", '%Y-%m-%d')
    # result = query_by_date(sdate, edate, 1, 2)
    t = '农业气象月报'
    result = query_by_type(t)
    return jsonify(result)


@app.route('/api/strawberry/get_price_detail', methods=['GET'])
def get_price_detail():
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
        result = query_by_date(sdate, edate, page, number)
        response['code'] = 0
        response['msg'] = '成功'
        response['data'] = result['data']
        response['page_size'] = result['page_size']
        response['total_elements'] = result['total_elements']
    return jsonify(response)


@app.route('/api/strawberry/get_price_analyse', methods=['POST', 'GET'])
def price_analyse():
    response = {}
    result = get_price_analyse()
    response['code'] = 0
    response['msg'] = '成功'
    response['data'] = result
    return jsonify(response)


@app.route('/api/pd&ip/newsList', methods=['GET'])
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


@app.route('/api/nmc/get_latest_forecast_and_assessment', methods=['GET'])
def latest_forecast_and_assessment():
    result = get_latest_forecast_and_assessment()
    response = {}
    response['code'] = 0
    response['msg'] = '成功'
    response['data'] = result
    return jsonify(response)


@app.route('/api/cfvin/newsList', methods=['GET'])
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


if __name__ == '__main__':
    app.config.from_object(Config())
    if os.environ.get('WERKZEUG_RUN_MAIN') == 'true':
        scheduler = APScheduler()
        scheduler.api_enabled = True
        scheduler.init_app(app)
        scheduler.start()
    app.run(
        host='0.0.0.0',
        port=8080,
        debug=True
    )