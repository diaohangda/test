#-*- codeing = utf-8 -*-
#@Time : 2021/9/8 12:04
#@Author :DHD
#@File : 4K.py
#@Software : PyCharm

import os
import requests
from lxml import etree

headers = {
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
}
if not os.path.exists('4k图片'):  # 创建文件夹
    os.mkdir('4k图片')

def tupian(url):
    res=requests.get(url=url,headers=headers).content
    # res_text=res.text
    return res

if __name__ == '__main__':
    url='https://pic.netbian.com/4kmeinv/'
    response=requests.get(url=url,headers=headers)
    response_text=response.text

    tree=etree.HTML(response_text)
    p=tree.xpath('//ul[@class="clearfix"]/li/a/img/@src')
    # print(p)
    di=0
    for i in p:
        tu_url='https://pic.netbian.com'+i
        dun=tupian(tu_url)
        di+=1

        # with open('4k图片/' + str(di)+'.jps', 'w', encoding='utf-8') as f:
        #     f.write(dun)
    #'https://pic.netbian.com'