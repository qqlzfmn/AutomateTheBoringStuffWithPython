podBayDoorStatus = 'open'
assert podBayDoorStatus == 'open', 'The pod bay doors need to be "open".'
podBayDoorStatus = 'close'
assert podBayDoorStatus == 'open', 'The pod bay doors need to be "open".'

# 这里将podBayDoorStatus 设置为 'open'，所以从此以后，我们充分期望这个变
# 量的值是 'open'。在使用这个变量的程序中，基于这个值是 'open' 的假定，我们可能
# 写下了大量的代码，即这些代码依赖于它是 'open'，才能按照期望工作。所以添加了
# 一个断言，确保假定podBayDoorStatus 是 'open' 是对的。这里，我们加入了信息 'The
# pod bay doors need to be "open".'，这样如果断言失败，就很容易看到哪里出了错。

# 稍后，假如我们犯了一个明显的错误，把另外的值赋给podBayDoorStatus，但
# 在很多行代码中，我们并没有意识到这一点。这个断言会抓住这个错误，清楚地告
# 诉我们出了什么错。

# 在日常英语中，assert 语句是说：“我断言这个条件为真，如果不为真，程序中什
# 么地方就有一个缺陷。(I assert that this condition holds true, and if not,
# there is a bug somewhere in the program.)”不像异常，代码不应该用try 和except
# 处理assert 语句。如果assert 失败，程序就应该崩溃。通过这样的快速失败，产生
# 缺陷和你第一次注意到该缺陷之间的时间就缩短了。这将减少为了寻找导致该缺陷的
# 代码，而需要检查的代码量。

# 断言针对的是程序员的错误，而不是用户的错误。对于那些可以恢复的错误（诸如
# 文件没有找到，或用户输入了无效的数据），请抛出异常，而不是用assert 语句检测它。
