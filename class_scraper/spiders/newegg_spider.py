from ast import Pass
from distutils.spawn import spawn
import scrapy

class NeweggSpider(scrapy.Spider):
    name = 'newegg'
    start_urls = ['https://www.newegg.com/p/pl?d=computers']

    def parse(self, response):
        for products in response.css('div.item-cell'):
            try:
                intermediate_price = products.css('li.price-current').get().replace('<li class="price-current"><span class="price-current-label"></span>$<strong>', '').replace('</strong><sup>','')
                s_price = intermediate_price.split('<', 1)
            except:
                pass
            finally:
                yield {
                    'name': products.css('a.item-title::text').get(),
                    'price': s_price[0],
                }
        
        next_page = response.css('a.pagination__next.icon-link').attrib['href']
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)