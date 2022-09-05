#-*- codeing = utf-8 -*-
#@Time : 2021/8/16 23:27
#@Author :DHD
#@File : 网页采集器.py
#@Software : PyCharm

import requests

header={
    'User-Agent':'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Mobile Safari/537.36 Edg/92.0.902.73'
}
wb1=input('输入搜索内容：')

# url='https://www.baidu.com/s?wd={}'.format(wb1)  #第一想法
# response=requests.get(url=url,headers=header)

url='https://www.sogou.com/web'
param={
    'query':wb1
}
response=requests.get(url=url,params=param,headers=header)
page_text=response.text

with open('网页采集器.html','w',encoding='utf-8') as f:
    f.write(page_text)

print("完成！")