spam = ['apples', 'bananas', 'tofu', 'cats']
def comma(spam):
    spam[-1] = 'and ' + spam[-1]
    string = spam[0]
    for i in spam[1:]:
        string = string + ', ' + i
    return string
print comma(spam)
exit()