import requests

res = requests.get('http://www.gutenberg.org/cache/epub/1112/pg1112.txt')
res.raise_for_status()
# 必须用“写二进制”模式打开该文件，即向函数传入字符串'wb'，作为open()的第二参数。
# 即使该页面是纯文本的（例如前面下载的罗密欧与朱丽叶的文本），你也需要写入二进制数据
# 而不是文本数据，目的是为了保存该文本中的“Unicode 编码”。
playFile = open('RomeoAndJuliet.txt', 'wb')
# 为了将Web 页面写入到一个文件，可以使用for 循环和Response 对象的iter_content()方法。
# iter_content()方法在循环的每次迭代中，返回一段内容。每一段都是bytes 数据类型，你需要指定一段包含多少字节。
# 10 万字节通常是不错的选择，所以将100000作为参数传递给iter_content()。
for chunk in res.iter_content(100000):
    playFile.write(chunk)
playFile.close()
