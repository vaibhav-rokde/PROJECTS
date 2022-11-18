import scrapy
from ..items import MyquotesItem

class QuotesSpider(scrapy.Spider):
    name = 'quotes'
    start_urls = ['http://quotes.toscrape.com/']

    def parse(self, response):
        items=MyquotesItem()

        add_quotes=response.css("div.quote")

        for quotes in add_quotes:
            title=quotes.css("span.text::text").extract()
            author=quotes.css(".author::text").extract()
            tag=quotes.css(".tag::text").extract()

            items['title']=title
            items['author']=author
            items['tag']=tag

            yield items

        next_page = response.css("li.next a::attr(href)").get()
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)
