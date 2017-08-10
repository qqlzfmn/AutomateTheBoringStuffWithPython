#! python3
# downloadXkcd.py - Downloads every single XKCD comic.
import requests, os, bs4, re

url = 'https://xkcd.com'  # starting url
os.makedirs('xkcd', exist_ok=True)  # store comics in ./xkcd
comicUrlPattern = re.compile('http.+png')  # 匹配 http…png
while not url.endswith('#'):  # 第一张漫画的Prev按钮链接到http://xkcd.com/# 表明没有前一个页面了
    # Download the page.
    print('Downloading page %s…' % url)
    try:
        res = requests.get(url)  # 返回一个Response对象
        res.raise_for_status()  # 通过检查Response对象的status_code属性，可以了解对这个网页的请求是否成功
    except Exception as e:
        print(e)
    soup = bs4.BeautifulSoup(res.text, "html.parser")  # 下载的页面作为一个字符串，保存在Response对象的text变量中。
    # Find the URL of the comic image.
    comicElems = soup.select('#middleContainer')  # 整个正文部分，包括标题、漫画、按钮和URL
    for comicElem in comicElems:
        try:
            # findAll(text=True)时，会直接提取整个html的text。text可以接受正则findAll(text=re.compile("pattern"))
            comicUrl = comicUrlPattern.findall(comicElem.findAll(text=re.compile("http"))[1])[0]  # 提取漫画的URL
        except Exception as e:
            print(e)
    # Download the image.
    print('Downloading image %s…' % comicUrl)
    try:
        res = requests.get(comicUrl)  # 下载漫画的图片
        res.raise_for_status()
    except Exception as e:
        print(e)
    # Save the image to ./xkcd.
    imageFile = open(os.path.join('xkcd', os.path.basename(comicUrl)), 'wb')  # 把漫画的图片保存到本地
    for chunk in res.iter_content(100000):
        imageFile.write(chunk)
    imageFile.close()
    # Get the Prev button's url.
    prevLink = soup.select('a[rel="prev"]')[0]  # 找到prev按钮，查看对应的URL为下一个需要下载的页面
    url = 'http://xkcd.com' + prevLink.get('href')  # URL变为前一页的URL
print('Done.')
