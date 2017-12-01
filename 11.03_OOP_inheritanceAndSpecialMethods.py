# Inheritance => way to form new classes using old classes already defined
# Newly created classes called Derived Classes => classes derived from called Base Classes
# Important benefits are code reuse and reduction of program base code

class Animal(): #Base class

  def __init__(self):
    print('Animal Created')

  def who_am_i(self):
    print('Animal')

  def eat(self):
    print('Eating')

class Dog(Animal):
  
  def __init__(self):
    # Animal.__init__(self)
    print('Dog created')

  def bark(self):
    print('Woof')

  def eat(self): #When I want to override the base class, I can add it to the derived class here and it will override the previous
    print('Dog eating')

mydog = Dog()
mydog.who_am_i() #Even though Dog does not have who_am_i in the class, it derives (or inherits) it from Animal
mydog.eat()
mydog.bark()


# Special methods => allow you to perform special operations
# Not called directly => called by specific python language syntax

class Book():
  def __init__(self,title,author,pages):
    self.title = title
    self.author = author
    self.pages = pages

  # Special method (most common)
  def __str__(self): #__str__ is the syntax of string representation
    return 'Title: {}, Author: {}, Pages: {}'.format(self.title,self.author,self.pages)

  # Another special method
  def __len__(self):
    return self.pages

  # Another special method (there are a lot)
  def __del__(self):
    print('A book is destroyed')

b = Book('Python','Jose',200)
print(b) #When you print on an object, you are showing the string representation => not actually defined the string representation until you call the special method
print(len(b))
del b