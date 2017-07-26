#! python3
# deleteBigFiles.py - A program that walks through a folder tree and searches for files with big size.

import os


def deleteBigFiles(folder):
    # Walk through a folder tree and searches for files with big size.
    for folderName, subfolders, filenames in os.walk(folder):
        for filename in filenames:
            filename = os.path.join(folderName, filename)
            size = os.path.getsize(filename) / (2 ** 20)
            if size > 100:
                print('%s : %.2fM' % (filename, size))
                # os.remove(filename)
    print('Done.')


folder = input('Please input an absolute path:')
deleteBigFiles(folder)
