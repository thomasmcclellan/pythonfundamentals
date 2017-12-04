# Decorators can be thought of as functions that modify the functionality of other functions => make them shorter and more pythonic

# s = 'GLOBAL VARIABLE'
# def func():
#   mylocal = 10
#   print(locals())
#   print(globals()['s'])

# func() 

# def hello(name = 'Tom'):
#   return 'hello ' + name

# print(hello())

# mynewgreet = hello

# (print(mynewgreet()))

# def hello(name = 'Tom'):
#   print('THE HELLO() FUNCTION HAS RUN')

#   def greet():
#     return 'THIS STRING IS INSIDE GREET()'

#   def welcome():
#     return 'THIS STRING IS INSIDE WELCOME()'
  
#   print(greet())
#   print(welcome())
#   print('End of hello()')

# welcome() #Not defined because welcome() only local


# def hello(name = 'Tom'):
#   print('THE HELLO() FUNCTION HAS RUN')

#   def greet():
#     return 'THIS STRING IS INSIDE GREET()'

#   def welcome():
#     return 'THIS STRING IS INSIDE WELCOME()'
  
#   if name == 'Tom':
#     return greet
#   else:
#     return welcome

# x = hello()

# print(x())


# def hello():
#   return 'Hi Tom'

# def other(func):
#   print('Hello')
#   print(func())

# other(hello)


def new_decorator(func):

  def wrap_func():
    print('CODE HERE BEFORE EXECUTING FUNC')
    func()
    print('FUNC() HAS BEEN CALLED')
  
  return wrap_func

@new_decorator #This is accomplishing the same thing as line78
def func_needs_decorator():
  print('THIS FUNCTION IS IN NEED OF A DECORATOR')

# func_needs_decorator = new_decorator(func_needs_decorator)

func_needs_decorator()
