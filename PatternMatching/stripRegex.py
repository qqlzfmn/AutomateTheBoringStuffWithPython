import re


def stripRegex(str, char=' '):
    # re.compile()的参数本质上是一个字符串，所以可以用字符串拼接的方式写
    # 要提取出中间的字符串，就需要变成非贪心模式，否则将会匹配后续的分割字符
    regex = re.compile(r'^[' + char + r']*(.+?)[' + char + r']*$')
    return regex.search(str).group(1)


print(stripRegex('   fnewuih564asui       '))
print(stripRegex('--------------   fnewuih564asui       ----------', '-'))
