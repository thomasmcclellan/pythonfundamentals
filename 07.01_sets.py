# Unordered collections of unique elements
x = set()

x.add(1)
x.add(2)
x.add(4)
x.add(0.1)
x.add(4) #It is only going to add 4 once => only takes in UNIQUE elements; if it repeats, it disregards it
print(x)

converted = set([1,1,1,1,1,1,1,2,2,2,2,2,2,2,3,3,3,3,3,3])
print(converted) #Since changed to set, it lists only {1,2,3}