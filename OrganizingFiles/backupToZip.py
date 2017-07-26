#! python3
# backupToZip.py - Copies an entire folder and its contents into a ZIP file whose filename increments.

import zipfile, os


def backupToZip(folder):
    # Backup the entire contents of "folder" into a ZIP file.

    folder = os.path.abspath(folder)  # make sure folder is absolute

    # Figure out the filename this code should use based on
    # what files already exist.
    number = 1
    while True:
        # 如果要备份的文件夹是C:\delicious，ZIP 文件的名称就应该是C:\delicious_N.zip
        zipFilename = os.path.basename(folder) + '_' + str(number) + '.zip'
        if not os.path.exists(zipFilename):
            break
        number = number + 1

    # Create the ZIP file.
    print('Creating %s…' % (zipFilename))
    backupZip = zipfile.ZipFile(zipFilename, 'w')

    # Walk the entire folder tree and compress the files in each folder.
    for foldername, subfolders, filenames in os.walk(folder):
        print('Adding files in %s…' % (foldername))
        # Add the current folder to the ZIP file.
        backupZip.write(foldername)
        # Add all the files in this folder to the ZIP file.
        for filename in filenames:
            # os.path.basename(path) 返回path最后的文件名。如果path以/或\结尾，那么就会返回空值。
            # 在本程序中为os.path.basename('C:\\delicious')，运行结果是'delicious'，newBase = 'delicious_'
            newBase = os.path.basename(folder) + '_'
            if filename.startswith(newBase) and filename.endswith('.zip'):
                continue  # don't backup the backup ZIP files
            backupZip.write(os.path.join(foldername, filename))
    backupZip.close()
    print('Done.')


# 程序运行时所在位置即为os.getcwd()，所以本程序在哪执行就会将C:\\delicious备份到哪
backupToZip('C:\\delicious')

'''
类似程序的想法：
你可以在其他程序中遍历一个目录树，将文件添加到压缩的ZIP 归档文件中。
例如，你可以编程做下面的事情：
• 遍历一个目录树，将特定扩展名的文件归档，诸如.txt 或.py，并排除其他文件。
• 遍历一个目录树，将除.txt 和.py 文件以外的其他文件归档。
• 在一个目录树中查找文件夹，它包含的文件数最多，或者使用的磁盘空间最大。
'''
