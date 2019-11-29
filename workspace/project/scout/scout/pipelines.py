# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scout.mysql import MySql

class MySql_data_Pipeline(object):
    def __init__(self):
        self.db = MySql('localhost', 'root', 'mysql', 'python')

    def process_item(self, item, spider):
        '''调用 item 里面的get_insert_data函数'''
        if hasattr(item, 'get_insert_data'):
            # 传参调用scout.db_sql里面的insert 方法
            insert_sql, data = item.get_insert_data()
            self.db.insert(insert_sql, data)

        return item
