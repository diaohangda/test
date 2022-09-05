# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from selenium.webdriver.chrome.options import Options
from selenium import webdriver
import time
from meituanSipder_two import MeiTuan
from meituanJieHun import jiehun
from meituanJiuBa import jiuba
import random
import re

def chuangjian_driver():                #创建一个driver对象
    chrome_options = Options()
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument('lang=zh_CN.UTF-8')
    ###解决浏览器受控制信息
    chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
    chrome_options.add_experimental_option('useAutomationExtension', False)
    chrome_options.add_argument(
        'user-agent=Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2227.0 Safari/537.36')
    chrome_options.add_argument("--disable-blink-features=AutomationControlled")
    path = r'D:\Python\Scripts\chromedriver.exe'
    driver = webdriver.Chrome(executable_path=path, options=chrome_options)
    return driver

def xuanzhe_chengshi(driver):                             #通过网页选择城市，并且返回城市名
    # driver = webdriver.Chrome(R'./venv/Scripts/chromedriver.exe')
    driver.get("https://www.meituan.com/changecity/")
    while(True):
        time.sleep(0.5)
        F_url = driver.current_url
        if(re.search('changecity',F_url) == None):
            time.sleep(2)
            T_url = driver.current_url
            break
    T_url = re.match(r'https://(.*?).meituan',T_url).group(1)
    # driver.close()
    return T_url

def denglu_test(T_url,driver):
    url = "https://"+T_url+".meituan.com"        #不带项目的网址
    driver.get(url+"/meishi/pn65/")                    #倒是改为自定义（城市+项目+页数）
    # if (currentPageUrl != url):
    # driver.get(url+"/meishi/")
    time.sleep(1)
    currentPageUrl = driver.current_url                             #获取当前网页url,判断是否需要登录
    currentPageUrl=re.match(r'https://(.*?).meituan',currentPageUrl).group(1)
    if(currentPageUrl=='passport'):

        '''a = '17688233623'
        b = 'qwe123456'
        for i in range(len(a)):            #输入账号
            driver.find_element_by_id('login-email').send_keys(a[io])
            sjs = random.random()
            time.sleep(sjs)
        for i in range(len(b)):             #输入密码
            driver.find_element_by_id('login-password').send_keys(b[i])
            sjs = random.random()
            time.sleep(sjs)
        driver.find_element_by_css_selector("input[value='登录']").click()'''            #登录
        while(True):                                                                   #判断是否要验证
            time.sleep(2)
            currentPageUrl = driver.current_url
            if(currentPageUrl == url+'/meishi/pn65/'):
                break
        time.sleep(3)
def request_get(driver):
    pass


def huoqu_dp(driver):                                               #获取除了美食，结婚，酒吧以外的店铺连接
    meun = driver.find_elements_by_xpath('//div[@class="abstract-item clearfix"]//a')
    xxjs_dianpu = []
    for meun in meun:
        xxjs_dianpu.append(meun.get_attribute("href"))
    return xxjs_dianpu                                                 #返回店铺的连接

def huoquxx_xxjs(driver):                                         #获取休闲娱乐和健身的信息
    xxjs_dianpu = huoqu_dp(driver)
    driver.get(xxjs_dianpu[0])
    name = driver.find_element_by_xpath('//h1[@class="seller-name"]').text
    address = driver.find_element_by_xpath('//div[@class="seller-info-body"]/div[1]/a/span').text
    tel = driver.find_element_by_xpath('//div[@class="seller-info-body"]/div[2]/span[2]').text
    one_images = driver.find_element_by_xpath('//div[@class="now-img"]').get_attribute("style")
    two_images = driver.find_element_by_xpath('//div[@class="album-ul clearfix"]/div[1]').get_attribute("style")
    three_images = driver.find_element_by_xpath('//div[@class="album-ul clearfix"]/div[2]').get_attribute("style")
    four_images = driver.find_element_by_xpath('//div[@class="album-ul clearfix"]/div[3]').get_attribute("style")
    five_images = driver.find_element_by_xpath('//div[@class="album-ul clearfix"]/div[4]').get_attribute("style")
    images = [one_images,two_images,three_images,four_images,five_images]
    for i in range(5):
        images[i] = re.match(r'background-image: url\("(.*?)"\);',images[i]).group(1)
        print(images[i])
    print(name,address,tel,images)

def huoquxx_Cxxjs(driver):
    xxjs_dianpu = huoqu_dp(driver)
    driver.get(xxjs_dianpu[0])
    name = driver.find_element_by_xpath('//h1[@class="seller-name"]').text
    address = driver.find_element_by_xpath('//div[@class="seller-info-body"]/div[1]/a/span').text
    tel = '无联系方式'
    one_images = driver.find_element_by_xpath('//div[@class="now-img"]').get_attribute("style")
    two_images = driver.find_element_by_xpath('//div[@class="album-ul clearfix"]/div[1]').get_attribute("style")
    three_images = driver.find_element_by_xpath('//div[@class="album-ul clearfix"]/div[2]').get_attribute("style")
    four_images = driver.find_element_by_xpath('//div[@class="album-ul clearfix"]/div[3]').get_attribute("style")
    five_images = driver.find_element_by_xpath('//div[@class="album-ul clearfix"]/div[4]').get_attribute("style")
    images = [one_images, two_images, three_images, four_images, five_images]
    for i in range(5):
        images[i] = re.match(r'background-image: url\("(.*?)"\);', images[i]).group(1)
        print(images[i])
    print(name, address, tel, images)

if __name__ == '__main__':
    driver = chuangjian_driver()
    try:
        T_url = xuanzhe_chengshi(driver)
        denglu_test(T_url,driver)

        meituan=MeiTuan(driver)
        #
        # meituan=MeiTuan(driver)
        meituan.pageHandle()

        driver.quit()
    except Exception as e:
        print(e.args)
        driver.quit()


# def dianpu_lianjie(driver):
#     menu = driver.find_elements_by_xpath('//div[@class="img"]//a')  # 爬取出当前页面店铺的连接
#     dianpu_lianjie = []
#     for menu in menu:
#         dianpu_lianjie.append(menu.get_attribute("href"))
#     print(dianpu_lianjie)
#     return dianpu_lianjie  # 将当前页面的店铺链接返回
#
# def  fangwen_dianpu():
#     New_dplj = dianpu_lianjie(driver)
#     print(New_dplj[0])
#     for i in range(len(New_dplj)):
#         time.sleep(3)
#         driver.get(New_dplj[i])
#         menu = driver.find_element_by_xpath('//div[@class="d-left"]').get_attribute('innerHTML')
#         print(menu)