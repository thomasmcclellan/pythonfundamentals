x = ("Insert another string here: {}".format('INSERT ME!'))
print(x)

y = "Item 1: {}, Item 2: {}".format('dog', 'cat')
print(y)

z = "Item 1: {x}, Item 2: {y}".format(x = 'dog', y = 'cat')
print(z)