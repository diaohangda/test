#-*- codeing = utf-8 -*-
#@Time : 2021/8/29 18:06
#@Author :DHD
#@File : jiongtu.py
#@Software : PyCharm

import requests
import re
import os
if __name__ == "__main__":
     url = 'https://www.qiushibaike.com/imgrank/page/%s/'
     headers={
         'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36',
     }

     #指定起始也结束页码
     page_start = int(input('enter start page:'))
     page_end = int(input('enter end page:'))

     #创建文件夹
     if not os.path.exists('images'):
         os.mkdir('images')

     #循环解析且下载指定页码中的图片数据
     for page in range(page_start,page_end+1):
         print('正在下载第%d页图片'%page)
         new_url = format(url % page)
         response = requests.get(url=new_url,headers=headers)

         #解析response中的图片链接
         e = '<div class="thumb">.*?<img src="(.*?)" alt.*?</div>'
         pa = re.compile(e,re.S)
         image_urls = pa.findall(response.text)

          #循环下载该页码下所有的图片数据
         for image_url in image_urls:
             image_url = 'https:' + image_url
             image_name = image_url.split('/')[-1]
             image_path = 'images/'+image_name
             image_data = requests.get(url=image_url,headers=headers).content
             with open(image_path,'wb') as fp:
                 fp.write(image_data)