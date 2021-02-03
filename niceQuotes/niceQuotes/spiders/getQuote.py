import scrapy


class GetquoteSpider(scrapy.Spider):
    name = 'getQuote'
    allowed_domains = ['toscrape.com']
    start_urls = ['http://quotes.toscrape.com/']

    def parse(self, response):
        quotes = response.xpath('//div[@class="quote"]')
        for item in quotes:
            quote = item.xpath('span[@class="text"]/text()').extract_first()
            author = item.xpath('span/small[@class="author"]/text()').extract_first()
            tag = item.xpath('div[@class="tags"]/a/text()').extract()

            yield {'Quote': quote, 'Author': author, 'Tags': tag}

        relative_next_url = response.xpath('//li[@class="next"]/a/@href').extract_first()
        absolute_next_url = response.urljoin(relative_next_url)

        yield scrapy.Request(absolute_next_url, callback=self.parse)
        # print(relative_next_url, absolute_next_url)
