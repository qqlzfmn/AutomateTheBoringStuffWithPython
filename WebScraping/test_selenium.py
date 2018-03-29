from selenium import webdriver
import time

# 模拟登陆QQ空间
browser = webdriver.Edge()  # 打开浏览器
browser.get('https://qzone.qq.com/')  # 打开QQ空间主页
browser.switch_to.frame("login_frame")  # 切换到'login_frame'帧
elem = browser.find_element_by_link_text('帐号密码登录')  # find_element_by_id("switcher_plogin").click()
elem.click()  # 点击'帐号密码登录'
user = browser.find_element_by_id("u")  # find_element_by_xpath('//*[@id="u"]')
user.clear()  # 清空输入框
user.send_keys('***')  # 输入账号
password = browser.find_element_by_id("p")  # find_element_by_xpath('//*[@id="p"]')
password.clear()  # 清空输入框
password.send_keys('***')  # 输入密码
browser.find_element_by_id("login_button").click()  # 点击登录按钮
time.sleep(5)  # 等待5秒查看效果
browser.quit()  # 关闭浏览器

# 模拟登陆微博
browser = webdriver.Edge()  # 打开浏览器
browser.get('https://weibo.com/')  # 打开微博主页
time.sleep(5)  # 等待页面加载完成
is_my_page = browser.title == '我的首页 微博-随时随地发现新鲜事'  # 判断标题是否是个人主页的标题
is_main_page = browser.title == '微博-随时随地发现新鲜事'  # 判断标题是否是登录页标题
if is_my_page:
    setting_button = browser.find_element_by_xpath(
        '//*[@id="plc_top"]/div/div/div[3]/div[2]/div[2]/a/em').click()  # 点击设置按钮
    time.sleep(1)  # 等待下拉菜单加载完成
    quit_button = browser.find_element_by_link_text('退出').click()  # 点击退出按钮
time.sleep(5)  # 等待退出后的页面加载完成
user = browser.find_element_by_xpath('//*[@id="loginname"]')  # 找到账号输入框
user.clear()  # 清空输入框
user.send_keys('***')  # 输入账号
password = browser.find_element_by_xpath('//*[@id="pl_login_form"]/div/div[3]/div[2]/div/input')  # 找到密码输入框
password.clear()  # 清空输入框
password.send_keys('***')  # 输入密码
browser.find_element_by_xpath('//*[@id="pl_login_form"]/div/div[3]/div[6]/a').click()  # 点击登录按钮
time.sleep(5)  # 等待5秒查看效果
browser.quit()  # 关闭浏览器
