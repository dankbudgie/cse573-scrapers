import scrapy

class BestBuySpider(scrapy.Spider):
    name = 'bestbuy'
    start_urls = ['https://www.bestbuy.com/site/laptop-computers/all-laptops/pcmcat138500050001.c?id=pcmcat138500050001']

    def parse(self, response):
        for products in response.css('li.sku-item'):
            yield {
                'name': products.css('div.sku-title::text').get(),
                'price': products.css('div.priceView-hero-price.priceView-customer-price::text').get().replace('$', ''),
            }
        
        next_page = response.css('a.sku-list-page-next').attrib['href']
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)