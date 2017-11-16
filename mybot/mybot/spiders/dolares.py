# -*- coding: utf-8 -*-
import scrapy
from mybot.items import PersonItem

class DolarSpider(scrapy.Spider):
    name = "dolares"
    #allowed_domains = ["http://www.bcb.gov.br"]
    start_urls = (
        'https://ptax.bcb.gov.br/ptax_internet/consultarUltimaCotacaoDolar.do',
    )

    def parse(self, response):
        dados = response.xpath('//td/text()')
        data = dados[0].extract()
        compra = dados[1].extract()
        venda = dados[2].extract()
        self.log(dados)
        p = PersonItem()
        p['data'] = data
        p['compra'] = compra
        p.save()
        #return PersonItem(p['data'] = data)