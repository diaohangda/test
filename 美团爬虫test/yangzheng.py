from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver import ActionChains
import time
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
driver.get('https://bot.sannysoft.com/')

time.sleep(1000)
driver.quit()


# driver.get('https://verify.meituan.com/v2/web/general_page?action=spiderindefence&requestCode=6d8cdfe154ac40cd90090c740bb6f9a8&platform=1000&adaptor=auto&succCallbackUrl=https%3A%2F%2Foptimus-mtsi.meituan.com%2Foptimus%2FverifyResult%3ForiginUrl%3Dhttp%253A%252F%252Fwww.meituan.com%252Fmeishi%252F98534322%252F')
#
# time.sleep(100)
# # hukuai=driver.find_element_by_id('yodaBox')
# # juli=driver.find_element_by_class_name('bg-tip')
# # print(hukuai.size)
#
# # action = ActionChains(driver)
# # action.drag_and_drop_by_offset(hukuai,230,33).perform()
# # time.sleep(30)
# js = "var q=document.getElementsByClassName('boxStatic')[0].scrollTop = 220"  # getElementsByClassName表示获取class='main'的元素列表，0表示第一个，所以使用的时候要加索引
# driver.execute_script(js)
driver.quit()
