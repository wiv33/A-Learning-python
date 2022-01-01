import re

import scrapy
from ecommerce.items import EcommerceItem


class GmarketCategoryAllSpider(scrapy.Spider):
    """
    command
    scrapy crawl gmarket_category_all
    scrapy crawl gmarket_category_all -o gmarket_category_all.csv -t csv
    scrapy crawl gmarket_category_all -o gmarket_category_all.json -t json
    """
    name = 'gmarket_category_all'

    def start_requests(self):
        yield scrapy.Request(url='http://corners.gmarket.co.kr/Bestsellers', callback=self.parse_main_page)

    def parse_main_page(self, response):
        print('parse_main_page')
        category_links = response.css('#categoryTabG li[class^="group"] a::attr(href)').getall()
        category_names = response.css('#categoryTabG li[class^="group"] a::text').getall()

        # 1st category crawling
        for link, name in zip(category_links, category_names):
            # print(f'http://corners.gmarket.co.kr{link}, {name}')
            yield scrapy.Request(url=f'http://corners.gmarket.co.kr{link}',
                                 callback=self.parse_items,
                                 meta={'main_category_name': name, 'sub_category_name': 'ALL'})

        # 2st category crawling
        for link, name in zip(category_links, category_names):
            # print(f'http://corners.gmarket.co.kr{link}, {name}')
            yield scrapy.Request(url=f'http://corners.gmarket.co.kr{link}',
                                 callback=self.parse_sub_category,
                                 meta={'main_category_name': name})

    def parse_sub_category(self, response):
        print('parse_sub_category', response.meta['main_category_name'], response.meta['sub_category_name'])
        category_links = response.css('div.navi.group ul > li > a::attr(href)').getall()
        category_names = response.css('div.navi.group ul > li > a::text').getall()

        for link, name in zip(category_links, category_names):
            # print(f'http://corners.gmarket.co.kr{link}, {name}')
            yield scrapy.Request(url=f'http://corners.gmarket.co.kr{link}',
                                 callback=self.parse_items,
                                 meta={'main_category_name': response.meta['main_category_name'],
                                       'sub_category_name': name}, )

    def parse_items(self, response):
        print('parse_main_category', response.meta['main_category_name'], response.meta['sub_category_name'])
        best_items = response.css('div.best-list')
        for i, el in enumerate(best_items[1].css('li'), 1):
            doc = EcommerceItem()

            title = el.css('a.itemname::text').get()  # title
            ori_price = el.css('div.o-price::text').get()  # 원 가격
            dis_price = el.css('div.s-price strong span span::text').get()
            discount_percent = el.css('div.s-price em::text').get()
            if ori_price is None:
                ori_price = dis_price
            ori_price = re.sub('[원,]', '', str(ori_price))
            dis_price = re.sub('[원,]', '', str(dis_price))

            if discount_percent is None:
                discount_percent = '0'
            else:
                discount_percent = discount_percent.replace('%', '')

            # print(i, title, ori_price, dis_price, discount_percent)
            doc['main_category_name'] = response.meta['main_category_name']
            doc['sub_category_name'] = response.meta['sub_category_name']
            doc['ranking'] = i
            doc['title'] = title
            doc['ori_price'] = ori_price
            doc['dis_price'] = dis_price
            doc['discount_percent'] = discount_percent
            yield doc

