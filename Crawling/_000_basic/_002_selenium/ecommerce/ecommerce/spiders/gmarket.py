import scrapy
import re

from ecommerce.items import EcommerceItem

"""
command
scrapy startproject ecommerce
cd ecommerce
scrapy genspider gmarket www.gmarket.co.kr
scrapy crawl gmarket
"""


class GmarketSpider(scrapy.Spider):
    name = 'gmarket'
    allowed_domains = ['www.gmarket.co.kr']
    start_urls = ['http://corners.gmarket.co.kr/Bestsellers/']

    def parse(self, response):
        titles = response.css('div.best-list li > a::text').getall()
        prices = response.css('div.best-list ul li div.item_price div.s-price strong span::text').getall()

        for num, title in enumerate(titles):
            doc = EcommerceItem()
            doc['title'] = title
            doc['price'] = re.sub('[원, ]', '', prices[num])
            yield doc
        self.log('end')
