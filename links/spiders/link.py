# -*- coding: utf-8 -*-
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from links.items import LinksItem

class LinkSpider(CrawlSpider):
    name = "link"
    custom_settings = {
        'LOG_FILE': 'output.log',
    }
    def __normalise(self, value):
		# Convert list to string
	    value = value if type(value) is not list else ' '.join(value)
		# Trim leading and trailing special characters (Whitespaces, newlines, spaces, tabs, carriage returns)
	    value = " ".join(value.split())
	    return value 
    
    def __init__(self, domain='', *args, **kwargs):
        super(LinkSpider, self).__init__(*args, **kwargs)
        self.start_urls = [domain]

    rules = (Rule(LinkExtractor(), callback='parse_page', follow=True),)

    def parse_page(self, response):
        self.logger.info('Parse function called on %s', response.url)
        item = LinksItem()
        item['page'] = response.url
        item['content'] = response.xpath('//p/text()').extract()
        #remove white space, newline character, tab character etc.
        item['content']= self.__normalise(item['content'])
        
        yield item
