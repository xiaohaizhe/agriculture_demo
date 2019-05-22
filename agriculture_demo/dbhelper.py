import pymongo
from agriculture_demo.settings import mongo_host, mongo_port, mongo_db_name, user, password


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

