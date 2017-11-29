def my_func(param1 = 'default'):
  '''
  THIS IS THE DOCSTRING
  '''
  print('my first python function {}'.format(param1))

my_func


def hello():
  return 'hello'

result = hello()

print(result)


def add_num(num1,num2):
  if type(num1) == type(num2) == type(10):
    return num1 + num2
  else:
    return 'Sorry, I need integers!'
  return num1 + num2

result = add_num('2','3')
print(result)