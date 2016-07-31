# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
list1 = open("1.csv").readlines()

class AndrewItem(scrapy.Item):

    title = scrapy.Field()
    image_urls = scrapy.Field()
    images = scrapy.Field()
    file_urls = scrapy.Field()
    files = scrapy.Field()
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass
