import scrapy
from scrapy.crawler import CrawlerProcess
from QuoteSpider import QuoteSpider

# makes a json file
if __name__ == '__main__':
    process = CrawlerProcess(settings={
        "FEEDS": {
            "items.json": {"format": "json"},
        },
    })

    process.crawl(QuoteSpider)
    process.start() # the script will block here until the crawling is finished



    