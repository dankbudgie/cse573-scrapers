import scrapy

class EbaySpider(scrapy.Spider):
    name = 'ebay'
    start_urls = ['https://www.ebay.com/sch/i.html?_nkw=computer&ssPageName=GSTL']

    def parse(self, response):
        for products in response.css('div[data-content="productItem"]'):
            yield {
                'name': products.css('h3.s-item__title::text').get(),
                'price': products.css('span.s-item__price::text').get().replace('$', ''),
            }
        
        next_page = response.css('a.pagination__next.icon-link').attrib['href']
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)