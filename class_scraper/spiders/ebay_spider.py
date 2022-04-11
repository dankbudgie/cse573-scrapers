import scrapy
import os
from scrapy.http import Request
import re

class EbaySpider(scrapy.Spider):
    name = 'ebay'
    start_urls = ['https://www.ebay.com/sch/i.html?_from=R40&_nkw=graphics+cards&_sacat=0&LH_TitleDesc=0&_pgn=1']
    max_pages = 1000

    def parse(self, response):
        try:
            for products in response.css('div.s-item__wrapper.clearfix'):
                yield {
                    'name': products.css('h3.s-item__title::text').get(),
                    'price': products.css('span.s-item__price::text').get().replace('$', ''),
                }
        except:
            pass

        if '&_pgn=' not in response.url and self.max_pages>=2:
            yield Request(response.request.url+"&_pgn=2")
        else:
            url = response.request.url
            current_page_no = re.findall('pgn=(\d+)',url)[0]
            next_page_no = int(current_page_no)+1
            url = re.sub('(^.*?&_pgn\=)(\d+)(.*$)',rf"\g<1>{next_page_no}\g<3>",url)
            if next_page_no <= self.max_pages:
                yield Request(url,callback=self.parse)