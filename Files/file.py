import os

os.chdir('F:\workspace\Python\AutomateTheBoringStuffWithPython\Files')

file = open('hello.txt')  # 执行完open()函数，文件即写入内存，用其他方式改写文件，再去read()，读到的是未改写的内容
text = file.read()  # 每当执行完read()方法，file虽然还是一个File对象，但是里边的内容已经没有了，需要重新open()
print(text)
file.close()

print()

file = open('hello.txt', 'r')  # open(file, mode='r') 默认打开文件方式为只读，参数可省略
lines = file.readlines()
for line in lines:
    print(line, end='')
file.close()

# 写入模式可以选择不存在的路径，而只读模式只能选择存在的路径
file = open('halo.txt', 'w')  # 参数'w'打开文件为写入模式，覆盖写入
file.write('五百年后，小娜会和士官长在光晕游戏中大战外星人。')
file.close()

file = open('hallo.txt', 'a')  # 参数'a'打开文件为添加模式，添加写入
file.write('这个程序运行了一次。\n')  # 末尾不自带换行，需自己写入
file.close()
