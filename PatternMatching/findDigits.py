import re

digitRegex = re.compile(r'^(\d{1,3})(,\d{3})*$')
digits = ['42', '1,234', '6,368,745', '12,34,567', '1234']

for digit in digits:
    digitFound = digitRegex.search(digit)
    if digitFound != None:
        print(digitFound.group())
