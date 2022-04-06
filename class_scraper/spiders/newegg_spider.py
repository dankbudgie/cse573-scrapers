import scrapy

class NeweggSpider(scrapy.Spider):
    name = 'newegg'
    start_urls = ['https://www.newegg.com/p/pl?d=computers']

    def parse(self, response):
        for products in response.css('div.item-cell'):
            yield {
                'name': products.css('a.item-title::text').get(),
                'price': products.xpath('div[2]/ul/li[3]/strong').get(),
            }
        
        next_page = response.css('a.pagination__next.icon-link').attrib['href']
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)