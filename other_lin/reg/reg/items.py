# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.item import Item, Field

class RegItem(scrapy.Item):
    id_     = scrapy.Field()
    ico     = scrapy.Field()
    nazovUJ = scrapy.Field()
    idUctovnychZavierok    = scrapy.Field()
