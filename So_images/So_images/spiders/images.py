# -*- coding: utf-8 -*-
import scrapy
from scrapy import Request
import json

class ImagesSpider(scrapy.Spider):
    BASE_URL = 'http://image.so.com/zj?ch=art&sn=%s&listtype=new&temp=1'
    start_index = 0
    # 限制最大下载数量，不能一直下载是不是
    MAX_DOWNLOAD_NUM = 1000#1000张图片
    name = 'images' 
    allowed_domains = ['image.so.com']
    start_urls = [BASE_URL % 0]  # 字符串格式化。。。

    def parse(self, response):
        # 字典
        infos = json.loads(response.body.decode('utf-8'))

        # 提取所有图片下载url到一个列表，赋值给item的image_urls字段
        yield {'image_urls':[info['qhimg_url'] for info in infos['list']]}
        
        # 若果count 字段大于０，并且下载数量不足最大下载数量，就继续获取下一页图片信息

        self.start_index += infos['count']

        # 返回的json字符串中的count字段不为0,而且已经下载的数量下于最大下载数，就继续下载下一页
        if infos['count'] > 0 and self.start_index < self.MAX_DOWNLOAD_NUM:
            # url的sn= 30 60 90 这样一直累加的
            yield Request(url=self.BASE_URL % self.start_index,callback=self.parse)


"""

遇到一个报错说robot.txt错误
把setting.py下面的ROBOTSTXT_OBEY改为Ｆalse即可,
意思是不遵守爬虫协议
ROBOTSTXT_OBEY = False 


图片我只保留了几张，剩下的900多张我删除了。。
"""