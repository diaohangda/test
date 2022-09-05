#-*- codeing = utf-8 -*-
#@Time : 2021/9/6 18:06
#@Author :DHD
#@File : 三国.py
#@Software : PyCharm
#coding=utf-8

import requests
from bs4 import BeautifulSoup
import time

headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
    }

def zhengwen(url):
    response=requests.get(url=url,headers=headers)
    response.encoding = response.apparent_encoding
    response_text=response.text

    soup=BeautifulSoup(response_text,'lxml')
    res=soup.find('div',class_='card bookmark-list').text.strip()

    return res

if __name__ == '__main__':
    url='http://www.shicimingju.com/book/sanguoyanyi.html'

    page=requests.get(url=url,headers=headers)
    page.encoding=page.apparent_encoding
    page_text=page.text
    soup=BeautifulSoup(page_text,'lxml')

    p=soup.select('div.book-mulu>ul>li>a')
    z=1
    with open('三国.txt','w',encoding='utf-8') as f:
        for i in p:
            print('正在下载第%s章'%z)
            z=z+1

            title=i.text
            page_url='https://www.shicimingju.com/'+i['href']
            zw=zhengwen(page_url)
            f.write(title+'\n'+zw)
            # f.write(title)
            # print(type(title))
            time.sleep(1)

#由于这个系统url='http://www.shicimingju.com/book/sanguoyanyi.html'自身的原因，它本身的网址跳转出现问题，所以无法正常的爬取正确的信息
#所以本次爬虫练习失败