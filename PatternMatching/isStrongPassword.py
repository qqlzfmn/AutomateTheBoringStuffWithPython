import re


def isStrongPassword(passWord):
    strongPasswordRegex1 = re.compile(r'.{8,}')     # 至少8个字符
    strongPasswordRegex2 = re.compile(r'[a-z]+')    # 至少1个小写字符
    strongPasswordRegex3 = re.compile(r'[A-Z]+')    # 至少1个大写字符
    strongPasswordRegex4 = re.compile(r'\d+')       # 至少1位数字

    if strongPasswordRegex1.search(passWord) != None and \
                    strongPasswordRegex2.search(passWord) != None and \
                    strongPasswordRegex3.search(passWord) != None and \
                    strongPasswordRegex4.search(passWord) != None:
        return True
    else:
        return False


password = 'Lmj521+~'
print(isStrongPassword(password))
