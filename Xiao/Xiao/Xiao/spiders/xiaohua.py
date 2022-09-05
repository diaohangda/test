import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

from Xiao.items import XiaoItem


class XiaohuaSpider(CrawlSpider):
    name = 'xiaohua'
    # allowed_domains = ['www.xxx.com']
    start_urls = ['http://www.xiaohuar.com/daxue/']


    link1=LinkExtractor(restrict_xpaths='//*[@id="wrap"]/div/nav/ul')        #解析连接,allow=r'/[a-zA-z]+/[^\s]*.html'
    link2=LinkExtractor(restrict_xpaths='//*[@id="wrap"]/div/div/div/div/a')
    rules = [
        Rule(link1, callback='parse_item',follow=True),
        Rule(link2, callback='next_item', follow=False),
    ]

    def parse_item(self, response):
        divs=response.xpath('//*[@id="wrap"]/div/div//div/div/a/img/@src').extract()

        for i in range(1,len(divs)):
            item = XiaoItem()
            item['Purl']=divs[i].strip()
            print('Purl_1:'+item['Purl'])
            yield item

    def next_item(self,response):
        divs=response.xpath('//*[@id="wrap"]/div/div/div[1]/div/div[4]/div[1]//p/img/@src').extract()
        for i in range(1,len(divs)):
            item = XiaoItem()
            item['Purl'] =divs[i].strip()
            print('Purl_2:' + item['Purl'])
            yield item
        # for div in divs:
        #     item = XiaoItem()
        #     purl = div.xpath('').extract()
        #     if len(purl):
        #         item['next_name']=purl[0].strip()
        #         print('next_name:' + item['next_name'])
        #     yield item