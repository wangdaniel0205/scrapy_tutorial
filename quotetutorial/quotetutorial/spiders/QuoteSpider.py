import scrapy

# How to export:::     A:\files\scrapy_tutorial\quotetutorial>scrapy crawl quotes -o item.json(or .csv)

class QuoteSpider(scrapy.Spider):
    name = 'quotes'
    start_urls = [
        'https://quotes.toscrape.com/'
    ]

    def parse(self, response):
        '''
        # response contains all the source code of the url
        title = response.css('title::text').extract() # get title
        #yield {'title': title} # scrapy should use yield instead of return

        # target element example: <span class="text" itemprop="text"> ... </span>
        quotes = response.css('span.text::text').extract() 
        # OR: response.xpath("//span[@class='text']/text()").extract()
        yield {'title':title, 'quotes': quotes}
        '''
        title = response.css('title::text').extract() # get title
        all_div_quotes = response.css('div.quote')

        for quote in all_div_quotes:
            quotes = quote.css('span.text::text').extract()
            authors = quote.css('.author::text').extract()
            tags = quote.css('.tag::text').extract()
            yield {
                'quotes': quotes,
                'author': authors,
                'tags': tags
            }