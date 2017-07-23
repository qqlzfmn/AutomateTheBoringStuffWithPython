import shelve, pprint
from myCats import cats

# cats = [{'name': 'Zophie', 'desc': 'chubby'}, {'name': 'Pooka', 'desc': 'fluffy'}]
shelfFile = shelve.open('myCats')
shelfFile['cats'] = cats
shelfFile.close()

shelfFile = shelve.open('myCats')
print(str(shelfFile['cats']))
print(str(list(shelfFile.keys())))
print(str(list(shelfFile.values())))
shelfFile.close()

print(str(pprint.pformat(cats)))
pyFile = open('myCats.py', 'w')
pyFile.write('cats = ' + pprint.pformat(cats) + '\n')
pyFile.close()
