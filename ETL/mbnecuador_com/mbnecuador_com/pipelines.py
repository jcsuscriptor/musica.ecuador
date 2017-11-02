# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


class MbnecuadorComPipeline(object):
    def __init__(self):
        self.ids_seen = set()

    def process_item(self, item, spider):
       
        if item['nombre'] in self.ids_seen:
            #raise DropItem("Duplicate item found: %s" % item)
            item['duplicado'] = 1
            return item
        else:
            self.ids_seen.add(item['nombre'])
            return item

