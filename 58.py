#-*- codeing = utf-8 -*-
#@Time : 2021/9/6 16:49
#@Author :DHD
#@File : 58.py
#@Software : PyCharm

import requests
from lxml import etree

url='https://m.58.com/dg/ershoufang/?reform=pcfront&PGTID=0d000000-0000-0e7a-2101-7d9df2ab4cd1'
headers = {
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
}
page_text=requests.get(url=url,headers=headers).text
print(page_text)

tree=etree.HTML(page_text)
lis_data=tree.xpath('//ul[@class="list"]/li')
for i in lis_data:
    title=i.xpath('.//span[@class="content-title"]/text()')[0].strip()
    desc = i.xpath('.//span[@class="content-desc"]//text()')
    community = i.xpath('.//span[@class="content-desc content-desc-community"]/text()')[0]
    price = i.xpath('.//span[@class="content-price"]/text()')[0]
    unit = i.xpath('.//span[@class="content-unit"]/text()')[0]
    size=desc[1].strip()+desc[2].strip()
    adrring=desc[0].strip()+community
    price_unit=price+unit
    data={
        '标题':title,
        '位置':adrring,
        '大小':size,
        '价格':price_unit
    }
    # print(data)



