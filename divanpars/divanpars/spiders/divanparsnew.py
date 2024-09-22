import scrapy


class DivanparsnewSpider(scrapy.Spider):
    name = "divanparsnew"
    allowed_domains = ["https://divan.ru"]
    start_urls = ["https://www.divan.ru/category/krovati"]

    def parse(self, response):
        pass
