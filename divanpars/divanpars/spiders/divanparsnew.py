import scrapy


class DivanparsnewSpider(scrapy.Spider):
    name = "divanparsnew"
    allowed_domains = ["https://divan.ru"]
    start_urls = ["https://www.divan.ru/category/krovati"]

    def parse(self, response):
        krovati = response.css('div._Ud0k')
        for krovat in krovati:
            yield {
                'name': krovat.css('div.lsooF span::text').get()
                'price': krovat.css('div.pY3d2 span::text').get()

            }
