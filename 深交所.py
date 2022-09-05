#-*- codeing = utf-8 -*-
#@Time : 2021/10/19 14:52
#@Author :DHD
#@File : shenjiaosuo.py
#@Software : PyCharm


import requests
import pymysql
import time

def geturl(i):
    ajx_url='http://www.szse.cn/api/disc/announcement/detailinfo'
    headers = {
        'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
    }

    params={
        'random':'0.09293754430443402',
        'pageSize':'30',
        'pageNum':i,
        'plateCode':'szse'
            }
    response=requests.get(url=ajx_url,params=params,headers=headers).json()
    all=response['data']
    getdata(all)

def getdata(tex):
    url = 'http://www.szse.cn/disclosure/listed/notice/index.html'
    for i in tex:
        code=i['secCode']
        name=i['secName']
        for t in i['announList']:
            id=url+t['id']
            title=t['title']
            time=t['publishTime']
            data={
                'code':code,
                'name':name,
                'id':id,
                'title':title,
                'time':time,

            }

            kun(data)

def kun(data):
    sql = 'insert into shen(seccode,secname,secaddring,sectitle,sectime) value ("%s","%s","%s","%s","%s")' % (data['code'], data['name'], data['id'], data['title'],data['time'])
    cursor.execute(sql)

if __name__ == '__main__':
    db = pymysql.connect('localhost', 'root', 'root', 'gusiwen')
    cursor = db.cursor()

    for i in range(1,10):
        geturl(i)

    db.commit()
    db.close()

