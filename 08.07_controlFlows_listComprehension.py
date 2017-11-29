# Continued from 03.02

x = [1,2,3,4]

out = []
for num in x:
  out.append(num ** 2)

print(out)

# OR

out = [num ** 2 for num in x]
print(out)