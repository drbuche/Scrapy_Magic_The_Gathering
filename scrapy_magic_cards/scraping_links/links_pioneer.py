import scrapy

class Cartas_NL(scrapy.Spider):

    name = 'Cartas_pioneer'
    start_urls = ['https://www.mtggoldfish.com/index/pioneer#online']

    def parse(self, response):
        link = response.xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "card_name", " " ))]//a//@href').getall()

        for card in range(len(link)):
            yield{
                'link': link[card]
            }