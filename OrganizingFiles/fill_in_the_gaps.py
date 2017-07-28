#! python3
# fill_in_the_gaps.py - A program that finds all files with a given prefix, such as spam001.txt, spam002.txt,
# and so on, in a single folder and locates any gaps in the numbering (such as if there is a spam001.txt and
# spam003.txt but no spam002.txt). The program rename all the later files to close this gap.

import os, re, shutil

namePattern = re.compile(r'^(spam)(\d+)(\.txt)$')  # 可以匹配 spam 开头 .txt 结尾，中间有任意位数字的文件名


def fill(folder):
    lst = []  # 用于存放 ( 去掉 0 的整数类型编号, 字符串类型文件名, 未去掉 0 时编号的整型长度 ) 的元组
    for file in os.listdir(folder):  # 遍历指定目录下所有文件，返回值是一个文件名的列表
        num = namePattern.search(file).group(2)  # 提取文件名中的数字部分
        lst.append((int(num.lstrip('0')), file, len(num)))  # 将元组添加到列表的末尾

    # 排序有两种方法，lst.sort() 和 lst = sorted(lst)：sort()是在原位重新排列列表，而sorted()是产生一个新的列表。
    lst.sort()  # 排序 lst 列表
    for index in range(len(lst)):  # 用 lst 列表的长度（也就是符合条件的文件个数）进行索引
        padding = lst[index][2]  # 用 len(num) 作为填充 '0' 之后的数字部分长度
        num = str(int(index) + 1)  # 新的文件编号
        padded_num = num.rjust(padding, '0')  # 格式化后的文件编号
        src = os.path.join(folder, lst[index][1])  # 源文件绝对路径
        dst = os.path.join(folder, namePattern.sub(r'\g<1>%s\g<3>' % padded_num, lst[index][1]))  # 目标文件绝对路径
        shutil.move(src, dst)  # 重命名
        print(os.path.relpath(src) + ' --> ' + os.path.relpath(dst))  # 打印出更名了的文件
        # 这里我们发现这种算法每次运行都会按照排序后的位置从 1 开始重命名所有文件，增加了磁盘读写的负担，但是简化了迭代次数
    return


folder = input('Please input an absolute path:')
fill(folder)
print('Done!')
