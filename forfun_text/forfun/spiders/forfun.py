#_*_coding:utf-8_*_
from bs4 import BeautifulSoup
from scrapy import Request
from scrapy.contrib.spiders import CrawlSpider, Rule
from  scrapy.contrib.linkextractors import LinkExtractor

class Forfun(CrawlSpider):
	"""docstring for Forfun"""
	name = "forfun"
	allowed_domains = ["111.com"]
	start_urls = ['http://www.111.com.cn/']

	rules = (
		Rule(LinkExtractor(allow=(r"1+\..+")), callback= 'parse', follow=True),
	)
	def parse(self, response):
		items = []
		bs = BeautifulSoup(response)
		for link in bs.find_all('a'):
			item = ForfunItem()
			if link.get('href') != Null and link.text != Null:
				try:
					item['url'] = link.get('href')
					item['url_title'] = link.text
				except:
					pass
				items.append(item)
		return items
