import scrapy


class CelebspiderSpider(scrapy.Spider):
    name = 'celebspider'
    allowed_domains = ['celebrityxyz.com']
    start_urls = ['https://celebrityxyz.com']

    def parse(self, response):
        pass
