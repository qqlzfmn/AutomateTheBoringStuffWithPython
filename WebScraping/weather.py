import requests, bs4, os, time

# downloader
weather = requests.get('http://www.tianqi.com/')  # 数据来源：天气网
weatherFile = open('weather.html', 'wb')  # 下载到本地weather.html文件里
for chunk in weather.iter_content(100000):  # 分包写入
    weatherFile.write(chunk)
weatherFile.close()

# parser
weatherFile = open('weather.html')
weatherSoup = bs4.BeautifulSoup(weatherFile, "html.parser")  # 用html解析器解析
cities = weatherSoup.select('div.right250 div.box250c a div.tqindex h3')  # 找到相应位置的数据
weathers = weatherSoup.select('div.right250 div.box250c a div.tqindex li.cDRed')
temperatures = weatherSoup.select('div.right250 div.box250c a div.tqindex span font')
futures = weatherSoup.select('div.right250 div.box250c div.wtline')
temperatures = temperatures[0].getText() + '～' + temperatures[1].getText()

# display
print(time.ctime())  # 当前时间
print('%s  %-3s  %s' % (cities[0].getText(), weathers[0].getText(), temperatures))  # 打印
print('明天  %-3s  %s' % (futures[0].getText(), futures[1].getText()))
print('后天  %-3s  %s' % (futures[2].getText(), futures[3].getText()))
print('大后天  %-3s  %s' % (futures[4].getText(), futures[5].getText()))

# clean up
weatherFile.close()
os.remove('weather.html')
