#-*- codeing = utf-8 -*-
#@Time : 2021/9/3 15:43
#@Author :DHD
#@File : 古诗2.py
#@Software : PyCharm

import requests
import re
from bs4 import BeautifulSoup
import os
import time
import pymysql

def get_name(url):#获取响应数据
    getpage=requests.get(url=url)  #发送请求
    page_text=getpage.text

    dd='<span><a href="(.*?)" target="_blank">.*?</a>.*?</span>'#获得古诗名、作者、网址
    p=re.compile(dd,re.S)
    res_url=p.findall(page_text)
    return res_url

def get_body(url):#获得古诗
    gusi = requests.get(url=url)
    gusi_text = gusi.text
    soup=BeautifulSoup(gusi_text,'lxml')

    tou=soup.select('h1')
    human=soup.select('p.source>a')
    body=soup.select('div.contson')
    wei=soup.select('div.contyishang>p')
    wei=str(wei)
    tt='<p>.*?韵译.*?<br/>(.*?)</p>'
    mi=re.findall(tt,wei)


    for toues,humanes,bodyes in zip(tou,human,body):
        ming = toues.get_text()
        ren=humanes.get_text()
        ci=bodyes.get_text()
        ming="'"+ming+"'"
        ren = "'" + ren + "'"
        ci = "'" + ci + "'"

        ku(ming,ren,ci)#存到数据库
        # memory(name,ren,ci)#存到指定文件夹
        time.sleep(1)

def ku(mines,humans,bodys):#数据库
    kun=pymysql.connect("localhost","root","root","gusiwen")
    cu=kun.cursor()
    sql="insert into gusi(ming,human,body) value (%s,%s,%s)"%(mines,humans,bodys)
    # sql="select * from gusi"
    cu.execute(sql)

    kun.commit()
    # cu.close()
    kun.close()




def memory(name,ren,ci):#持久式存储
    if not os.path.exists('唐诗三百首2'):#创建文件夹
        os.mkdir('唐诗三百首2')

    with open('唐诗三百首2/'+name+'.txt','w',encoding='utf-8') as f:#把古诗存进文件夹
        f.write(str(name)+'\n'*2+str(ren)+'\n'*2+str(ci))

if __name__ == '__main__':
    url='https://so.gushiwen.cn/gushi/tangshi.aspx'#指定url
    res_url=get_name(url)
    for de in res_url:
        body_url = 'https://so.gushiwen.cn/' + de
        get_body(body_url)
