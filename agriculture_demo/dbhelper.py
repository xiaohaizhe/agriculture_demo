import pymongo
from agriculture_demo.settings import mongo_host, mongo_port, mongo_db_name, user, password
from datetime import datetime

today = datetime.now()


class DBHelper():
    def __init__(self):
        host = mongo_host
        port = mongo_port
        client = pymongo.MongoClient(host=host, port=port)
        dbname = mongo_db_name
        mydb = client[dbname]
        mydb.authenticate(name=user, password=password)
        self.mydb = mydb

    def vertify_and_insert(self, item, collection, *args):
        col = self.mydb[collection]
        condition = {}
        for s in args:
            condition[s] = item[s]
        isValid = col.find(condition).count()
        if isValid == 0:
            data = dict(item)
            col.insert(data)

    def get_latest_date(self, collection):
        col = self.mydb[collection]
        count = col.find().count()
        if count <= 0:
            return None
        else:
            results = col.find().sort("date", pymongo.DESCENDING).limit(1)
            return results[0]["date"]


if __name__ == '__main__':
    # dbhelper = DBHelper()
    # date = dbhelper.get_latest_date("strawberry_price")
    # today = datetime.today()
    # days = (today-date).days
    # print(type(date))
    # print(days)
    for i in range(1, 2):
        print(str(i))
