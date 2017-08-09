#! python3
# downloadXkcd.py - Downloads every single XKCD comic.
import requests, os, bs4, re

url = 'https://xkcd.com'  # starting url
os.makedirs('xkcd', exist_ok=True)  # store comics in ./xkcd
comicUrlPattern = re.compile('http.+png')
while not url.endswith('#'):
    # Download the page.
    print('Downloading page %s…' % url)
    try:
        res = requests.get(url)
        res.raise_for_status()
    except Exception as e:
        print(e)
    soup = bs4.BeautifulSoup(res.text, "html.parser")
    # Find the URL of the comic image.
    comicElems = soup.select('#middleContainer')
    for comicElem in comicElems:
        try:
            comicUrl = comicUrlPattern.findall(comicElem.findAll(text=re.compile("http"))[1])[0]
        except Exception as e:
            print(e)
    # Download the image.
    print('Downloading image %s…' % comicUrl)
    try:
        res = requests.get(comicUrl)
        res.raise_for_status()
    except Exception as e:
        print(e)
    # Save the image to ./xkcd.
    imageFile = open(os.path.join('xkcd', os.path.basename(comicUrl)), 'wb')
    for chunk in res.iter_content(100000):
        imageFile.write(chunk)
    imageFile.close()
    # Get the Prev button's url.
    prevLink = soup.select('a[rel="prev"]')[0]
    url = 'http://xkcd.com' + prevLink.get('href')
print('Done.')
