import scrapy


class DldudSpider(scrapy.Spider):
    name = 'dldud'
    allowed_domains = ['hcs.eduro.go.kr']
    start_urls = ['http://hcs.eduro.go.kr/']

    def parse(self, response):
        pass
