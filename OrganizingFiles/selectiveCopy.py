#! python3
# selectiveCopy.py - A program that walks through a folder tree and searches for files with a certain
# file extension (such as .pdf or .jpg). Copy these files from whatever location they are in to a new folder.

import os, shutil


def selectiveCopy(folder, newfolder, filetype):
    # Copy files with a certain file extension to a new folder.

    folder = os.path.abspath(folder)  # make sure folder is absolute
    newfolder = os.path.abspath(newfolder)

    number = 0

    for foldername, subfolders, filenames in os.walk(folder):
        for filename in filenames:
            if filename[len(filename) - 4:] == filetype:
                shutil.copy(os.path.join(folder, filename), newfolder)
                number = number + 1
    return number


folder = input('Please input source folder:')
newfolder = input('Please input destination folder:')
filetype = input('Please input filetype(such as .pdf or .jpg):')
number = selectiveCopy(folder, newfolder, filetype)
print(str(number) + ' files has been copied.')
