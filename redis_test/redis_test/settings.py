# Scrapy settings for redis_test project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'redis_test'

SPIDER_MODULES = ['redis_test.spiders']
NEWSPIDER_MODULE = 'redis_test.spiders'


DOWNLOAD_DELAY=1
# LOG_LEVEL='ERROR'
DOWNLOADER_MIDDLEWARES = {
   'redis_test.middlewares.RedisTestDownloaderMiddleware': 300,
}
ITEM_PIPELINES = {
   'scrapy_redis.pipelines.RedisPipeline': 310,
}


REDIS_HOST = 'localhost'                            # 主机名
REDIS_PORT = 6379                                   # 端口
# REDIS_URL = 'redis://10.20.88.158:6379/0'       # 连接URL（优先于以上配置）
# REDIS_PARAMS  = {}                                  # Redis连接参数             默认：REDIS_PARAMS = {'socket_timeout': 30,'socket_connect_timeout': 30,'retry_on_timeout': True,'encoding': REDIS_ENCODING,}）
# # REDIS_PARAMS['redis_cls'] = 'myproject.RedisClient' # 指定连接Redis的Python模块  默认：redis.StrictRedis
# REDIS_ENCODING = "utf-8"
# # 去重规则对应处理的类
DUPEFILTER_CLASS = 'scrapy_redis.dupefilter.RFPDupeFilter'
# #使用scrapy_redis组件组件的调度器
SCHEDULER = 'scrapy_redis.scheduler.Scheduler'
# # 是否在开始之前清空 调度器和去重记录，True=清空，False=不清空
SCHEDULER_PERSIST = True
# SCHEDULER_QUEUE_CLASS = 'scrapy_redis.queue.SpiderPriorityQueue'



