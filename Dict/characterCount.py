# -*- coding: utf-8 -*-
import pprint
message = 'It was a bright cold day in April, and the clocks were striking thirteen.'
count = {}
for character in message:
    count.setdefault(character, 0)
    count[character] = count[character] + 1
pprint.pprint(count)

'''
prettyprint 模块有 pprint.pprint()和pprint.pformat()方法
pprint()用于打印
pformat()用于转换为格式化的字符串
pprint.pprint(count)等价于print(pformat(count))
'''