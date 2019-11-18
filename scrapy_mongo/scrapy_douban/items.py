# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ScrapyDoubanItem(scrapy.Item):
    # define the fields for your item here like:
    moviename = scrapy.Field()
    info = scrapy.Field()
    year = scrapy.Field()
    stars = scrapy.Field()
    synopsis = scrapy.Field()
