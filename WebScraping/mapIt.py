#! python3
# mapIt.py - Launches a map in the browser using an address from the command line or clipboard.

import webbrowser, sys, pyperclip

if len(sys.argv) > 1:
    # Get address from commend line
    address = ' '.join(sys.argv[1:])
else:
    # Get address from clipboard.
    address = pyperclip.paste()
webbrowser.open('http://www.google.cn/maps/place/' + address)

'''
天津市宝坻区东环路宝鑫景苑
天津科技大学学生第一公寓
870 Valencia St, San Francisco, CA 94110
'''
