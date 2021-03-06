import scrapy

class LinksStandard(scrapy.Spider):

    name = 'links_standard'
    start_urls = ['https://www.mtggoldfish.com/index/ZNR_MID#online']

    def parse(self, response):
        link = response.xpath('//*[contains(concat( " ", @class, " " ), concat( " ", "card_name", " " ))]//a//@href').getall()

        for card in range(len(link)):
            yield{
                'link': link[card]
            }