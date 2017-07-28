import logging

logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')
# debug() 函数将调用basicConfig()，打印一行信息。格式是在 basicConfig()函数中指定的，并且包括传递给 debug() 的消息。
logging.debug('Start of program')


# 不要用print()调试!

# 在调试完成后，你需要花很多时间，从代码中清除每条日志消息的print() 调用。
# 你甚至有可能不小心删除一些print() 调用，而它们不是用来产生日志消息的。
# 日志消息的好处在于，你可以随心所欲地在程序中想加多少就加多少，稍后只要
# 加入一次logging.disable（logging.CRITICAL）调用，就可以禁止日志。
# 不像print()，logging 模块使得显示和隐藏日志信息之间的切换变得很容易。

# 日志消息是给程序员的，不是给用户的。用户不会因为你便于调试，而想看到
# 字典值的内容。请将日志信息用于类似这样的目的。对于用户希望看到的消息，
# 例如“文件未找到”或者“无效的输入，请输入一个数字”，应该使用print() 调用。
# 我们不希望禁用日志消息之后，让用户看不到有用的信息。


def factorial(n):
    logging.debug('Start of factorial(%d)' % (n))
    total = 1
    for i in range(1, n + 1):
        total *= i
        logging.debug('i is ' + str(i) + ', total is ' + str(total))
    logging.debug('End of factorial(%d)' % (n))
    return total


print(factorial(5))
logging.debug('End of program')
