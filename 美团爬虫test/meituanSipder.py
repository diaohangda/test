import time
import random
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd

class Meituan():
    def __init__(self,driver):
        """
        : return list_information:店铺信息列表[店名，地址，电话，图片1...5]
        """
        self.HTTP='https:'
        self.driver=driver
        self.list_information=[]


    def pageHandle(self):
        try:
            wait = WebDriverWait(self.driver, 3, 0.5)
            ###获取下一页连接
            next_url = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="icon-btn_right"]')))
            ###获取店家连接
            dianjia_url = wait.until(EC.presence_of_all_elements_located((By.XPATH, '//div[@class="img"]//a')))
            self.dianjiaInformation(dianjia_url)
            time.sleep(random.uniform(2.5, 4.0))
            if 'disabled' in next_url.get_attribute('class'):
                print('no next!')
            else:
                next_url.click()
            # return self.list_information
        except Exception as e:
            print(e.args)
            self.driver.quit()

    def dianjiaInformation(self,dianjia_node):
        try:
            wait = WebDriverWait(self.driver, 4, 0.5)
            for node in dianjia_node:
                node.click()

                details = wait.until(
                    EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/section/div/div[2]')))

                name = details.find_element_by_xpath('./div[1]/div[1]').text.split('\n')[1].strip()  ##店家名字
                address = details.find_element_by_xpath('./div[1]/div[3]/p[1]').text.split('：')[1].strip()  ##店铺地址
                tel = details.find_element_by_xpath('./div[1]/div[3]/p[2]').text.split('：')[1].strip()  ##电话
                one_images = details.find_element_by_xpath('.//div[2]/div/div/img').get_attribute('src')  # 第一张图
                imagesList = details.find_elements_by_xpath('./div[2]/ul//li/div')  # 其余四张
                image_list = [name, address, tel, one_images]
                for image in imagesList:
                    image_list.append(image.find_element_by_xpath('./img').get_attribute('src'))
                self.driver.back()
                self.list_information.append(image_list)
                time.sleep(random.uniform(2.5, 4.0))

        except Exception as e:
            print(e.args)
            self.driver.quit()