import scrapy

class LinksSpecial(scrapy.Spider):

    name = 'links_special'
    start_urls = ['https://www.mtggoldfish.com/prices/paper/special']

    def parse(self, response):
        link = response.xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "card_name", " " ))]//a//@href').getall()

        for card in range(len(link)):
            yield{
                'link': link[card]
            }




