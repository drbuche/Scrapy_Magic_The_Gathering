![N|Solid](https://i.imgur.com/PvOuhOr.png)

# Scrapy + Power BI = Magic: The Gathering!


Foi realizado a scraping da página de venda de cartas [MTG Gold Fish](https://www.mtggoldfish.com/) com intuito de testar algumas técnicas de coleta, limpeza e apresentação de dados.
- Link: www.encurtador.com.br/bdflE

- Para tal projetos, foram utilizadas as seguintes ferramentas:


- [x] Python
	- [x] Scrapy
	- [x] Pandas
- [x] Microsoft Power BI
- [x] random.randint(0, 99) copos de café 

Dentro deste Dashboard interativo a imaginação é o limite, podemos avaliar cartas tanto em características monetárias quanto em características de poder, dentro de cada arranjo temos diversos filtros, divirta-se!

*Você pode utilizar esse código como base e automatizar tal coleta e conecta-la a um banco de dados, o qual pode alimentar o Dashboard em tempo real! Criando inúmeras novas possibilidades de análise de dados.*


# Utilizando!

- Utilize o comando abaixo para coletar os links:
```sh
scrapy runspider links_NomeDoModulo.py -O links_NomeDoModulo.csv
```

- Utilize o comando abaixo para coletar as cards :
```sh
scrapy runspider cards_NomeDoModulo.py -O cards_NomeDoModulo.csv
```
- Caso esteja com problema com perca de dados durante a coleta (dados : None), entre no modulo default_settings.py, que está na pasta settings do Scrapy, e modifique a velocidade entre as coletas.
```sh
DOWNLOAD_DELAY = 0.90 # tente usar entre 0.25 a 1
``` 

- Unindo os dados coletados e removendo as linhas brancas, em uma única tabela:
```sh
python join_cards.py
``` 

*Não esqueça que os arquivos .csv devem estar na mesma pasta que os módulos, caso contrario mude o caminho do arquivo dentro do modulo.*"# Scrapy_MagicTG_Cards" 
"# Scrapy_MagicTG_Cards" 
"# Scrapy_MagicTG_Cards" 
"# Scrapy_MagicTG_Cards" 
"# Scrapy_MagicTG_Cards" 
"# Scrapy_MagicTG_Cards" 
"# Scrapy_MagicTG_Cards" 
