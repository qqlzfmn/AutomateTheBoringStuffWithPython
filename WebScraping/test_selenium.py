from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import time

# 模拟登陆QQ空间
# browser = webdriver.Edge()
# browser.get('https://qzone.qq.com/')
# browser.switch_to.frame("login_frame")
# elem = browser.find_element_by_link_text('帐号密码登录')  # find_element_by_id("switcher_plogin").click()
# elem.click()
# user = browser.find_element_by_id("u")  # find_element_by_xpath('//*[@id="u"]')
# user.clear()
# user.send_keys('***')
# password = browser.find_element_by_id("p")  # find_element_by_xpath('//*[@id="p"]')
# password.clear()
# password.send_keys('***')
# browser.find_element_by_id("login_button").click()
# time.sleep(5)
# browser.quit()

# 模拟登陆微博
browser = webdriver.Edge()
browser.get('https://weibo.com/')
time.sleep(5)
wait = WebDriverWait(browser, 10)
is_my_page = EC.title_is('我的首页 微博-随时随地发现新鲜事')(browser)
is_main_page = EC.title_is('微博-随时随地发现新鲜事')(browser)
if is_my_page:
    setting_button = browser.find_element_by_xpath('//*[@id="plc_top"]/div/div/div[3]/div[2]/div[2]/a/em').click()
    time.sleep(1)
    quit_button = browser.find_element_by_link_text('退出').click()
time.sleep(5)
user = browser.find_element_by_xpath('//*[@id="loginname"]')
user.clear()
user.send_keys('***')
password = browser.find_element_by_xpath('//*[@id="pl_login_form"]/div/div[3]/div[2]/div/input')
password.clear()
password.send_keys('***')
browser.find_element_by_xpath('//*[@id="pl_login_form"]/div/div[3]/div[6]/a').click()
time.sleep(5)
browser.quit()
