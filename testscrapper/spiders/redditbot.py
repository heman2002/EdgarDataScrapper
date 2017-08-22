# -*- coding: utf-8 -*-
import scrapy
import pandas

df = pandas.read_excel('/home/himanshu/Downloads/Input.xlsx')
values = df['URL'].values
# print values

class RedditbotSpider(scrapy.Spider):
    name = 'redditbot'
    # allowed_domains = ['www.reddit.com/r/gameofthrones/']
    start_urls = values
    # print start_urls

    def parse(self, response):
        # data = response.css('table::text').extract()
        # print data
        # pass
        tables = response.xpath('//table')
        for index, tr in enumerate(tables.xpath('.//tr')):
            for td in tr.xpath('.//td'):
                for p in td.xpath('.//p//text()').re(r'\bCredit Default Swap\b'):
                    temp = tables.xpath('.//tr//td//p')[index + 1].extract()
                    print temp
                    # scraped_info = {
                    # 'url' : response.url,
                    # 'CDS Text' : temp[1],
                    # 'Expiration Date' : temp[2],
                    # 'Notional Amount' : temp[3],
                    # }
                    # yield scraped_info
