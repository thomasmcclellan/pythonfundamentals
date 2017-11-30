# Follows the LEGB rule:

# Local
# Names assigned in any way within a function (def or lambda), and not declared global in that function => don't use global key word call

# Englosing Function Locals (EFL)
# Name in the local scope of any and all enclosing functions (def or lambda), from INNER to OUTER => functions within functions (high order)

# Global
# Names assigned at the top-level of a module file, or declared global in a def within the file => at top level or using global key word

# Built-in
# Names preassigned in the built-in names module:
# Open, range, SyntaxError, LEM, etc.

# Example 1
x = 25

def my_func():
  x = 50
  return x

print(x) #25 => global (top level)
print(my_func()) #50 local 
my_func() #Calls function, but doesn't actually print 50
print(x) #25 => not affected by function so defaults to global (top level) again

# Example 2
# Local
lambda x: x**2

# EFL
name = 'George'

def greet():
  name = 'Sammy'

  def hello():
    print('Hello ' + name) #Looks for name and finds it on line35
  
  hello() #Calls hello function

greet() #'Hello Sammy' => follows path from inner-most, out
print(name) #'George' => prints globally

# Built-in
# There are functions that are already defined within Python (like len)
# NEVER define len = 25 or something because it means you can't use len as it's usual form

# Example 3
x = 50 

def func(x):
  print('x is: ',x) #Calling existing x (global)
  x = 1000 #x newly defined locally
  print('local x changed to: ',x) #Calling local x (work in => out)

func(x) #Calling function => 1000
print(x) #In global namespace => 50

# Example 4
# Changing a value GLOBALLY
x = 50

def global_func():
  global x #Don't use global keyword unless have to => but it allows you to reach out to global context
  x = 1000

print('Before function call, x is: ',x) #50
global_func()
print('After function call, x is: ',x) #1000

# OR (and better)
x = 50

def global_func():
  x = 1000
  return x #Has same effect as global keyword but doesn't risk accidently redefining anything in the global space

print('Before function call, x is: ',x) #50
x = global_func()
print('After function call, x is: ',x) #1000