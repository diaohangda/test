# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class FilmPipeline:
    def process_item(self, item, spider):
        # print(item['munber'])

        fp=open('movie_name.txt','a')
        fp.write(item['name']+'\t'*3+item['mianhumber']+'\t'*3+item['miantitle']+'\n')
        fp.close()

        # with open('movie_name.txt','a') as f:
        #     f.write(item['munber'].encode("utf-8")+'\t'*3+item['name'].encode("utf-8")+'\t'*3+item['mianhumber'].encode("utf-8")+'\t'*3+item['miantitle'].encode("utf-8")+'\n')


