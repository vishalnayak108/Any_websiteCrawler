# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

from scrapy.exporters import JsonLinesItemExporter

class LinksPipeline(object):
    def open_spider(self, spider):
        self.export_ = []

    def close_spider(self, spider):
        item_p = {"pages": self.export_}
        f = open('output.json', 'wb')
        exporter = JsonLinesItemExporter(f, encoding='utf-8')
        exporter.start_exporting()
        exporter.export_item(item_p)
        exporter.finish_exporting()
        exporter.file.close()

    def process_item(self, item, spider):
        self.export_.append(item)
        return item

