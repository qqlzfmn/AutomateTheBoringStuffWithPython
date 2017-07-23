# -*- coding: utf-8 -*-
from __future__ import print_function
birthdays = {'Alice': 'Apr 1', 'Bob': 'Dec 12', 'Carol': 'Mar 4'}
while True:
    name = raw_input('Enter a name(blank to quit):')

    '''
    错误信息：
    D:\Python27\python.exe F:/workspace/Python/Dict/birthday.py
    Enter a name(blank to quit):Bob
    Traceback (most recent call last):
      File "F:/workspace/Python/Dict/birthday.py", line 4, in <module>
        name = input('Enter a name(blank to quit):')
      File "<string>", line 1, in <module>
    NameError: name 'Bob' is not defined
    
    Process finished with exit code 1
    
    问题原因：
    raw_input更符合用户输入的习惯，把任何用户输入都转换成字符串存储，在需要其它类型的数据时，调用相应的函数进行转换
    input用户输入什么就存储什么，所以用户输入必须符合Python语法要求，否则会出错
    
    解决办法：
    用input():输入字符串时要带引号
    或直接用raw_input()函数，输入字符串时就可以直接输入了
    '''

    if name == '':
        break
    if name in birthdays:
        print(birthdays[name] + ' is the birthday of ' + name)
    else:
        print('I do not konw ' + name + '\'s birthday, ', end = '')
        birthdays[name] = raw_input('please tell me:')
        print('Birthday of ' + name + ' has rememberd')
exit()