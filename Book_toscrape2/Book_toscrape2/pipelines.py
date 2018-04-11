# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class BookPipeline(object):

"""
	把review_rating的等级由原来的five英文映射成数字等级5
"""
	review_rating_map = {
	'One': 1,
	'Two': 2,
	'Three': 3,
	'Four': 4,
	'Five': 5
	}

	def process_item(self, item, spider):
		rating = item.get('review_rating')
		# rating = item.get('review_rating')

		if rating:
			item['review_rating'] = self.review_rating_map[rating]
		return item
