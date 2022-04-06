import scrapy

class EbaySpider(scrapy.Spider):
    name = 'ebay'
    start_urls = ['https://www.ebay.com/sch/i.html?_from=R40&_trksid=p2334524.m570.l1313&_nkw=graphics+cards&_sacat=0&LH_TitleDesc=0&rt=nc&_odkw=computer&ssPageName=GSTL']

    def parse(self, response):
        try:
            for products in response.css('div.s-item__wrapper.clearfix'):
                yield {
                    'name': products.css('h3.s-item__title::text').get(),
                    'price': products.css('span.s-item__price::text').get().replace('$', ''),
                }
        except:
            pass
        
        next_page = response.css('a.pagination__next.icon-link').attrib['href']
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)