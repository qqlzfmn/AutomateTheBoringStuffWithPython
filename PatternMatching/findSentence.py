import re

sentenceRegex = re.compile(r'(Alice|Bob|Carol) (eats|pets|throws) (apples|cats|baseballs)\.',re.IGNORECASE)
sentences = ['Alice eats apples.',
             'Bob pets cats.',
             'Carol throws baseballs.',
             'Alice throws Apples.',
             'BOB EATS CATS.',
             'Robocop eats apples.',
             'ALICE THROWS FOOTBALLS.',
             'Carol eats 7 cats.']

for sentence in sentences:
    sentenceFound = sentenceRegex.search(sentence)
    if sentenceFound != None:
        print(sentenceFound.group())