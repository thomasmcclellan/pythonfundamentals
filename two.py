import one
print('TOP LEVEL TWO.PY')
one.func()

if __name__ == '__main__':
  print('Two.py being run directly')
else:
  print('Two.py has been imported')