#! python3
# downloadMzitu.py - Download beauty pictures.
import requests, bs4, os

url = 'http://www.mzitu.com/hot/'  # starting url
os.makedirs('Mzitu', exist_ok=True)  # store pictures in ./Mzitu
# TODO: Find pattern
# TODO: Download all pictures
