# -*- coding:utf-8 -*-
from scrapy.contrib.spiders import CrawlSpider,Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.selector import Selector
from cnblog.items import CnblogItem
import sys
import string
import codecs
#sys.stdout=codecs.open('jsonData2.txt','a', encoding='utf-8') #将打印信息输出在相应的位置下


add = 0
class DmozSpider(CrawlSpider):

    name = "huhu"
    allowed_domains = ["zhaopin.com"]
    start_urls = [
        "http://sou.zhaopin.com/jobs/searchresult.ashx?",
    ]

    
    rules = (
        Rule(SgmlLinkExtractor(allow=("jobs/searchresult.ashx.*sg=.*"))),
        Rule(SgmlLinkExtractor(allow=("http://jobs.zhaopin.com/\d*\.htm?")), callback='parse_item'),
   
    )

    def parse_item(self, response):      
        sel = Selector(response)
        items = []
        item = CnblogItem()
        item['jobName'] = sel.xpath("/html/body/div[5]/div[1]/div[1]/h1/text()").extract()
        item['salary'] = sel.xpath("/html/body/div[6]/div[1]/ul/li[1]/strong/text()").extract()
        item['date'] = sel.xpath("//*[@id='span4freshdate']/text()").extract()
        item['jobYear'] = sel.xpath("/html/body/div[6]/div[1]/ul/li[5]/strong/text()").extract()
        item['number'] = sel.xpath("/html/body/div[6]/div[1]/ul/li[7]/strong/text()").extract()
        item['place'] = sel.xpath("/html/body/div[6]/div[1]/ul/li[2]/strong/a/text()").extract()
        item['jobCluster'] = sel.xpath("/html/body/div[6]/div[1]/ul/li[4]/strong/text()").extract()
        item['edu'] = sel.xpath("/html/body/div[6]/div[1]/ul/li[6]/strong/text()").extract()
        item['jobClass'] = sel.xpath("/html/body/div[6]/div[1]/ul/li[8]/strong/a/text()").extract()
        item['context'] = sel.xpath("/html/body/div[6]/div[1]/div[1]/div/div[1]/p/text()").extract()
        items.append(item)
        return items