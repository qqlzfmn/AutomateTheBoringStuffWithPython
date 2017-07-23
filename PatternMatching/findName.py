import re

nameRegex = re.compile(r'[A-Z][a-zA-z]* Nakamoto')
names = ['Satoshi Nakamoto',
         'Alice Nakamoto',
         'RoboCop Nakamoto',
         'satoshi Nakamoto',
         'Mr.Nakamoto',
         'Nakamoto',
         'Satoshi nakamoto']

for name in names:
    nameFound = nameRegex.search(name)
    if nameFound != None:
        print(nameFound.group())