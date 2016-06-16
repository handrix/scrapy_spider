# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json

class ZhilianPipeline(object):

    def __init__(self):
        self.file = open('job_data.txt', 'a')

    def process_item(self, item):
        self.file.write(item[job] + '@^@')
        self.file.close()
        return item