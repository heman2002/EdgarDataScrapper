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
            for td in tr.xpath('.//td//p//text()').re(r'\bCredit Default Swap\b|\bCDS\b|\bCredit Swap\b|\bCredit Default Swaps\b'):
                temptr = tables.xpath('.//tr')[index + 1]
                temptd = temptr.xpath('.//td//p//text()').extract()
                temptd = list(filter(lambda x: x != '\n', temptd))
                temptd = map(lambda each:each.replace('\t', ''), temptd)
                scraped_info = {
                'url' : response.url,
                'CDS Text' : temptd[0],
                'Expiration Date' : temptd[1],
                'Notional Amount' : temptd[2],
                'Unrealised Appreciation' : temptd[3]
                }
                yield scraped_info

# df1 = pandas.read_csv('/home/himanshu/testscrapper/reddit.csv')
# df1.merge(df, left_on='url', right_on='URL')
