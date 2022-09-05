#-*- codeing = utf-8 -*-
#@Time : 2021/10/7 17:49
#@Author :DHD
#@File : main.py
#@Software : PyCharm

"""from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
settings = get_project_settings()
crawler = CrawlerProcess(settings)
crawler.crawl('爬虫名字')
crawler.crawl('爬虫名字2')
crawler.start()
crawler.start()"""

from scrapy.cmdline import execute

execute('scrapy crawl movie'.split())