# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import scrapy
from scrapy.contrib.pipeline.images import ImagesPipeline,FilesPipeline
from PIL import Image

class AndrewPipeline(ImagesPipeline):

    def set_filename(self, key, response):
        if response.meta['x']==1:
            return "full/Schematics/%s.jpg" % (response.meta['title'])
        else:
            if response.meta['x']>1:
                return "full/Product Images/%s%s.jpg" % (response.meta['title'],response.meta['x']-1)
            else:
                return "full/Product Images/%s.jpg" % (response.meta['title'])

    def get_media_requests(self, item, info):
        x=0
        for image_url in item['image_urls']:
            yield scrapy.Request(image_url, meta={'title': item['title'],'x': x})
            x=x+1

    def get_images(self, response, request, info):
        for key, image, buf in super(AndrewPipeline, self).get_images(response, request, info):
            key = self.set_filename(key, response)
            yield key, image, buf

class AndrewPipeline2(FilesPipeline):

    def set_filename(self, key, response):
        return "full/%s.pdf" % (response.meta['title'])

    def get_media_requests(self, item, info):
        if item['file_urls']!="":
            yield scrapy.Request(item['file_urls'], meta={'title': item['title']})

    def get_images(self, response, request, info):
        for key, image, buf in super(AndrewPipeline, self).get_images(response, request, info):
            key = self.set_filename(key, response)
            yield key, image, buf
