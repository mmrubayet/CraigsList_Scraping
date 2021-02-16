import scrapy


class CelebspiderSpider(scrapy.Spider):
    name = 'celebspider'
    allowed_domains = ['celebrityxyz.com']
    start_urls = ['https://celebrityxyz.com']

    def parse(self, response):
        for category in response.css('div#indexmenu'):
             yield { 'cat': category.css('li a::attr(href)').re(r'/list/profession/\s*(.*)')
             }
            # print(category)
