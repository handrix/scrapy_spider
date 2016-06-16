# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class CnblogItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    jobName = scrapy.Field()
    salary = scrapy.Field()
    date = scrapy.Field()
    jobYear = scrapy.Field()
    number = scrapy.Field()
    place = scrapy.Field()
    jobCluster = scrapy.Field()
    edu = scrapy.Field()
    jobClass = scrapy.Field()
    context = scrapy.Field()

