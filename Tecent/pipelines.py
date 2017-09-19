# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from pymongo import MongoClient
from scrapy.conf import settings
import json


class TecentPipeline(object):

    def __init__(self):

        self.file = open('tecten.json', 'w')

    def process_item(self, item, spider):
        result = json.dumps(dict(item), ensure_ascii=False) + ',\n'
        self.file.write(result)
        return item

    def close_sipder(self, spider):
        self.file.close()


class MonogoPipeline(object):

    def __init__(self):

        host = settings['MONGO_HOST']
        port = settings['MONGO_PORT']
        databases = settings['MONGO_DBNAME']
        colname = settings['MONGO_COLNAME']

        self.heander = MongoClient(host, port)
        self.db = self.heander[databases]
        self.col = self.db[colname]

    def process_item(self, item, spider):
        date = dict(item)
        self.col.insert(date)
        return item

    def close_spider(self):
        self.heander.close()