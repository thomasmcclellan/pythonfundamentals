# Review of 01-07

############
# Problem 1
############

# Given: 
s = 'django'

# Use indexing to print out the following:
# 'd'
s[0]

# 'o'
s[-1]

# 'djan'
s[:4]

# 'jan'
s[1:4]

# 'go'
s[4:]

# Reverse string
s[::-1]

############
# Problem 2
############

# Given:
l = [3,7,[1,4,'hello']]

# Reassign 'hello' to 'goodbye'
1[2][2] = 'goodbye'

############
# Problem 3
############

# Using keys and indexing, grab 'hello' from the following dictionaries:

d1 = {'simple_key':'hello'}
d1['simple_key']

d2 = {'k1':{'k2':'hello'}}
d2['k1']['k2']

d3 = {'k1':[{'nest_key':['this is deep', ['hello']]}]}
d3['k1'][0]['nest_key'][1][0] #If didn't have last 0, would return the list, not just 'hello'

############
# Problem 4
############

# Use a set to find the unique values of list below:
my_list = [1,1,1,1,1,2,2,2,2,3,3,3,3]

set(my_list)

############
# Problem 5
############

# Given:
age = 4
name = 'Sammy'

# Use print formatting to print the following string:
"Hello my dog's name is Sammy and he is 4 years old"

print("Hellow my name dog's name is {a} and he is {b} years old.".format(a=age, b=name))