import shutil, os
from send2trash import send2trash

os.chdir('F:\workspace\Python\AutomateTheBoringStuffWithPython\OrganizingFiles')


try:
    os.mkdir('delicious')
except FileExistsError:
    pass
f = open('spam.txt', 'w')
f.close()
f = open('eggs.txt', 'w')
f.close()
# 如果文件存在，会被直接覆盖掉，不返回FileExistsError，最好在执行命令前先判断文件是否存在，让用户自己判断是否复制
print(shutil.copy('spam.txt', '.\\delicious'))
print(shutil.copy('eggs.txt', '.\\delicious\\eggs2.txt'))
os.remove('spam.txt')
print('Destination file \'.\\spam.txt\' has been removed.')
os.remove('eggs.txt')
print('Destination file \'.\\eggs.txt\' has been removed.')
print()

try:
    os.mkdir('bacon')
except FileExistsError:
    pass
try:
    # 当文件已存在时，无法创建该文件。返回FileExistsError
    print(shutil.copytree('.\\bacon', '.\\bacon_backup'))
except FileExistsError:
    print('Destination path \'.\\' + os.path.relpath('.\\bacon_backup\' already exists'))
    print()


try:
    os.mkdir('eggs')
except FileExistsError:
    pass
f = open('bacon.txt', 'w')
f.close()
try:
    # 如果存在目录eggs，则移动bacon.txt到eggs目录；如果不存在目录eggs，则移动bacon.txt到eggs文件，即将bacon.txt改名为eggs
    # 如果目录eggs中已存在bacon.txt文件，则抛出shutil.Error异常
    # 一般此命令都是要将文件移动到目录，所以在移动前最好判断目录是否存在
    print(shutil.move('bacon.txt', 'eggs'))
except shutil.Error:
    print('Destination path \'.\\eggs\\bacon.txt\' already exists')
# 移动bacon.txt到eggs目录并更名为new_bacon.txt
f = open('bacon.txt', 'w')
f.close()
print(shutil.move('bacon.txt', '.\\eggs\\new_bacon.txt'))
try:
    # 如果目录不存在，也会抛出异常
    print(shutil.move('spam.txt', '.\\does_not_exist\\eggs\\new_spam.txt'))
except FileNotFoundError:
    print('Destination path \'.\\does_not_exist\\eggs\' does not exist.')
    print()


shutil.rmtree('delicious')
print('Destination path \'.\\delicious\' has been removed.')
shutil.rmtree('bacon')
print('Destination path \'.\\bacon\' has been removed.')
shutil.rmtree('bacon_backup')
print('Destination path \'.\\bacon_backup\' has been removed.')


# send2trash.send2trash()可以在任何操作系统把文件或文件夹发送到回收站（垃圾桶）
send2trash('eggs')
print('Destination path \'.\\eggs\' has been send to trash bin.')