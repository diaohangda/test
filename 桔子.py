#-*- codeing = utf-8 -*-
#@Time : 2021/8/31 19:30
#@Author :DHD
#@File : 桔子.py
#@Software : PyCharm
#coding=utf-8

import requests
import re
import time

url='http://scxk.nmpa.gov.cn:81/xk/itownet/portalAction.do?method=getXkzsList'
header={
    'User-Agent':'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Mobile Safari/537.36 Edg/92.0.902.84'
}

with open('桔子.txt', 'w', encoding='utf-8') as f:
    for i in range(1,21):
        data={
        'on': 'true',
        'page':str(i),
        'pageSize': '15',
        'productName':'',
        'conditionType': '1',
        'applyname':'',
        'applysn': ''
    }

        response=requests.post(url=url,data=data,headers=header).text
        rexx=r'"ID":"(.*?)"'
        idname=re.findall(rexx,response)

        for i in idname:
            url_p='http://scxk.nmpa.gov.cn:81/xk/itownet/portalAction.do?method=getXkzsById'
            datas={
                'id':i
            }
            res=requests.post(url=url_p,data=datas,headers=header).text
            f.write(res+'\n')
            time.sleep(1)




