import os, shutil

# os.chdir('F:\workspace\Python\AutomateTheBoringStuffWithPython\OrganizingFiles')

# 创建如图 tree.jpg 的目录关系
for i in [r'delicious', r'delicious\cats',
          r'delicious\walnut', r'delicious\walnut\waffles']:
    try:
        os.mkdir(i)
    except FileExistsError:
        pass
for i in [r'.\delicious\cats\catnames.txt', r'.\delicious\cats\zophie.jpg',
          r'.\delicious\walnut\waffles\butter.txt', r'.\delicious\spam.txt']:
    f = open(i, 'w')
    f.close()

# 遍历文件夹，os.walk() 的返回值有三个，分别是当前文件夹名、子文件夹名、子文件名
for folderName, subfolders, filenames in os.walk(r'delicious'):
    print(r'The current folder is ' + folderName)
    for subfolder in subfolders:
        print(r'SUBFOLDER OF ' + folderName + r': ' + subfolder)
    for filename in filenames:
        print(r'FILE INSIDE ' + folderName + r': ' + filename)
    print()

shutil.rmtree(r'delicious')
