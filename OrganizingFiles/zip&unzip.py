import zipfile, shutil, os

os.chdir('F:\workspace\Python\AutomateTheBoringStuffWithPython\OrganizingFiles')

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
f = open(r'.\delicious\spam.txt', 'w')
# 给 spam.txt 添加一些内容
f.write('spam\n' * (2 ** 20))
f.close()

# 压缩 delicious 文件夹，必须逐个文件（文件夹）压缩
# 'w'模式将覆盖delicious.zip文件，如果只是希望添加内容，用'a'模式
newZip = zipfile.ZipFile('delicious.zip', 'w', zipfile.ZIP_DEFLATED)
for folderName, subfolders, filenames in os.walk(r'delicious'):
    newZip.write(folderName)
    for filename in filenames:
        newZip.write(os.path.join(folderName, filename))
newZip.close()

# 删除 delicious 文件夹
shutil.rmtree(r'delicious')

# 操作 delicious.zip 压缩文件中指定文件的 ZipInfo 对象
zipFile = zipfile.ZipFile('delicious.zip')
print(zipFile.namelist())
print()
zipInfo = zipFile.getinfo('delicious/spam.txt')
print('File size of spam.txt: %.5fM' % (zipInfo.file_size / (2 ** 20)))
print('Compressed size of spam.txt: %.5fM' % (zipInfo.compress_size / (2 ** 20)))
print('Compression ratio: %.5f%%' % ((zipInfo.file_size - zipInfo.compress_size) / zipInfo.file_size * 100))

# 操作 delicious.zip 压缩文件中指定文件的 ZipFile 对象
zipFile.extractall()  # 解压到os.getcwd()文件夹
zipFile.extractall('example')  # 解压到 example 文件夹
zipFile.extract('delicious/spam.txt', 'example')  # 解压单个文件到 example 文件夹
zipFile.close()

# 遍历文件夹
print()
for folderName, subfolders, filenames in os.walk(r'example'):
    print(r'The current folder is ' + folderName)
    for subfolder in subfolders:
        print(r'SUBFOLDER OF ' + folderName + r': ' + subfolder)
    for filename in filenames:
        print(r'FILE INSIDE ' + folderName + r': ' + filename)
    print()

# 删除创建的目录和文件
shutil.rmtree(r'delicious')
shutil.rmtree(r'example')
os.remove('delicious.zip')
