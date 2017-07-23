import os

os.chdir('F:\各种资料\课外\Python\书')
os.mkdir('.\\test')
os.rmdir('.\\test')
path = os.getcwd()
print('Change current working directory(CWD) to ' + path)
relpath = os.path.relpath('F:\workspace\Python\AutomateTheBoringStuffWithPython\Files')
abspath = os.path.abspath(relpath)
print('The relative path of ' + abspath + ' to CWD is: ' + relpath)
print('relpath is absolutely path? ' + str(os.path.isabs(relpath)))
print('abspath is absolutely path? ' + str(os.path.isabs(abspath)))
file = path + '\\Python科学计算.pdf'
filePath, fileName = os.path.split(file)
fullPath = file.split(os.path.sep)
print('os.path.split: ' + str(os.path.split(file)))
print('String.split: ' + str(fullPath) + ' with sep: ' + os.path.sep)
books = os.listdir(path)
size = 0
for book in books:
    size = size + os.path.getsize(os.path.join(path, book))
size = size / (2 ** 20)  # change Bytr to MB
print('Size of all my books: ' + str(size).split('.')[0] + 'MB')
print('Does ' + path + ' exists? ' + str(os.path.exists(path)))
print('Is ' + path + ' a dir? ' + str(os.path.isdir(path)))
print('Is ' + path + ' a file? ' + str(os.path.isfile(path)))
print('Is ' + file + ' a file? ' + str(os.path.isfile(file)))
print('Test if a USB driver exists: ' + str(os.path.exists('I:\\')))
