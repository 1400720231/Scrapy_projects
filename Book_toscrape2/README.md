---
title: README
tags: scrapy, FilePipeline
grammar_cjkRuby: true
---


----------
2018年04月11日 23时11分27秒
*==**scrapy 爬取http://books.toscrape.com**==*


----------


**爬取字段：**

 1. 书名
 2. 价格
 3. 评价等级
 4. 评价数量
 5. 产品编码
 6. 库存量


----------


**整体逻辑：**

 1. 爬取主页面的书籍详情页面链接。
 2. 寻找主页面有没有下一页链接，有的话重复步骤　1。
 3. 把2中获取到的详情页面的链接给book_parse函数处理获取每个书的需要的字段。
 4. 其中调用了set()集合，做到了书名去重。


**Items代码：**
``` stylus

import scrapy
class BookItems(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    name = scrapy.Field() # 书名
    price = scrapy.Field() # 价格
    review_rating = scrapy.Field() # 评价等级
    review_num = scrapy.Field() #评价数量
    upc = scrapy.Field() # 产品编码
    stock = scrapy.Field()# 库存量

```
