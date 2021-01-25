from urllib import parse
import scrapy
from scrapy.spiders import CrawlSpider , Rule
from scrapy.linkextractors import LinkExtractor
from news_mk.items import NewsMkItem
from scrapy.loader import ItemLoader

class FirstOfSpider(scrapy.Spider):
    name = 'first_of'
    allowed_domains = ['off.net.mk']
    start_urls = ['http://off.net.mk']
    base_url = "http://off.net.mk"
    
    

    def parse(self, response):
        links = response.xpath('//a/@href').getall()
        for link in links:
            
            absolute_url = self.base_url + link
            #print(absolute_url)
            yield scrapy.Request(absolute_url, callback=self.parse_1)

    def parse_1(self,response):
        
        #news = NewsMkItem()
        # news['title'] = response.selector.xpath('//span/text()').get(),
        # a = response.selector.xpath('//div[@class="objaveno"]/text()').get()
        # print(a)
        #news['url'] = response.url
        l = ItemLoader(item=NewsMkItem(), response=response)
        l.add_xpath('title', '//span/text()')
        l.add_xpath('data', '//div[@class="objaveno"]/text()')
        l.add_value('url', response.url)
        return l.load_item()
        