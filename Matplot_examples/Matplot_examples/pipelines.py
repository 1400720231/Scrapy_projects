# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

from scrapy.pipelines.files import FilesPipeline
from urllib.parse import urlparse
from os.path import basename,dirname,join


class MyFilesPipelines(FilesPipeline):
	# 重构FilesPipeline中的返回文件储存名字的方法
	def file_path(self,request,response=None,info=None):
		path = urlparse(request.url).path # 获取大概这样的路径example/a.py
		return join(basename(dirname(path)),basename(path))

"""
	假设path = example/a.py
	basename(path) = a.py
	dirname(path) = example
	basename(dirname(path)) = example
	join() = example/a.py


"""