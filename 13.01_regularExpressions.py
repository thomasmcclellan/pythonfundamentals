# Regular expressions allow to search for patterns in python strings

import re #re = regular expressions

patterns = ['term1', 'term2']

text = 'This is a string with term1, but not the other'

for pattern in patterns:
  print('I am searching for: ' + pattern)

  if re.search(pattern,text):
    print('MATCH')
  else:
    print('NO MATCH')


print(re.findall('match','test phrase match in middle'))

