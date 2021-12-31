import scrapy


class GmarketCategoryAllSpider(scrapy.Spider):
    name = 'gmarket_category_all'

    def start_requests(self):
        yield scrapy.Request(url='http://corners.gmarket.co.kr/Bestsellers', callback=self.parse_main_page)

    def parse_main_page(self, response):
        print('parse_main_page')
        category_links = response.css('#categoryTabG li[class^="group"] a::attr(href)').getall()
        category_names = response.css('#categoryTabG li[class^="group"] a::text').getall()

        for link, name in zip(category_links, category_names):
            print(f'http://corners.gmarket.co.kr{link}, {name}')

