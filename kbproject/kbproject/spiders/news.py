# -*- coding: utf-8 -*-
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

from kbproject.items import Headline


class NewsSpider(CrawlSpider):
    name = 'news'
    allowed_domains = ['news.yahoo.co.jp', 'headlines.yahoo.co.jp']
    #start_urls = ['https://news.yahoo.co.jp/']
    start_urls = ['https://news.yahoo.co.jp/search/?p=阿部寛&ei=utf-8&fr=news_sw']

    rules = (
        #Rule(LinkExtractor(allow=r'/pickup/\d+$'), callback='parse_topics'),
        Rule(LinkExtractor(allow=r'/article.+$'), callback='parse_topics'),
    )
    """
    def parse(self, response):
        #for url in response.css('ul.topics a::attr("href")').re(r'/pickup/¥d+$'):
        for url in response.css('ul.toptopics_list a::attr("href")').re(r'/pickup/\d+$'):
            yield scrapy.Request(response.urljoin(url), self.parse_topics)
    """
    
    def parse_topics(self, response):
        item = Headline()
        #item['title'] = response.css('.newsTitle ::text').extract_first()
        #item['body'] = response.css('.hbody').xpath('string()').extract_first()
        item['title'] = response.css('.hd').xpath('string()').extract_first()
        item['body'] = response.css('.ynDetailText.yjDirectSLinkTarget').xpath('string()').extract_first()
        
        yield item
