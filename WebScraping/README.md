# 用 selenium 模块控制浏览器

1. 安装 selenium 模块  
    ```python 
	pip install selenium
	```
    
2. 导入 selenium 模块  
    ```python 
	from selenium import webdriver
	```
    
3. selenium 模块支持的浏览器  
    - Chrome
    - Edge
    - Firefox
    - IE
    - Opera
    - Safari  
	
4. 启动浏览器 （以 Edge 为例）  
    ```python 
	browser = webdriver.Edge()
	```  
    
    此时会提示 ```selenium.common.exceptions.WebDriverException``` 类型的错误：

    > selenium.common.exceptions.WebDriverException:
    Message: 'MicrosoftWebDriver.exe' executable needs to be in PATH.
    Pleasedownload from http://go.microsoft.com/fwlink/?LinkId=619687
    
    我们去 [WebDriver - Microsoft Edge Development](http://go.microsoft.com/fwlink/?LinkId=619687) 下载 Edge 浏览器的 WebDriver。  
    其他浏览器请根据你的错误提示的最后一句找到下载 WebDriver 的网站。 
    
    进入网站我们发现 Downloads 里有很多版本供我们下载，所以首先我们要确定下载哪个版本的 WebDriver。  
    
    Win 10 点击 开始 → 设置 → 系统 → 关于，找到「OS版本」。  
    对应「OS 版本」再回到 [WebDriver - Microsoft Edge Development](http://go.microsoft.com/fwlink/?LinkId=619687) 页面下载相应版本的 WebDriver。  
    
    下载完的 WebDriver 随意放在你想放的位置，然后把这个路径添加到系统环境变量的 Path 里。  
    
    大功告成，再次执行 ```browser = webdriver.Edge()``` 你会发现错误提示没有了，而且会打开你的 Edge 浏览器 （先别关这个浏览器，后面还要用到）。  
	还有错误提示的小伙伴请重启你的 CMD 或 PowerShell。  
    
5. 打开网页  
    ```python 
	browser.get('http://lzf.kim/')
	```  
    执行完这一句你会发现之前打开的浏览器打开了一个百度首页。
    
6. 在页面中寻找元素  
    ```python 
	elem = browser.find_element_by_link_text('下一页 »')
	```  
	该指令试图找到文本是 「下一页 »」 的 \<a> 元素。
    
	- selenium 的 WebDriver 方法，用于寻找元素：
	
	|方法名|返回的 WebElement 对象/列表|
	|---|---|
	|browser.find_element_by_class_name(name) browser.find_elements_by_class_name(name)|使用 CCS 类 name 的元素|
	|browser.find_element_by_css_selector(selector) browser.find_elements_by_css_selector(selector)|匹配 CCS selector 的元素|
	|browser.find_element_by_id(id) browser.find_elements_by_id(id)|匹配 id 属性值的元素|
	|browser.find_element_by_link_text(text) browser.find_elements_by_link_text(text)|完全匹配提供的 text 的 \<a> 元素|
	|browser.find_element_by_partial_link_text(text) browser.find_elements_by_partial_link_text(text)|包含提供的 text 的 \<a> 元素|
	|browser.find_element_by_name(name) browser.find_elements_by_name(name)|匹配 name 属性值的元素|
	|browser.find_element_by_tag_name(name) browser.find_elements_by_tag_name(name)|匹配标签 name 的元素 （大小写无关，\<a> 元素匹配 'a' 和 'A' ）|
	
	- WebElement 的属性和方法：
	
	|属性或方法|描述|
	|---|---|
	|tag_name|标签名，例如 'a' 表示 \<a> 元素|
	|get_attribute(name)|该元素 name 属性的值|
	|text|该元素内的文本，例如 \<span>hello\</span> 中的 'hello'|
	|clear()|对于文本字段或文本区域元素，清除其中输入的文本|
	|is_displayed()|如果该元素可见，返回 True，否则返回 False|
	|is_selected()|对于复选框或单选框元素，如果该元素被选中，返回 True，否则返回 False|
	|location|一个字典，包含键 'x' 和 'y'，表示该元素在页面上的位置|
	
7. 点击页面  
    ```python 
	elem.click()
	```  
    该指令模拟点击 elem 这个元素
    
8. 填写并提交表单
    ```python 
    search = browser.find_element_by_css_selector('#s')
    search.send_keys('数字图像处理')
    search.submit()
    ```  
    
9. 发送特殊按键
    ```python 
    from selenium.webdriver.common.keys import Keys
    elem = browser.find_element_by_tag_name('html')
    elem.send_keys(Keys.END)
    ```
    
    特殊按键保存在 ```selenium.webdriver.common.keys.Keys``` 里，所以需要 ```from selenium.webdriver.common.keys import Keys```。  
	然后随意选取一个元素，或者选取整个页面 （即\<html>标签） ```elem = browser.find_element_by_tag_name('html')```。  
	最后向该元素发送按键 ```elem.send_keys(Keys.END)```。
    
    - ```selenium.webdriver.common.keys``` 模块中常用的变量：
    
	|属性|含义|
	|---|---|
	|Keys.DOWN, Keys.UP, Keys.LEFT, Keys.RIGHT|键盘箭头键|
	|Keys.ENTER, Keys.RETURN|Enter (\\n) 和 Return (\\r) 键|
	|Keys.HOME, Keys.END, Keys.PAGE_DOWN, Keys.PAGE_UP|Home、End、PageUp 和 PageDown 键|
	|Keys.ESCAPE, Keys.BACK_SPACE, Keys.DELETE|Esc、Backspace 和 Delete 键|
	|Keys.F1, Keys.F2, ... , Keys.F12|键盘顶部的 F1 到 F12 键|
	|Keys.Tab|Tab 键|
	
10. 点击浏览器按钮  
	```python 
	browser.back()
	```
	该指令模拟点击浏览器的返回按钮
	
	- selenium 模块能实现模拟点击的方法：
	
	|方法|功能|
	|---|---|
	|browser.back()|点击「返回」按钮|
	|browser.forward()|点击「前进」按钮|
	|browser.refresh()|点击「刷新」按钮|
	|browser.quit()|点击「关闭窗口」按钮|
	
11. 更多关于 selenium 的信息  
	[Selenium with Python — Selenium Python Bindings 2 documentation](http://selenium-python.readthedocs.io/)
