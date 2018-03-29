from selenium import webdriver
import time

browser = webdriver.Edge()
browser.get('https://qzone.qq.com/')
browser.switch_to.frame("login_frame")
elem = browser.find_element_by_link_text('帐号密码登录')  # find_element_by_id("switcher_plogin").click()
elem.click()
user = browser.find_element_by_id("u")  # find_element_by_xpath('//*[@id="u"]')
user.clear()
user.send_keys('***')
password = browser.find_element_by_id("p")  # find_element_by_xpath('//*[@id="p"]')
password.clear()
password.send_keys('***')
browser.find_element_by_id("login_button").click()
time.sleep(5)
browser.quit()
