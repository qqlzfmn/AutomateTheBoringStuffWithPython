import bs4

exampleFile = open('example.html')
exampleSoup = bs4.BeautifulSoup(exampleFile, "html.parser")
print(type(exampleSoup))

# 返回一个列表，其中包含所有带有id="author"的元素，将这个Tag对象的列表保存在变量elements中。
elements = exampleSoup.select('#author')
print(type(elements))
# len(elems)告诉我们列表中只有一个Tag对象，只有一次匹配。
print(len(elements))
print(type(elements[0]))
# 在该元素上调用getText()方法，返回该元素的文本，或内部的HTML。
print(elements[0].getText())
# 将该元素传递给str()，这将返回一个字符串，其中包含开始和结束标签，以及该元素的文本。
print(str(elements[0]))
# attrs给了我们一个字典，包含该元素的属性'id'，以及id 属性的值'author'。
print(elements[0].attrs)
print()

# 这一次，select()给我们一个列表，包含3 次匹配，我们将它保存在pElements中。
pElements = exampleSoup.select('p')
# 将该元素传递给str()，这将返回一个字符串，其中包含开始和结束标签，以及该元素的文本。
print(str(pElements[0]))
# 在该元素上调用getText()方法，返回该元素的文本，或内部的HTML。
print(pElements[0].getText())
print(pElements[1].getText())
print(pElements[2].getText())
print()

# 这里，我们使用select()来寻找所有<span>元素，然后将第一个匹配的元素保存在spanElements中。
spanElements = exampleSoup.select('span')[0]
print(str(spanElements))
# 将属性名'id'传递给get()，返回该属性的值'author'。
print(spanElements.get('id'))
# get()一个不存在的属性名，返回None。
print(spanElements.get('some_nonexistent_addr') == None)
print(spanElements.attrs)

exampleFile.close()
