#! python3
# mcb.pyw - Saves and loads pieces of text to the clipboard.
# Usage: py mcb.pyw save <keyword> - Saves clipboard to keyword.
#        py mcb.pyw <keyword> - Loads keyword to clipboard.
#        py mcb.pyw list - Loads all keywords to clipboard.
#        py mcb.pyw del <saved keyword> - Delete saved keyword.
#        py mcb.pyw del - Delete all saved keywords.

import shelve, pyperclip, sys

# shelve - Manage shelves of pickled objects.
# To summarize the interface (key is a string, data is an arbitrary object):
#
#         import shelve
#         d = shelve.open(filename) # open, with (g)dbm filename -- no suffix
#
#         d[key] = data   # store data at key (overwrites old data if
#                         # using an existing key)
#         data = d[key]   # retrieve a COPY of the data at key (raise
#                         # KeyError if no such key) -- NOTE that this
#                         # access returns a *copy* of the entry!
#         del d[key]      # delete data stored at key (raises KeyError
#                         # if no such key)
#         flag = key in d # true if the key exists
#         list = d.keys() # a list of all existing keys (slow!)
#
#         d.close()       # close it

mcbShelf = shelve.open('mcb')

# Save clipboard content.
# sys.argv[] 是用来获取命令行参数的，sys.argv[0] 表示代码本身文件路径，所以参数从 1 开始
# len(sys.argv) == 3 的意思是命令行有两个参数，且第一个参数为「save」忽略大小写
# 例如命令行格式为「py mcb.pyw save quiz」命令是「mcb.pyw」，参数一sys.argv[1] = save，参数二sys.argv[2] = quiz
if len(sys.argv) == 3 and sys.argv[1].lower() == 'save':
    # mcbShelf[quiz] = 'We'll have a quiz at the end of the show.'
    mcbShelf[sys.argv[2]] = pyperclip.paste()

if len(sys.argv) == 3 and sys.argv[1].lower() == 'del' and (sys.argv[2] in mcbShelf):
    del mcbShelf[sys.argv[2]]

# 一个参数的命令，如果参数为「list」输出所有 mcbShelf 的 key 到 clipboard
# 如果参数为 mcbShelf 中的一个 key，输出对应的 value 到 clipboard
elif len(sys.argv) == 2:
    # List keywords and load content.
    if sys.argv[1].lower() == 'list':
        pyperclip.copy(str(list(mcbShelf.keys())))
    elif sys.argv[1].lower() == 'del':
        for k in mcbShelf.keys():
            del mcbShelf[k]
    elif sys.argv[1] in mcbShelf:
        pyperclip.copy(mcbShelf[sys.argv[1]])
mcbShelf.close()