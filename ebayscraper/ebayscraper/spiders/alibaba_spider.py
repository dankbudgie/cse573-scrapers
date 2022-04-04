import scrapy

class AlibabaSpider(scrapy.Spider):
    name = 'alibaba'
    start_urls = ['https://www.alibaba.com/trade/search?fsb=y&IndexArea=product_en&CatId=&SearchText=computer&viewtype=&tab=']
    
    def parse(self, response):
        for products in response.css('div.list-no-v2-inner.m-gallery-product-item-v2.img-switcher-parent'):
            yield {
                'name': products.css('p.elements-title-normal__content.large::text').get(),
                'price': products.css('span.elements-offer-price-normal__promotion::text').get().replace('$', ''),
            }
        
        # logic to handle next page
        # next_page = response.css('a.seb-pagination__pages-link').attrib['href']
        # if next_page is not None:
        #     yield response.follow(next_page, callback=self.parse)