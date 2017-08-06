#! python3
# lucky.py - Opens several Google search results.
import requests, sys, webbrowser, bs4

print('\n正在百度…')  # display text while downloading the Google page
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) Chrome/50.0.2661.102'}
payload = {'wd': sys.argv[1:]}  # 从命令行接收要搜索的关键字
url = 'https://www.baidu.com/s'

res = requests.get(url, params=payload, headers=headers)
res.raise_for_status()
print('正在打开搜索页面：' + res.url)
webbrowser.open(res.url)
print()

# Retrieve top search result links.
soup = bs4.BeautifulSoup(res.text, "html.parser")

# Open a browser tab for each result.
linkElements = soup.select('#content_left [class^=result] [class~=t] a')

for i in linkElements:
    if i.getText() == '官网':
        del linkElements[linkElements.index(i)]
print('首页共有%d个选项：' % len(linkElements))

for i in linkElements:
    print(i.getText())
print()

numOpen = min(3, len(linkElements))
for i in range(numOpen):
    print('正在打开第%d个页面…' % (i + 1))
    webbrowser.open(linkElements[i].get('href'))

print()
print('完成！\n')
