import scrapy
import csv


class CardsStandard(scrapy.Spider):
    name = 'Cards_standard'
    allowed_domains = ['https://www.mtggoldfish.com/']
    start_urls = []

    start_urls_base_T = []
    file = open("links_standard.csv", "r")
    csv_reader = csv.reader(file)
    for row in csv_reader:
        start_urls_base_T.append(row[0])



    for url in start_urls_base_T:

        start_urls.append(f'https://www.mtggoldfish.com{url}')

    def parse(self, response):
        nome = response.css('.gatherer-name::text').get()
        preco = response.css('.paper .price-box-price::text').get()
        descri = response.css('.gatherer-oracle::text').getall()
        color = response.xpath('body//main//div//div//div//div//h3/span//@aria-label').getall()
        power = response.css('.gatherer-power::text').getall()
        raridade = response.css('.gatherer-rarity::text').getall()
        tipo = response.css('.gatherer-type::text').getall()
        edicao = response.css('.price-card-name-set-name::text').get()
        try:
            var_pre_dia = response.xpath(
                '//*[contains(concat( " ", @class, " " ), concat( " ", "price-card-statistics-table2", " " ))]//tr[(((count(preceding-sibling::*) + 1) = 1) and parent::*)]//*[contains(concat( " ", @class, " " ), concat( " ", "text-right", " " ))]//span/text()')[
                0].getall()
        except:
            var_pre_dia = response.css('.increase::text').get()
        try:
            var_pre_semana = response.xpath(
                '//*[contains(concat( " ", @class, " " ), concat( " ", "price-card-statistics-table2", " " ))]//tr[(((count(preceding-sibling::*) + 1) = 2) and parent::*)]//*[contains(concat( " ", @class, " " ), concat( " ", "text-right", " " ))]//span/text()')[
                0].getall()
        except:
            var_pre_semana = response.css('.decrease::text').get()
        preco_maior = response.css('.price-card-statistics-table2 tr:nth-child(3) .text-right::text').get()
        preco_menor = response.css('.price-card-statistics-table2 tr:nth-child(4) .text-right::text').get()
        taxa_foil = response.css('.price-card-statistics-table:nth-child(1) tr~ tr+ tr .text-right::text').get()
        spread = response.css('.price-card-statistics-table:nth-child(1) tr:nth-child(1) .text-right::text').get()
        imagem = response.xpath('//body//main//div//div//picture//@src').get()


        yield {

            'nome': nome,
            'imagem': imagem,
            'power': power,
            'preco': preco,
            'raridade': raridade,
            'tipo': tipo,
            'edicao': edicao,
            'descricao': descri,
            'color': color,
            'format': 'Standard',
            'variacao_diaria': var_pre_dia,
            'variacao_semana': var_pre_semana,
            'maior_preco': preco_maior,
            'menor_preco': preco_menor,
            'spread': spread,
            'taxa_foil': taxa_foil,

        }

