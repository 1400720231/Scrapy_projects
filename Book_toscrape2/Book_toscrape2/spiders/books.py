# -*- coding: utf-8 -*-
import scrapy
from Book_toscrape2.items import BookItems
from scrapy.linkextractors import LinkExtractor


class BooksSpider(scrapy.Spider):
    name = 'books'
    allowed_domains = ['books.toscrape.com']
    start_urls = ['http://books.toscrape.com/']


    def parse(self, response):
        le = LinkExtractor(restrict_css='article.product_pod h3')  # 提取主页面所有的详情页面
        for link in le.extract_links(response):
            yield scrapy.Request(link.url, callback=self.parse_book)# 找到详情页面返回给parse_book页面处理

        le = LinkExtractor(restrict_css='ul.pager li.next')# 寻找下一页链接
        links = le.extract_links(response)
        if links:
            next_url = links[0].url
        yield scrapy.Request(next_url,callback=self.parse)# 找到下一页链接再回调给self.parse



    def parse_book(self,response):# 此时的response是详情页链接Request后返回的，是详情页面的response
        book = BookItems()# 实例化items
        sel = response.css('div.product_main')
        book['name'] = sel.xpath('./h1/text()').extract_first()# 在匹配name子字段
        book['price'] = sel.css('p.price_color::text').extract_first()# 匹配价格字段
        book['review_rating'] = sel.css('p.star-rating::attr(class)').re_first('star-rating ([A-Za-z]+)')

        sel =response.css('table.table.table-striped')
        book['upc'] = sel.xpath('(.//tr)[1]/td/text()').extract_first()
        book['stock'] = sel.xpath('(.//tr)[last()-1]/td/text()').re_first('\((\d+) available\)')
        book['review_num'] = sel.xpath('(.//tr)[last()]/td/text()').extract_first()
        yield book# yield items回去准备给其他组件用
