# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class EcommerceItem(scrapy.Item):
    # define the fields for your item here like:
    main_category_name = scrapy.Field()
    sub_category_name = scrapy.Field()
    ranking = scrapy.Field()
    title = scrapy.Field()
    ori_price = scrapy.Field()
    dis_price = scrapy.Field()
    discount_percent = scrapy.Field()
