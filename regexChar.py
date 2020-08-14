#here a project for regex of digits
import re

text = input('say something: ').lower()
funnyRegex = re.compile(r'(ha)*')
mo = funnyRegex.search(text)
funny = (mo.group()) 
if funny != '':
    print('what is funny?')
else:
    print('ok then..')




