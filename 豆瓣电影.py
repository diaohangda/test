#-*- codeing = utf-8 -*-
#@Time : 2021/8/23 23:33
#@Author :DHD
#@File : 豆瓣电影.py
#@Software : PyCharm

import requests
import re
import json

url='https://movie.douban.com/j/chart/top_list?type=25&interval_id=100%3A90&action=&start=0&limit=20'
header={
    'User-Agent':'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Mobile Safari/537.36 Edg/92.0.902.78'
}
param={
    'type': '25',
    'interval_id': '100:90',
    'action': '',
    'start': '0',
    'limit': '20'
}

response=requests.get(url=url,params=param,headers=header)
list=response.json()

with open('豆豆.txt', 'w', encoding='utf-8') as f:
    for lit in list:
        lites=str(lit)
        rank=re.findall("'rank': (.*?),",lites)
        name=re.findall("'title': '(.*?)'",lites)
        score=re.findall("'score': '(.*?)'",lites)
        types=re.findall("'types': (.*?)],",lites)
        for ranks,names,scores,typees in zip(rank,name,score,types):
            data={
                '序号': ranks,
                '名称': names,
                '评分': scores,
                '类别': typees

            }
            f.write(str(data)+'\n')


# with open('douban.txt', 'w+', encoding='utf-8') as f:
#     for lit in list:
#         f.write(str(lit))



# fp=open('豆瓣电影.json','w',encoding='utf-8')
# json.dump(dic,fp=fp,ensure_ascii=False)
#
# print('完成！')
