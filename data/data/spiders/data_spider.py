from ..items import DataItem
import scrapy

class data(scrapy.Spider):
    name = 'data'
    start_urls = ['https://quotes.toscrape.com/']

    def parse(self, response):
        all_div_qut = response.css('div.quote')

        for quote in all_div_qut:
            items = DataItem()  # Create a new item for each quote

            text = quote.css('span.text::text').get()
            author = quote.css('small.author::text').get()
            tag = quote.css('div.tags a.tag::text').extract()

            items['title'] = text
            items['author'] = author
            items['tag'] = tag

            yield items

