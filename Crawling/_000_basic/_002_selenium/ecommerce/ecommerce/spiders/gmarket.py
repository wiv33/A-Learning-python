import scrapy

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
    start_urls = ['http://www.gmarket.co.kr/']

    def parse(self, response):

        print(response.text)
        pass
