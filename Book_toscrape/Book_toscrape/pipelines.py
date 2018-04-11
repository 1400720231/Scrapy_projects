# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


"""
piplines 这里专门放置处理items的组件，记得去setting.py中激活!!!


"""

from scrapy.exceptions import DropItem
# 格式化价格的pipeline
class PriceConverterPipeline(object):
	exchange_rate = 8.5309
	def process_item(self, item, spider):
   		price = float(item['price'][1:])*self.exchange_rate
   		item['price'] = '￥%.2f'%price
   		return item

# 去重书本名字的pipeline
class DuplicatesPipeline(object):

	def __init__(self):
		self.book_set = set()

	def process_item(self, item, spider):
		name = item['name']
		if name in self.book_set:
			raise DropItem('%s这个书本名字已经存在'%name) # 如果报错DropItem，这一项item数据会被删除不要
		self.book_set.add(name)
		return item 