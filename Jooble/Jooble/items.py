# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy
"""
 # 为实例化后的对象填充值
        article_item["url_object_id"] = get_md5(response.url)
        article_item["title"] = title
        article_item["url"] = response.url
        try:
            create_date = datetime.datetime.strptime(create_date, "%Y/%m/%d").date()
        except Exception as e:
            create_date = datetime.datetime.now().date()
        article_item["create_date"] = create_date
        article_item["front_image_url"] = [front_image_url]
        article_item["praise_nums"] = praise_nums
        article_item["comment_nums"] = comment_nums
        article_item["fav_nums"] = fav_nums
        article_item["tags"] = tags
        article_item["content"] = content


"""
class JobBoleArticleItem(scrapy.Item):
    title = scrapy.Field()  #标题
    create_date = scrapy.Field()# 发表日期
    front_image_url = scrapy.Field() # 封面图链接地址
    url = scrapy.Field()  # 链接
    url_object_id = scrapy.Field()  #url_id http://blog.jobbole.com/113817/ 113817则为其id
    praise_nums = scrapy.Field(   )  # 点赞数
    comment_nums = scrapy.Field()  # 评论书
    fav_nums =scrapy.Field()  # 收藏数
    tags = scrapy.Field() # 标签
    content = scrapy.Field() # 评论
    
 