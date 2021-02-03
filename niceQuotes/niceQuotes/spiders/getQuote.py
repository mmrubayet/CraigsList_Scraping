import scrapy


class GetquoteSpider(scrapy.Spider):
    name = 'getQuote'
    allowed_domains = ['http://quotes.toscrape.com/']
    start_urls = ['http://http://quotes.toscrape.com//']

    def parse(self, response):
        pass
