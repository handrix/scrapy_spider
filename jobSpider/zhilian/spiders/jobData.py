#_*_coding:utf-8_+_
from urlparse import urljoin
import simplejson

from scrapy.http import Request
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.selector import HtmlXPathSelector

from zhilian.items import ZhilianItem

class BookSpider(CrawlSpider):
    name = 'zhilian'
    allowed_domains = ['zhaopin.com']
    start_urls = [
        "http://sou.zhaopin.com/jobs/searchresult.ashx", 
    ]
    rules = (
        Rule(SgmlLinkExtractor(allow=('ff='))),
        Rule(SgmlLinkExtractor(allow=('http://jobs.zhaopin.com/\d*.htm\?ssidkey=.*&ss=.*&ff=.*')), callback="parse_item"),
    )
#        Rule(SgmlLinkExtractor(allow=('http://sou\.zhaopin\.com/jobs/searchresult\.ashx\?jl=.*&sm=\d*&p=\d*'))),

        
    def parse_item(self, response):
            res = HtmlXPathSelector(response)
            item = ZhilianItem()
            context = res.select("//div[@class='tab-inner-cont']/p/text()").extract()
            for con in context:
                item['job'] = con
            yield item
            next_url = res.select("//li[@class='pagesDown-pos']/a/@href").extract
            yield Request(url, callback=self.parse_item)