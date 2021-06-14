import scrapy

class QuoteSpider(scrapy.Spider):
    name = 'quotes'
    start_urls = [
        'https://quotes.toscrape.com/'
    ]

    def parse(self, response):
        # response contains all the source code of the url

        title = response.css('title::text').extract() # get title
        yield {'title': title} # scrapy should use yield instead of return