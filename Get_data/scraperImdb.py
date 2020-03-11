from itemCatalogo import ItemCatalogo
import scrapy
import logging
from scrapy.crawler import CrawlerProcess
from scrapy import Selector
import requests


class ImdbSpider(scrapy.Spider):    
    name = 'imdb_spider'
    logging.getLogger('scrapy').propagate = False  # No mostrar log de scrapy
    contador = 0
    totalUrls = 0

    def start_requests(self):
        """
        urls = [
            'https://www.imdb.com/title/tt1502397',
            'https://www.imdb.com/title/tt7975244'
        ]
        """

        urls = ItemCatalogo.urlsImdb()

        self.totalUrls = len(urls)

        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)
    
    def empieza(self):
        process = CrawlerProcess({
            'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)',
            'DOWNLOAD_DELAY': 2,
            'COOKIES_ENABLED': 'False'
        })

        process.crawl(ImdbSpider)
        process.start()

    def parse(self, response):
        self.contador += 1

        print('Obteniendo presupuesto. Iteración:', self.contador, 'de', self.totalUrls)

        res = requests.get(response.url)
        sel = Selector(res)

        # Obtengo el id de IMDb quitando la / del final
        urlAux = str(response.url)

        if urlAux[-1] == '/':
            urlAux = urlAux[:-1]

        idImdb = urlAux[urlAux.rfind('/') + 1:]

        budget = ' '.join(sel.css(".txt-block:contains('Budget')::text").extract()).strip()

        if budget != '' and len(budget) > 0:
            if '$' in budget:
                budget = budget.replace('$', '')

            if '.' in budget:
                budget = budget.replace('.', '')

            if ',' in budget:
                budget = budget.replace(',', '')

            intBudget = int(budget)
            ItemCatalogo.actualizaPresupuestoImdb('Movie', intBudget, idImdb)
            print('PRESUPUESTO:', intBudget, 'IMDb id:', idImdb)
        else:
            print('No encontrado presupuesto:', idImdb)


if __name__ == "__main__":
    aaa = ImdbSpider()
    aaa.empieza()
