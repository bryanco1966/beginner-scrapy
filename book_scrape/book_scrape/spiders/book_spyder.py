import scrapy
from book_scrape.items import BookScrapeItem

class BooksSpider(scrapy.Spider):
    name = 'books'
    start_urls = [

        'http://books.toscrape.com/'
    ]

    #scraping the entire page
    # def parse(self, response):
    #     page = response.url.split('/')[-2]
    #     filename = 'books-%s.html' % page
    #     with open(filename, 'wb') as f:
    #         f.write(response.body)
    def parse(self, response):
        item = BookScrapeItem()
        item['title']= response.xpath('//*/h3/a/text()').extract()
        item['price']= response.xpath('//p[@class="price_color"]/text()').extract()

        return item
