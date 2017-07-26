#! python3
# fill_in_the_gaps.py - A program that finds all files with a given prefix, such as spam001.txt, spam002.txt,
# and so on, in a single folder and locates any gaps in the numbering (such as if there is a spam001.txt and
# spam003.txt but no spam002.txt). The program rename all the later files to close this gap.

import os, re, shutil

namePattern = re.compile(r'(spam)(%d){3}(\.txt)')


def fill(folder):
    # TODO: Rewrite all!
    # files = []
    # for folderName, subfolders, filenames in os.walk(folder):
    #     for filename in filenames:
    #         if re.match(namePattern, filename) != None:
    #             files.append(filename)
    # files.sort()
    # maxFileNum = int(files[len(files) - 1][4 : 6])
    # for i in range(1 , maxFileNum + 1):
    #     if i == int(files[i - 1][4 : 6]):
    #         continue
    #     else:
    #         for j in range(i, maxFileNum + 1):
    #             shutil.move()
    #
    return


folder = input('Please input an absolute path:')
fill(folder)
print('Done!')
