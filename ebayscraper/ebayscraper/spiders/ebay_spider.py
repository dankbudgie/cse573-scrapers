import scrapy


class EbaySpider(scrapy.Spider):
    name = 'ebay'
    start_urls = ['https://www.ebay.com/sch/i.html?_from=R40&_trksid=p2334524.m570.l1313&_nkw=graphics+cards&_sacat=0&LH_TitleDesc=0&_odkw=graphics+card&_osacat=0']

    def parse(self, response):
        for products in response.css('div.s-item__wrapper.clearfix'):
            yield {
                'name': products.css('h3.s-item__title::text').get(),
                'price': products.css('span.s-item__price::text').get().replace('$', ''),
            }
        
        next_page = response.css('a.pagination__next.icon-link').attrib['href']
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)