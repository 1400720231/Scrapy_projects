# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import MySQLdb
from twisted.enterprise import adbapi
# 获取文章链接id插件
class JooblePipeline(object):
    def process_item(self, item, spider):
        item['url_object_id'] = item['url_object_id'].split('/')[-2]
        return item


class MySQLPipeline(object):
    def open_spider(self,spider):
        db = spider.settings.get('MYSQL_DB_NAME','spider')
        host = spider.settings.get('MYSQL_HOST','127.0.0.1')
        port = spider.settings.get('MYSQL_PORT',3306)
        user = spider.settings.get('MYSQL_USER','root')
        passwd = spider.settings.get('MYSQL_PASSWORD','root')

        self.dbpool = adbapi.ConnectionPool('MySQLdb',host=host,port=port,db=db,user=user,passwd=passwd,charset='utf8')
       
    def close_spider(self,spider):
        self.dbpool.close()


    def process_item(self,item,spider):
        self.dbpool.runInteraction(self.insert_db,item)
        return item


    def insert_db(self,tx,item):
        values = (item['title'],item['create_date'],item['front_image_url'],item['url'],item['url_object_id'],item['praise_nums'],item['comment_nums'],item['fav_nums'],item['tags'],item['content'])
        # django数据库中的表名字，打算直接写进去
        sql = 'INSERT INTO search_jobbolearticle(title,create_date,front_image_url,url,url_object_id,praise_nums,comment_nums,fav_nums,tags,content) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
        tx.execute(sql,values)


"""
# 把爬到的数据直接写见数据库，准备和django做后台交互，动态显示
class MySQLPipeline(object):
    def open_spider(self,spider):
        db = spider.settings.get('MYSQL_DB_NAME','xy')
        host = spider.settings.get('MYSQL_HOST','127.0.0.1')
        port = spider.settings.get('MYSQL_PORT',3306)
        user = spider.settings.get('MYSQL_USER','root')
        passwd = spider.settings.get('MYSQL_PASSWORD','root')

        self.db_conn = MySQLdb.connect(host=host,port=port,db=db,user=user,passwd=passwd,charset='utf8')
        self.db_cur = self.db_conn.cursor()  # 创建数据库游标

    def close_spider(self,spider):
        self.db_conn.commit()
        self.db_conn.close()


    def process_item(self,item,spider):
        self.insert_db(item)
        return item


    def insert_db(self,item):
        values = (item['title'],item['create_date'],item['front_image_url'],item['url'],item['url_object_id'],item['praise_nums'],item['comment_nums'],item['fav_nums'],item['tags'],item['content'])
        # django数据库中的表名字，打算直接写进去
        sql = 'INSERT INTO search_jobbolearticle(title,create_date,front_image_url,url,url_object_id,praise_nums,comment_nums,fav_nums,tags,content) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
        self.db_cur.execute(sql,values)

"""
# title = scrapy.Field()  #标题
#     create_date = scrapy.Field()# 发表日期
#     front_image_url = scrapy.Field() # 封面图链接地址
#     url = scrapy.Field()  # 链接
#     url_object_id = scrapy.Field()  #url_id http://blog.jobbole.com/113817/ 113817则为其id
#     praise_nums = scrapy.Field(   )  # 点赞数
#     comment_nums = scrapy.Field()  # 评论书
#     fav_nums =scrapy.Field()  # 收藏数
#     tags = scrapy.Field() # 标签
#     content = scrapy.Field() # 评论
#     