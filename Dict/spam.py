spam = {'color': 'red', 'age': '42'}
for k in spam.keys():
    print k
for v in spam.values():
    print v
for i in spam.items():
    print i
print

print spam.keys()
print type(spam.keys())
print list(spam.keys())
print type(list(spam.keys()))
print spam.items()
print type(spam.items())
print

for k, v in spam.items():
    print 'Key: ' + k + '   Value: ' + v
print

print 'color' in spam
print 'color' in spam.keys()
print 'color' not in spam.values()
print 'red' in spam
print 'red' in spam.keys()
print 'red' not in spam.values()