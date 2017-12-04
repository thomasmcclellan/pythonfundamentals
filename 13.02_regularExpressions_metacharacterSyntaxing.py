# Meta Character Syntaxing

import re

def multi_re_find(patterns,phrase):

  for pat in patterns:
    print('Searching for pattern {}'.format(pat))
    print(re.findall(pat,phrase))
    print('\n')


test_phrase = 'sdsd..sssddd..sdddsddd...dds...dsssss...sddddd'

test_patterns = ['sd*'] #Searching for s, followed by 0 or more 'd's => * attached to d
test_patterns = ['sd+'] #Searching for one or more d's
test_patterns = ['sd?'] #Searching for 0 or 1 d
test_patterns = ['sd{3}'] #Searching for 3 d's
test_patterns = ['sd{2,4}'] #Searching for 2 to 4 d's
test_patterns = ['s[sd]+'] #Searching for s, followed by one or more s's or d's


test_phrase = 'This is a string!  Notice, it has punctuation.  But, how can we remove it?'

test_patterns = ['[^!.,?]+'] #Searching to omit (^) !,.,,,or ? one or more times
test_patterns = ['[a-z]+'] #Searching for sequence of lower-case letters
test_patterns = ['[A-Z]+'] #Searching for sequence of upper-case letters


test_phrase = 'This is a string with numbers 123456789 and a symbol #hashtag'

test_patterns = [r'\d+'] #Searching for digits (numbers) only
test_patterns = [r'\D+'] #Searching for non-digits
test_patterns = [r'\s+'] #Searching for whitespace
test_patterns = [r'\S+'] #Searching for non-whitespace
test_patterns = [r'\w+'] #Searching for alpha-numerics
test_patterns = [r'\W+'] #Searching for non-alpha-numberics


multi_re_find(test_patterns,test_phrase)