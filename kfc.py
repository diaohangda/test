#-*- codeing = utf-8 -*-
#@Time : 2021/8/31 13:53
#@Author :DHD
#@File : kfc.py
#@Software : PyCharm

import requests
import pymysql
import time

url='https://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=keyword'
header={
    'User-Agent':'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Mobile Safari/537.36 Edg/92.0.902.84'
}

# city=input('请输入城市名：')
city='广州'

with open('kfc.txt','w',encoding='utf-8') as f:
    db=pymysql.connect("localhost","root","root","gusiwen")
    cursor=db.cursor()
    for index in range(1,5):
        data={
            'cname':'',
            'pid':'',
            'keyword': city,
            'pageIndex': index,
            'pageSize': '10'
        }
        response=requests.post(url=url,data=data,headers=header).json()

        for dic in response['Table1']:
            Num=dic['rownum']
            Name=dic['storeName']
            Address=dic['addressDetail']
            f.write('Num:'+str(Num)+'\t'+'Name:'+Name+'\t'+'address:'+Address+'\n')

            # sql='insert into kfc(num,ming,address) value (%d,"%s","%s")'%(Num,Name,Address)
            sql='insert into kfc(num,ming,address) value ({},"{}","{}")'.format(Num,Name,Address)
            cursor.execute(sql)
            time.sleep(1)

    db.commit()
    db.close()
    print("over!!!")