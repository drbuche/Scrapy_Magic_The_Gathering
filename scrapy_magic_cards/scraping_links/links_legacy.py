import scrapy

class Cartas_NL(scrapy.Spider):

    name = 'Cartas_legacy'
    start_urls = ['https://www.mtggoldfish.com/prices/paper/legacy_one']

    def parse(self, response):
        link = response.xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "card_name", " " ))]//a//@href').getall()

        for card in range(len(link)):
            yield{
                'link': link[card]
            }

