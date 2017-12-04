# Errors and Exceptions
# Three keywords: try, except, finally
# With these, we can dictate our code logic in case of an error

try: 
  f = open('simple.txt', 'r') # w = write; r = read only
  f.write('Test write to simple text')
except IOError: #Looks for this specific error => if you don't know the specific error, just write 'except' with no error listed
  print('ERROR: COULD NOT FIND FILE OR READ DATA')
else:
  print('SUCCESS!')
  f.close()

try: 
  f = open('simple.txt', 'r')
  f.write('Test write to simple text')
except: 
  print('ERROR: COULD NOT FIND FILE OR READ DATA')
finally: #Works even if there is an error
  print('I ALWAYS WORK NO MATTER WHAT')