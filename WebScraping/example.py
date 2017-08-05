import bs4

exampleFile = open('example.html')
exampleSoup = bs4.BeautifulSoup(exampleFile, "html.parser")
print('type of exampleSoup = bs4.BeautifulSoup(open(\'example.html\')) is %s' % type(exampleSoup))
elements = exampleSoup.select('#author')
print('type of elements = exampleSoup.select(\'#author\') is %s' % type(elements))
print('length of elements is %s' % len(elements))
print('type of elements[0] is %s' % type(elements[0]))
print('text of elements[0] is %s' % elements[0].getText())
print('str(elements[0]) = %s' % str(elements[0]))
print('attributes of elements[0] is %s' % elements[0].attrs)
exampleFile.close()
