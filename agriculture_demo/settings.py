# -*- coding: utf-8 -*-
import os

# Scrapy settings for agriculture_project project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'agriculture_project'

SPIDER_MODULES = ['agriculture_demo.spiders']
NEWSPIDER_MODULE = 'agriculture_demo.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
# USER_AGENT = 'agriculture_project (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False
HTTPERROR_ALLOWED_CODES = [301]
# Configure maximum concurrent requests performed by Scrapy (default: 16)
# CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://doc.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
# DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
# CONCURRENT_REQUESTS_PER_DOMAIN = 16
# CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
# COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
# TELNETCONSOLE_ENABLED = False

# Override the default request headers:
# DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
# }

# Enable or disable spider middlewares
# See https://doc.scrapy.org/en/latest/topics/spider-middleware.html
SPIDER_MIDDLEWARES = {
    'agriculture_demo.middlewares.AgricultureDemoSpiderMiddleware': 543,
}

# Enable or disable downloader middlewares
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
    'agriculture_demo.middlewares.AgricultureDemoDownloaderMiddleware': 543,
    'agriculture_demo.middlewares.my_useragent_middleware': 544,
}
# 配置保存本地的地址
project_dir = os.path.abspath(os.path.dirname(__file__))  # 获取当前爬虫项目的绝对路径
IMAGES_STORE = os.path.join(project_dir, "images")  # 组装新的图片路径
IMAGES_EXPIRES = 90  # 90天内抓取的都不会被重抓

# Enable or disable extensions
# See https://doc.scrapy.org/en/latest/topics/extensions.html
# EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
# }

# Configure item pipelines
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
    # 'agriculture_demo.pipelines.AgricultureDemoPipeline': 300,
    'agriculture_demo.pipelines.MofcomPipeline': 301,
    'agriculture_demo.pipelines.NatescPipeline': 302,
    'agriculture_demo.pipelines.ImagePipeline': 303,
    'agriculture_demo.pipelines.NmcPipeline': 304,
    'agriculture_demo.pipelines.PrecipitationPipeline': 305,
    'agriculture_demo.pipelines.CfvinPipeline': 306,
    'agriculture_demo.pipelines.AppleZhengzhouPipeline': 307,
    'agriculture_demo.pipelines.AppleAgronetPipeline': 308,
    # 'agriculture_demo.pipelines.DiseasesOrPestsPipeline': 309,

}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/autothrottle.html
# AUTOTHROTTLE_ENABLED = True
# The initial download delay
# AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
# AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
# AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
# AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
# HTTPCACHE_ENABLED = True
# HTTPCACHE_EXPIRATION_SECS = 0
# HTTPCACHE_DIR = 'httpcache'
# HTTPCACHE_IGNORE_HTTP_CODES = []
# HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'

mongo_host = '127.0.0.1'
mongo_port = 27017
mongo_db_name = 'agriculture_demo'
user = 'agri_demo_user'
password = '123456'
