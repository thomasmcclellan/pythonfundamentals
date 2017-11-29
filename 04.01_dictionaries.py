# Python's version of objects
# They do not retain order! => They only have key-value pairing

my_stuff = {'key1': 'value1', 'key2': 'value2', 'key3': {'stuff': [1,2,'THIS ONE']}}
print(my_stuff) #Notice, NO ORDER!

x = my_stuff['key3']['stuff'][2].lower()
print(x)

food = {'lunch': 'pizza', 'breakfast': 'eggs'}
food['lunch'] = 'burger'
print(food['lunch'])
food['dinner'] = 'pasta'
print(food)
