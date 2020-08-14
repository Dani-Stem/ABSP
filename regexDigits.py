#here a project for regex of digits 

import re

print('Hello, please tell me what date u applied? mm-dd-yyyy:')
ish = input()
dateRegex = re.compile(r'\d\d-\d\d-\d\d\d\d')
mo = dateRegex.search(ish)
date = (mo.group())
print('ur last application date is: ' + date + ' is that correct?')