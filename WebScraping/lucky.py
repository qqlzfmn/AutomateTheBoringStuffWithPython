#! python3
# lucky.py - Opens several Google search results.
import requests, sys, webbrowser, bs4

print('正在百度…')  # display text while downloading the Google page
res = requests.get('https://www.baidu.com/baidu?&ie=utf-8&word=' + 'url')  # .join(sys.argv[1:])
res.raise_for_status()
# Retrieve top search result links.
soup = bs4.BeautifulSoup(res.text, "html.parser")
# Open a browser tab for each result.
linkElements = soup.select('div#content_left h3 a')
numOpen = min(5, len(linkElements))
for i in range(numOpen):
    webbrowser.open(linkElements[i].get('href'))
