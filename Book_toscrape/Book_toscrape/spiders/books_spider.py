# coding:utf-8
import scrapy
from ..items import BookItems


class BooksSpider(scrapy.Spider):
	name = 'books'
	start_urls = ['http://books.toscrape.com/']

	def parse(self,response):

		for sel in response.css('article.product_pod'):
			book = BookItems()  # 调用items实例化，然后再返回
			book['name'] = sel.xpath('./h3/a/@title').extract_first()
			book['price'] = sel.css('p.price_color::text').extract_first()

			yield book
		next_url = response.css('ul.pager li.next a::attr(href)').extract_first()
		if next_url:
			next_url = response.urljoin(next_url)

			yield scrapy.Request(next_url, callback=self.parse)