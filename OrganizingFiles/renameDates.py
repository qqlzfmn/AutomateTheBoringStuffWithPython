#! python3
# renameDates.py - Renames filenames with American MM-DD-YYYY date format to European DD-MM-YYYY.

import shutil, os, re

# Create a regex that matches files with the American date format.
datePattern = re.compile(r"""^(.*?)          # all text before the date
                        ((0|1)?\d)-          # one or two digits for the month
                        ((0|1|2|3)?\d)-     # one or two digits for the day
                        ((19|20)\d\d)       # four digits for the year
                        (.*?)$               # all text after the date
                        """, re.VERBOSE)  # 不能包含所有情况，为了简单起见，这个正则表达式已经足够好了

# 从头阅读该正则表达式，每遇到一个左括号就计数加一，具体情况如下
"""
                    ^(1)         # all text before the date
                    (2 (3) )-    # one or two digits for the month
                    (4 (5) )-    # one or two digits for the day
                    (6 (7) )     # four digits for the year
                    (8)$         # all text after the date
"""

# Loop over the files in the working directory.
for amerFilename in os.listdir('.'):
    mo = datePattern.search(amerFilename)
    # Skip files without a date.
    if mo == None:  # amerFilename 中的文件名不匹配该正则表达式
        continue  # 跳过循环剩下的部分，转向下一个文件名

    # Get the different parts of the filename.
    beforePart = mo.group(1)  # 匹配文件名开始处、日期出现之前的任何文本
    monthPart = mo.group(2)
    dayPart = mo.group(4)
    yearPart = mo.group(6)
    afterPart = mo.group(8)  # 匹配日期之后的任何文本

    # Form the European-style filename.
    euroFilename = beforePart + dayPart + '-' + monthPart + '-' + yearPart + afterPart

    # Get the full, absolute file paths.
    absWorkingDir = os.path.abspath('.')  # 取当前工作目录的绝对路径
    amerFilename = os.path.join(absWorkingDir, amerFilename)  # 生成美国日期文件的绝对路径
    euroFilename = os.path.join(absWorkingDir, euroFilename)  # 生成欧洲日期文件的绝对路径

    # Rename the files.
    print('Renaming "%s" to "%s"...' % (amerFilename, euroFilename))  # 打印将要改名的文件以确认
    # shutil.move(amerFilename, euroFilename) # 确认完成后，进行正式改名

"""
类似程序的想法：
有很多其他的理由，导致你需要对大量的文件改名。
• 为文件名添加前缀，诸如添加spam_，将eggs.txt 改名为spam_eggs.txt。
• 将欧洲风格日期的文件改名为美国风格日期。
• 删除文件名中的0，诸如spam0042.txt。
"""
