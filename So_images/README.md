---
title: 360图片下载
tags: scrapy, ImagesPipeline
grammar_cjkRuby: true
---


----------


**scrapy爬取360图片网站的图片下载到本地**


----------


==强调3点：==

 1. ImagesPipeline
 2. ROBOTTXT_OBEY = False
 3. IMAGES_STORE = 'downloads' 


----------


1、　是图片pipeline组件
2、　ROBOTTXT_OBEY = False表示不遵守机器人协议，因为这个网址禁止访问了
3、　IMAGES_STORE = 'downloads'  # 下载保存路径
