import scrapy
import os
from scrapy.http import Request
import re
from selectorlib import Extractor

class AlibabaSpider(scrapy.Spider):
    name = 'alibaba'
    start_urls = ['https://www.alibaba.com/trade/search?spm=a2700.galleryofferlist.0.0.46f6789aOUc0dP&IndexArea=product_en&SearchText=computer&page=1&f0=y']
    extractor = Extractor.from_yaml_file(os.path.join(os.path.dirname(__file__), "../resources/Alibaba.yml"))
    max_pages = 5
    
    def parse(self, response):
        data = self.extractor.extract(response.text,base_url=response.url)
        if data['Products']:
            for product in data['Products']:
                yield product


        # Try paginating if there is data
        if data['Products']:
            if '&page=' not in response.url and self.max_pages>=2:
                yield Request(response.request.url+"&page=2")
            else:
                url = response.request.url
                current_page_no = re.findall('page=(\d+)',url)[0]
                next_page_no = int(current_page_no)+1
                url = re.sub('(^.*?&page\=)(\d+)(.*$)',rf"\g<1>{next_page_no}\g<3>",url)
                if next_page_no <= self.max_pages:
                    yield Request(url,callback=self.parse)

        # for products in response.css('div.list-no-v2-inner.m-gallery-product-item-v2.img-switcher-parent'):
        #     print(products.css)
        #     yield {
        #         'name': products.css('p.elements-title-normal__content.large::text').get(),
        #         'price': products.css('span.elements-offer-price-normal__promotion::text').get(),
        #     }
        
        # logic to handle next page
        # next_page = response.css('a.seb-pagination__pages-link').attrib['href']
        # if next_page is not None:
        #     yield response.follow(next_page, callback=self.parse)