# Wont always need a full-blown function
# There are times when you need a function only one time

# Filter function
my_list = [1,2,3,4,5,6,7,8]
def even_bool(num):
  return num % 2 == 0

evens = filter(even_bool, my_list)
print(list(evens))

# Now with lambda expression...
my_list = [1,2,3,4,5,6,7,8]

evens = filter(lambda num:num % 2 == 0, my_list)
print(list(evens))