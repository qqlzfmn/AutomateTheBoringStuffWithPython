# ! python3
# downloadMzitu.py - Download beauty pictures.
import requests, bs4, os


def header(referer):  # 设置从浏览器调试程序得到的header信息
    headers = {'Host': 'i.meizitu.net',
               'Connection': 'keep-alive',
               'Accept': 'image/webp,image/*,*/*;q=0.8',
               'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) Chrome/50.0.2661.102 Safari/537.36',
               'Referer': '{}'.format(referer),
               'Accept-Encoding': 'gzip, deflate, sdch',
               'Accept-Language': 'zh-CN,zh;q=0.8'}
    return headers


urls = [''] * 5  # 开一个长度为5数据类型为string的空列表
for i in range(5):
    urls[i] = 'http://www.mzitu.com/hot/page/%s/' % (i + 1)  # 最热分类一共有5页
os.makedirs('Mzitu', exist_ok=True)  # 创建总文件夹
p = 0  # 已下载专辑数

# 查询总专辑数
for url in urls:
    try:
        res = requests.get(url)
    except Exception:
        pass
    soup = bs4.BeautifulSoup(res.text, "html.parser")
    albums = soup.select('#pins > li > a')

    # 查询每个专辑包含的文件数
    for album in albums:
        href = album.get('href')
        try:
            hrefRes = requests.get(href)
        except Exception:
            pass
        hrefSoup = bs4.BeautifulSoup(hrefRes.text, "html.parser")
        picNumRes = hrefSoup.select('body > div.main > div.content > div.pagenavi > a')
        picNum = int(picNumRes[4].select('span')[0].getText())

        # 创建子文件夹
        subFolder = album.select('img')[0].get('alt')  # Tag数据类型也支持select方法
        subFolder = subFolder.replace('\\', '').replace('/', '').replace(':', '').replace('*', '') \
            .replace('?', '').replace('"', '').replace('<', '').replace('>', '').replace('|', '')  # 去除不合法的符号
        subFolder = os.path.join('Mzitu', '【%sP】%s' % (picNum, subFolder))
        print('正在创建子文件夹：' + subFolder + '...')
        try:
            os.makedirs(subFolder, exist_ok=True)
        except FileExistsError:
            pass

        # 打开专辑页面，下载图片
        for i in range(picNum):
            pageUrl = href + '/' + str(i + 1)
            try:
                pageRes = requests.get(pageUrl)
            except Exception:
                pass
            pageSoup = bs4.BeautifulSoup(pageRes.text, "html.parser")
            picRes = pageSoup.select('body > div.main > div.content > div.main-image > p > a > img')
            picUrl = picRes[0].get('src')
            try:
                pic = requests.get(picUrl, headers=header(picUrl))
            except Exception as e:
                print(e)
                pass
            print('正在下载文件：' + os.path.basename(picUrl) + '...')
            imageFile = open(os.path.join(subFolder, os.path.basename(picUrl)), 'wb')  # 把漫画的图片保存到本地
            for chunk in pic.iter_content(100000):
                imageFile.write(chunk)
            imageFile.close()

        # 提示下载进度
        p = p + 1
        print('已下载%d个专辑\n' % p)
print('全部完成！')
