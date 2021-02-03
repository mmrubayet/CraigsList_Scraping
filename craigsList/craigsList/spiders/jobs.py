import scrapy


class JobsSpider(scrapy.Spider):
    name = 'jobs'
    # allowed_domains = ['https://newyork.craigslist.org/search/egr']
    # start_urls = ['https://newyork.craigslist.org/search/egr/']
    allowed_domains = ['http://quotes.toscrape.com/']
    start_urls = ['http://quotes.toscrape.com/']

    def parse(self, response):
        # titles = response.xpath('//a[@class="result-title hdrlnk"]/text()').extract()
        qoutes = response.xpath('//span[@class="text"]/text()').extract()
        for qoute in qoutes:
            yield {'Quote': qoute}
        # print(titles)
# the craiglist site blocked my ip. So we are using this for now. We will try later.
# or, we will bypass the blockage using proxy.
