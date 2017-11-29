# For loops
seq = [1,2,3,4,5,6]

for item in seq:
  # Code here
  print(item)

d = {'Sam':1, 'Frank':2, 'Dan':3}

for dictionary in d:
  print(dictionary) #Sam Frank Dan
  print(d[dictionary]) #Sam 1 Frank 2 Dan 

# While loops
i = 1

while i < 5: 
  print('i is: {}'.format(i))
  i += 1