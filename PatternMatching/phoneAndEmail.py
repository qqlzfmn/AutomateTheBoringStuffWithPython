#! python3
# phoneAndEmail.py - Finds phone numbers and email addresses on the clipboard.

import pyperclip, re

# Create phone regex.
phoneRegex = re.compile(r'''(
            (\d{3}|\(\d{3}\))?               # 区号
            (\s|-|\.)?                       # 分隔符
            (\d{3})                           # 前三位数
            (\s|-|\.)                        # 分隔符
            (\d{4})                           # 后四位数
            (\s*(ext|x|ext.)(\s*\d{2,5}))?  # 分机号
            )''', re.VERBOSE)

# Create email regex.
emailRegex = re.compile(r'''(
            [a-zA-Z0-9._%+-]+               # 用户名
            @                                 # @ 符号
            [a-zA-Z0-9.-]+                  # 一级域名
            (\.[a-zA-Z]{2,4})                # 顶级域名
            )''', re.VERBOSE)

# Find matches in clipboard text.
text = str(pyperclip.paste())
matches = []
# print(phoneRegex.findall(text))
for groups in phoneRegex.findall(text):
    if groups[1] == '':
        phoneNum = '    ' + '-'.join([groups[3], groups[5]])
    elif not groups[1].isnumeric():
        phoneNum = '-'.join([groups[1][1:4], groups[3], groups[5]])
    else:
        phoneNum = '-'.join([groups[1], groups[3], groups[5]])
    if groups[8] != '':
        phoneNum += ' ext' + groups[8]
    matches.append(phoneNum)
for groups in emailRegex.findall(text):
    matches.append(groups[0])

# Copy resaults to the clipboard.
if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print('Copied to clipboard:')
    print('\n'.join(matches))
else:
    print('No phone numbers or email addresses found.')
