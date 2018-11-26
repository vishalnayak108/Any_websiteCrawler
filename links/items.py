# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy

def serial_item(value):
    return value.decode('utf-8')

class LinksItem(scrapy.Item):
    
    page = scrapy.Field(serializer=serial_item)
    content = scrapy.Field(serializer=serial_item)
