#! python3
# madLibs.py - a phrasal template word game.

import os

os.chdir('F:\workspace\Python\AutomateTheBoringStuffWithPython\Files')

fileIn = open('madlibs.txt')
fileOut = open('madlibs_out.txt', 'w')
line = fileIn.read()
# 把文件内容打开成单词
words = line.split(' ')
replaceLine = ''
for word in words:
    # 判断 word 是否大于一个字符，且全是大写（可以排除句首的'A'），满足条件则替换成输入的单词
    if len(word) > 1 and word.isupper():
        # 判断是元音还是辅音开头以确定用'a'还是'an'
        if word[0] in ['A', 'E', 'I', 'O', 'U']:
            print('Enter an ' + word.lower() + ':')
        else:
            print('Enter a ' + word.lower() + ':')
        replaceWord = input()
        # 句子末尾的特殊情况
        if word[len(word) - 1] == '.':
            replaceLine = replaceLine + replaceWord + '.'
        else:
            replaceLine = replaceLine + replaceWord + ' '
    # 不满足条件，保持不变
    else:
        replaceLine = replaceLine + word + ' '
print(replaceLine)
fileOut.write(replaceLine)
fileIn.close()
fileOut.close()
