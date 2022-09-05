import scrapy
from lxml import etree
from film.items import FilmItem

class MovieSpider(scrapy.Spider):
    name = 'movie'
    allowed_domains = ['movie.douban.com/top250']
    start_urls = ['http://movie.douban.com/top250/']

    def parse(self, response):
        tree=etree.HTML(response.text)
        munbers=tree.xpath('//ol[@class="grid_view"]/li//em')
        dbs=tree.xpath('//ol[@class="grid_view"]/li//img/@alt')
        mianhumbers=tree.xpath('//ol[@class="grid_view"]/li//div[@class="bd"]/p')
        miantitles = tree.xpath('//ol[@class="grid_view"]/li//p[@class="quote"]/span[@class="inq"]')

        for db,munber,mianhumber,miantitle in zip(dbs,munbers,mianhumbers,miantitles):
            item=FilmItem()
            item['name']=db
            item['munber'] = munber.text
            item['mianhumber'] = mianhumber.text
            item['miantitle'] = miantitle.text
            yield item



        # print(response.text)  # 获取字符串类型的响应内容
        # print(response.body)  # 获取字节类型的相应内容
