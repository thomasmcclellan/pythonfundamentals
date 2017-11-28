# Strings hold text info and hold "" or ''
# Can have []

'hello'
"hello"
"I'm a dog"

my_string = 'abcdefg'
print(my_string)
print(my_string[0])
print(my_string[3:])
print(my_string[:3]) #Goes up to, BUT NOT INCLUDING the number
print(my_string[2:5])
print(my_string[::])
print(my_string[::2]) #The number is the step size (goes up by two)

# Strings are IMMUTIBLE 

x = my_string.upper()
print(x)

y = my_string.lower()
print(y)

z = my_string.capitalize()
print(z)

two_words = 'Hello world'
t = two_words.split()
print(t)