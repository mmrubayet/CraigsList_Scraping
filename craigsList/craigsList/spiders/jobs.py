import scrapy


class JobsSpider(scrapy.Spider):
    name = 'jobs'
    # allowed_domains = ['https://newyork.craigslist.org/search/egr']
    # start_urls = ['https://newyork.craigslist.org/search/egr/']
    allowed_domains = ['http://quotes.toscrape.com/']
    start_urls = ['http://quotes.toscrape.com/']

    def parse(self, response):
        # titles = response.xpath('//a[@class="result-title hdrlnk"]/text()').extract()
        titles = response.xpath('//span[@class="text"]/text()').extract()
        print(titles)
