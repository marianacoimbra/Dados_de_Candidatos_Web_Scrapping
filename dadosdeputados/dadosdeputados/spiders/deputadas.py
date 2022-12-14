import scrapy

from ..Utils import Utils
class DeputadasSpider(scrapy.Spider):
    name = "deputadas"
    
    def start_requests(self):
        deps_file = open("../lista_deputadas.txt", "r")

        deps_urls = deps_file.read().splitlines()

        for url in deps_urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        main_response= Utils(response)

        main_data = main_response.main(gender="F")

        yield main_data