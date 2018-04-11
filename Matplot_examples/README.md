---
title: 2018-4-12爬取python文件源码
tags: scrapy, matplot.org源码文件

---


==**对http://matplotlib.org/examples/index.html源码本地下载**==

**重点地方：重构文件名返回函数**
**==pipelines.py文件下：==**
``` stylus

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
```
**结果：**
![enter description here](./images/选区_030.png)