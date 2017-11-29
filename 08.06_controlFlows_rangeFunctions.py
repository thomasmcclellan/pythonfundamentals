# Can quickly generate ranges based on starting and ending points
a = [1,2,3,4,5]
print(a) #[1,2,3,4,5]

b = range(5)
print(b) #range(0,5) => saves space; doesn't have to list all numbers

c = list(range(5))
print(c) #[0,1,2,3,4]

d = list(range(0,20,2))
print(d) #[0,2,4,6,8,10,12,14,16,18] => remember it doesn't include 20


for item in range(10):
  print(item) # 0 1 2 3 4 5 6 7 8 9