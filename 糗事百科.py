#-*- codeing = utf-8 -*-
#@Time : 2021/9/1 10:21
#@Author :DHD
#@File : 糗事百科.py
#@Software : PyCharm


import requests
import re
import os

# 创建文件夹
if not os.path.exists('images'):
    os.mkdir('images')

start_page=int(input('开始页：'))
end_page=int(input('结束页：'))
for q in range(start_page,end_page+1):
    url='https://www.qiushibaike.com/imgrank/page/q/'
    header={
        'User-Agent':'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Mobile Safari/537.36 Edg/92.0.902.84'
    }


    response=requests.get(url=url,headers=header)
    # jpg=re.findall(r'<div class="thumb">.*?<img src="(.*?)" alt.*?</div>',response)
    f=open('糗事.txt','w',encoding='utf-8')
    f.write(response.text)
    f.close()
    e = '<a href="/article.*?<img src="(.*?)" alt.*?</a>'
    pa = re.compile(e, re.S)
    image_urls = pa.findall(response.text)

    for image_url in image_urls:
        image_url = 'https:' + image_url
        image_name = image_url.split('/')[-1]
        image_path = 'images/' + image_name
        image_data = requests.get(url=image_url, headers=header).content
        with open(image_path, 'wb') as fp:
            fp.write(image_data)





