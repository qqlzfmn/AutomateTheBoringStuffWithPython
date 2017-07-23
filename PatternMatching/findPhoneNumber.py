import re

message = 'Call me at 415-555-1011 tomorrow. 415-555-9999 is my office.'
message2 = 'Call me at (415)555-1011 tomorrow. (415)555-9999 is my office.'
phoneNumRegex = re.compile(r'\d{3}-\d{3}-\d{4}')
phoneRegex = re.compile(r'''(
            (\d{3}|\(\d{3}\))?               # 区号
            (\s|-|\.)?                       # 分隔符
            \d{3}                             # 前三位数
            (\s|-|\.)                        # 分隔符
            \d{4}                             # 后四位数
            (\s*(ext|x|ext.) \s*\d{2,5})?   # 分机号
            )''',re.VERBOSE)
mo = phoneNumRegex.findall(message)
mo2 = phoneRegex.findall(message2)
print(phoneNumRegex,mo,mo2)
# mo 输出
if mo != []:
    for i in mo:
        print('Phone number found:' + i)
else:
    print('None phone number found.')
print('Done!')
# mo2 输出
if mo2 != []:
    for i in mo2:
        print('Phone number found:' + i[0])
else:
    print('None phone number found.')
print('Done!')