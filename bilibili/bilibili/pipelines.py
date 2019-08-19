# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql
from bilibili.settings import HOST,PORT,USER,PASSWORD,DATABASE,CHARSET

class BilibiliPipeline(object):
    def __init__(self):
        self.connect = pymysql.connect(
            host=HOST,
            port=PORT,
            user=USER,
            password=PASSWORD,
            database=DATABASE,
            charset=CHARSET)

    def open_spider(self, spider):
        self.cursor = self.connect.cursor()
        self.insert = "insert into rank_all (href,title) values (%s,%s)"

    # spider运行时使用
    def process_item(self, item, spider):
        try:
            row = self.cursor.execute(self.insert, [item['href'],item['title']])
        except:
            print("已有记录")
        else:
            if row > 0:
                self.connect.commit()
            else:
                self.connect.rollback()
        return item

    # spider关闭时使用
    def close_spider(self, spider):
        self.cursor.close()
        self.connect.close()
