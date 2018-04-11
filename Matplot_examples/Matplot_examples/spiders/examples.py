# -*- coding: utf-8 -*-
import scrapy
from ..items import ExamplesItem

from scrapy.linkextractors import LinkExtractor

class ExamplesSpider(scrapy.Spider):
    name = 'examples'
    allowed_domains = ['matplotlib.org']
    start_urls = ['http://matplotlib.org/examples/index.html']

    def parse(self, response):
        le = LinkExtractor(restrict_css='div.toctree-wrapper.compound',deny='/index.html$')
        for link in le.extract_links(response):
        	yield scrapy.Request(link.url,callback=self.parse_example)

    def parse_example(self,response):
    	# 获取下载链接
    	href = response.css('a.reference.external::attr(href)').extract_first()
    	# 构建绝对路径，因为这里不是用linkextractors写的
    	url = response.urljoin(href)
    	example = ExamplesItem()
    	example['file_urls'] = [url] # 传入一个列表，可以循环迭代下载
    	yield example
