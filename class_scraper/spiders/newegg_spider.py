from ast import Pass
from distutils.spawn import spawn
import scrapy
import os
from scrapy.http import Request
import re
from selectorlib import Extractor

class NeweggSpider(scrapy.Spider):
    name = 'newegg'
    start_urls = ['https://www.newegg.com/p/pl?d=computers&page=1']
    max_pages = 5

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
        
        if '&page=' not in response.url and self.max_pages>=2:
            yield Request(response.request.url+"&page=2")
        else:
            url = response.request.url
            current_page_no = re.findall('page=(\d+)',url)[0]
            next_page_no = int(current_page_no)+1
            url = re.sub('(^.*?&page\=)(\d+)(.*$)',rf"\g<1>{next_page_no}\g<3>",url)
            if next_page_no <= self.max_pages:
                yield Request(url,callback=self.parse)