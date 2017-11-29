# Immutable sequences
t = (1,2,3)
print(t[0])


t = ('a', True, 123)
print(t)

t[0] = 'NEW' #Error => cannot change data

# If changed to a list, it can change
list = ['a', True, 123]
print(list)

list[0] = 'NEW' #Works!
print(list)