import scrapy


class WlgnSpider(scrapy.Spider):
    name = 'wlgn'
    allowed_domains = ['hcs.eduro.go.kr']
    start_urls = ['http://hcs.eduro.go.kr/']

    def parse(self, response):
        pass
