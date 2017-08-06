#! python3
# lucky.py - Opens several Google search results.
import requests, sys, webbrowser, bs4

print('Baiduing…')  # display text while downloading the Google page
res = requests.get('https://www.baidu.com/baidu?&ie=utf-8&word=' + ' '.join(sys.argv[1:]))
res.raise_for_status()
# TODO: Retrieve top search result links.
# TODO: Open a browser tab for each result.
