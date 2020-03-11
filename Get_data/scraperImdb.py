import scrapy
import logging
from scrapy.crawler import CrawlerProcess
from scrapy import Selector
import requests
from itemCatalogo import ItemCatalogo


class ImdbSpider(scrapy.Spider):
    name = 'imdb_spider'
    logging.getLogger('scrapy').propagate = False  # No mostrar log de scrapy

    def start_requests(self):
        """
        urls = [
            'https://www.imdb.com/title/tt1502397',
            'https://www.imdb.com/title/tt7975244'
        ]
        """

        urls = ItemCatalogo.urlsImdb()

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
        res = requests.get(response.url)
        sel = Selector(res)
        budget = ' '.join(sel.css(".txt-block:contains('Budget')::text").extract()).strip()
        
        if budget and len(budget) > 0:
            if '$' in budget:
                budget = budget.replace('$', '')

            if '.' in budget:
                budget = budget.replace('.', '')

            if ',' in budget:
                budget = budget.replace(',', '')

        intBudget = int(budget)

        print(intBudget)

        # for result in response.css("div.txt-block h4.inline::text"):
            # print(result.extract())


if __name__ == "__main__":
    aaa = ImdbSpider()
    aaa.empieza()
