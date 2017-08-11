# 用selenium模块控制浏览器

1. 安装selenium模块  
    ```pip install selenium```
    
2. 导入selenium模块  
    ```from selenium import webdriver```
    
3. selenium模块支持的浏览器  
    - Chrome
    - Edge
    - Firefox
    - IE
    - Opera
    - Safari
    
4. 启动浏览器（以Edge为例）  
    ```browser = webdriver.Edge()```  
    
    此时会提示selenium.common.exceptions.WebDriverException类型的错误：
    > selenium.common.exceptions.WebDriverException:
    Message: 'MicrosoftWebDriver.exe' executable needs to be in PATH.
    Pleasedownload from http://go.microsoft.com/fwlink/?LinkId=619687
    
    我们去[WebDriver - Microsoft Edge Development](http://go.microsoft.com/fwlink/?LinkId=619687)下载Edge浏览器的WebDriver。  
    其他浏览器请根据你的错误提示的最后一句找到下载WebDriver的网站。 
    
    进入网站我们发现Downloads里有很多版本供我们下载，所以首先我们要确定下载哪个版本的WebDriver。  
    
    Win10点击 开始→设置→系统→关于，找到「OS版本」  
    对应「OS 版本」再回到[WebDriver - Microsoft Edge Development](http://go.microsoft.com/fwlink/?LinkId=619687)页面下载相应版本的WebDriver。  
    
    下载完的WebDriver随意放在你想放的位置，然后复制这个路径，添加到系统环境变量的Path里。  
    
    大功告成，再次执行```browser = webdriver.Edge()```你会发现错误提示没有了，而且会打开你的Edge浏览器（先别关这个浏览器，后面还要用到），还有错误提示的小伙伴请重启你的CMD或PowerShell。  
    
5. 打开网页  
    ```browser.get('http://lzf.kim/')```  
    执行完这一句你会发现之前打开的浏览器打开了一个百度首页。
    
6. 在页面中寻找元素  
	- selenium的WebDriver方法，用于寻找元素：
	
	|方法名|返回的WebElement对象/列表|
	|---|---|
	|browser.find_element_by_class_name(name) browser.find_elements_by_class_name(name)|使用CCS类name的元素|
	|browser.find_element_by_css_selector(selector) browser.find_elements_by_css_selector(selector)|匹配CCS selector的元素|
	|browser.find_element_by_id(id) browser.find_elements_by_id(id)|匹配id属性值的元素|
	|browser.find_element_by_link_text(text) browser.find_elements_by_link_text(text)|完全匹配提供的text的\<a>元素|
	|browser.find_element_by_partial_link_text(text) browser.find_elements_by_partial_link_text(text)|包含提供的text的\<a>元素|
	|browser.find_element_by_name(name) browser.find_elements_by_name(name)|匹配name属性值的元素|
	|browser.find_element_by_tag_name(name) browser.find_elements_by_tag_name(name)|匹配标签name的元素（大小写无关，\<a>元素匹配'a'和'A'）|
	
	- WebElement的属性和方法
	
	|属性或方法|描述|
	|---|---|
	|tag_name|标签名，例如'a'表示\<a>元素|
	|get_attribute(name)|该元素name属性的值|
	|text|该元素内的文本，例如\<span>hello\</span>中的'hello'|
	|clear()|对于文本字段或文本区域元素，清除其中输入的文本|
	|is_displayed()|如果该元素可见，返回True，否则返回False|
	|is_selected()|对于复选框或单选框元素，如果该元素被选中，返回True，否则返回False|
	|location|一个字典，包含键'x'和'y'，表示该元素在页面上的位置|
	
	例：  
	```elem = browserfind_element_by_link_text('关于我')```  
	该指令试图找到文本是'关于我'的\<a>元素。
	
7. 点击页面  
    ```elem.click()```  
    该指令模拟点击elem这个元素
    
8. 