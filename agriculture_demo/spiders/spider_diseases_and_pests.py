# -*- coding: utf-8 -*-
import scrapy
from agriculture_demo.items import DiseasesOrPests
from flask_pymongo import PyMongo
from flask import Flask
from mongodb import deal_with_results, JSONEncoder
import json
from agriculture_demo.items import ImageItem

'''
不在定时任务中，
已经手动爬过整个库
'''
app = Flask(__name__)
app.config.update(
    MONGO_URI='mongodb://agri_demo_user:123456@127.0.0.1:27017/agriculture_demo'
)


class SpiderDiseasesAndPestsSpider(scrapy.Spider):
    name = 'spider_diseases_and_pests'
    allowed_domains = ['crop.agridata.cn']
    start_urls = ['http://crop.agridata.cn/disease/16-%E8%B4%AE%E7%B2%AE/indexchuliang.htm']

    def parse(self, response):
        mongo = PyMongo(app)
        dpdata = mongo.db.diseases_or_pests
        data= [
            "水稻",
            "麦类",
            "玉米",
            "杂粮",
            "豆类",
            "薯类",
            "棉麻",
            "油料",
            "糖烟",
            "茶桑",
            "药用植物",
            "杂草",
            "地下害虫",
            "农田鼠害",
            "贮粮"
        ]
        for d in data:
            results1 = dpdata.find({"first_level": d})
            for result in results1:
                result = json.dumps(result, cls=JSONEncoder)
                result = json.loads(result)
                html = result["html"]
                html = html.split('src="')
                count = 0
                total = 0
                for s in html:
                    if count % 2 == 1:
                        total += 1
                        count += 1
                        s = s.split('"')[0]
                        imageItem = ImageItem()
                        imageItem['file_name'] = 'diseases_and_pests'
                        imageItem['image_url'] = s
                        if "second_level" in result.keys() and result["second_level"] != None:
                            if total > 1:
                                image_name = result["first_level"] + "_" + result["second_level"] + "_" + result[
                                    "name"] + "_" + str(total)
                            else:
                                image_name = result["first_level"] + "_" + result["second_level"] + "_" + result["name"]
                        else:
                            if total > 1:
                                image_name = result["first_level"] + "_" + result["name"] + "_" + str(total)
                            else:
                                image_name = result["first_level"] + "_" + result["name"]
                        imageItem['image_name'] = image_name
                        yield imageItem
                        # print(s)
                    else:
                        count += 1
                        continue
        # results = response.xpath("//table//table//tr[11]//td[3]//font//a")
        # count = 0
        # for result in results:
        #     count += 1
        #     name = result.xpath("./text()").extract_first()
        #     print(name)
        #     link = result.xpath("./@href").extract_first()
        #     link = "http://crop.agridata.cn/disease/16-贮粮/" + link
        #     print(link)
        #     print(str(count) + "." + name.strip() + '-' + link)
        #     yield scrapy.Request(link, callback=self.parse_third, meta={"name": name, "count": count})

    # def parse_second(self, response):
    #     second_level = response.meta['name']
    #     count = response.meta['count']
    #     results = response.xpath("//table//tr//td//a")
    #     for result in results:
    #         name = result.xpath("./text()").extract_first()
    #         link = result.xpath("./@href").extract_first()
    #         link = "http://crop.agridata.cn/disease/15-农田鼠害/"+link
    #         if name != None:
    #             yield scrapy.Request(link, callback=self.parse_third, meta={"name": name,"second_level":second_level})
    #         else:
    #             name = result.xpath("./font/text()").extract_first()
    #             if name!=None:
    #                 yield scrapy.Request(link, callback=self.parse_third, meta={"name": name, "second_level": second_level})
    #             else:
    #                 continue
    # result = response.xpath("//table//tr[7]//td[2]")
    # name = result.xpath(".//font[position()>0]/text()").extract()
    # print(name)
    # name_r = ''
    # for s in name:
    #     name_r += s
    # link = result.xpath(".//a/@href").extract_first()
    # link = "http://crop.agridata.cn/disease/13－药用植物/"+link
    # yield scrapy.Request(link, callback=self.parse_third, meta={"name": name_r.strip(), "second_level": second_level})

    # def parse_third(self, response):
    #     # second_level = response.meta['name']
    #     name = response.meta['name']
    #     html = response.xpath("//body").extract_first()
    #     data = DiseasesOrPests()
    #     data['first_level'] = "贮粮"
    #     data['second_level'] = None
    #     data['type'] = "虫害"
    #     data['name'] = name
    #     data['html'] = html
    #     yield data
    # if count == 1:
    #     print(str(count) + ".豆类-病害-" + deseases_or_pests_name)
    #     data = DiseasesOrPests()
    #     data['first_level'] = '豆类'
    #     data['second_level'] = '蚕豆'
    #     data['type'] = '病害'
    #     data['name'] = deseases_or_pests_name
    #     data['html'] = html
    #     yield data
    # elif count > 1 and count <=8:
    #     print(str(count) + ".豆类-虫害-" + deseases_or_pests_name)
    #     data = DiseasesOrPests()
    #     data['first_level'] = '豆类'
    #     data['second_level'] = '蚕豆'
    #     data['type'] = '虫害'
    #     data['name'] = deseases_or_pests_name
    #     data['html'] = html
    #     yield data
    # elif count == 9:
    #     print(str(count) + ".豆类-病害-" + deseases_or_pests_name)
    #     data = DiseasesOrPests()
    #     data['first_level'] = '豆类'
    #     data['second_level'] = '豌豆'
    #     data['type'] = '病害'
    #     data['name'] = deseases_or_pests_name
    #     data['html'] = html
    #     yield data
    # else:
    #     print(str(count) + ".豆类-病害-" + deseases_or_pests_name)
    #     data = DiseasesOrPests()
    #     data['first_level'] = '豆类'
    #     data['second_level'] = '绿豆'
    #     data['type'] = '病害'
    #     data['name'] = deseases_or_pests_name
    #     data['html'] = html
    #     yield data

    # if count >= 1 and count <= 11:
    #     print(str(count) + ".大麦-病害-" + deseases_or_pests_name)
    #     data = DiseasesOrPests()
    #     data['first_level'] = '麦类'
    #     data['second_level'] = '大麦'
    #     data['type'] = '病害'
    #     data['name'] = deseases_or_pests_name
    #     data['html'] = html
    #     yield data
    # elif count >= 12 and count <= 39:
    #     print(str(count) + ".大麦-虫害-" + deseases_or_pests_name)
    #     data = DiseasesOrPests()
    #     data['first_level'] = '麦类'
    #     data['second_level'] = '大麦'
    #     data['type'] = '虫害'
    #     data['name'] = deseases_or_pests_name
    #     data['html'] = html
    #     yield data
    # elif count >= 40 and count <= 85:
    #     print(str(count) + ".小麦-病害-" + deseases_or_pests_name)
    #     data = DiseasesOrPests()
    #     data['first_level'] = '麦类'
    #     data['second_level'] = '小麦'
    #     data['type'] = '病害'
    #     data['name'] = deseases_or_pests_name
    #     data['html'] = html
    #     yield data
    # elif count >= 86 and count <= 115:
    #     print(str(count) + ".小麦-虫害-" + deseases_or_pests_name)
    #     data = DiseasesOrPests()
    #     data['first_level'] = '麦类'
    #     data['second_level'] = '小麦'
    #     data['type'] = '虫害'
    #     data['name'] = deseases_or_pests_name
    #     data['html'] = html
    #     yield data
    # elif count >= 116 and count <= 121:
    #     print(str(count) + ".荞麦-病害-" + deseases_or_pests_name)
    #     data = DiseasesOrPests()
    #     data['first_level'] = '麦类'
    #     data['second_level'] = '荞麦'
    #     data['type'] = '病害'
    #     data['name'] = deseases_or_pests_name
    #     data['html'] = html
    #     yield data
    # elif count == 122:
    #     print(str(count) + ".荞麦-虫害-" + deseases_or_pests_name)
    #     data = DiseasesOrPests()
    #     data['first_level'] = '麦类'
    #     data['second_level'] = '荞麦'
    #     data['type'] = '虫害'
    #     data['name'] = deseases_or_pests_name
    #     data['html'] = html
    #     yield data
    # elif count >= 123 and count <= 131:
    #     print(str(count) + ".燕麦-病害-" + deseases_or_pests_name)
    #     data = DiseasesOrPests()
    #     data['first_level'] = '麦类'
    #     data['second_level'] = '燕麦'
    #     data['type'] = '病害'
    #     data['name'] = deseases_or_pests_name
    #     data['html'] = html
    #     yield data
    # elif count >= 132 and count <= 134:
    #     print(str(count) + ".燕麦-虫害-" + deseases_or_pests_name)
    #     data = DiseasesOrPests()
    #     data['first_level'] = '麦类'
    #     data['second_level'] = '燕麦'
    #     data['type'] = '虫害'
    #     data['name'] = deseases_or_pests_name
    #     data['html'] = html
    #     yield data
    # elif count >= 135 and count <= 139:
    #     print(str(count) + ".其他-病害-" + deseases_or_pests_name)
    #     data = DiseasesOrPests()
    #     data['first_level'] = '麦类'
    #     data['second_level'] = '其他'
    #     data['type'] = '病害'
    #     data['name'] = deseases_or_pests_name
    #     data['html'] = html
    #     yield data
    # else:
    #     print(str(count) + ".其他-虫害-" + deseases_or_pests_name)
    #     data = DiseasesOrPests()
    #     data['first_level'] = '麦类'
    #     data['second_level'] = '其他'
    #     data['type'] = '虫害'
    #     data['name'] = deseases_or_pests_name
    #     data['html'] = html
    #     yield data
