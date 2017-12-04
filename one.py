def func():
  print('Func() in one.py')

print('TOP LEVEL ONE.PY')

if __name__ == '__main__':
  print('One.py is being run directly')
else:
  print('One.py has been imported')