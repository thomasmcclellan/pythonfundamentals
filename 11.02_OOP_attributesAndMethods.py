# Attributes are characteristics of an object
# Methods are operations we can perform on an object

class Dog():
  def __init__(self,breed,name): #Methods look likes functions within the class and have the __#__ syntax
    self.breed = breed #Attribute involves self.#
    self.name = name #self operates similarly to the 'this' keyword in JS

my_dog = Dog('Lab','Sammy') #Now that we have the attribute of breed, we need to supply said attribute
print(my_dog.breed) #Lab
print(my_dog.name) #Sammy


# Class Object Attributes (COA)
# Goes outside any methods at top to pertain to all methods

class Dog():
  # COA
  species = 'Mammal'

  def __init__(self,breed,name): 
    self.breed = breed 
    self.name = name 

my_dog = Dog('Lab','Sammy') 
print(my_dog.breed) #Lab
print(my_dog.name) #Sammy
print(my_dog.species) #Mammal


# Methods => functions defined within the body of a class
# Used to perform operations within the attributes of objects and are essential in incapsulation concepts of the OOP paradigm => essential in dividing the responsibilities in programming
# Methods are the whole point in creating your own object

class Circle():
  pi = 3.14

  def __init__(self,radius = 1): #If no radius is given, it defaults at 1
    self.radius = radius

  def area(self):
    return self.radius * self.radius * Circle.pi

  def set_radius(self,new_r):
    self.radius = new_r

  myc = Circle(3)
  myc.set_radius(999)
  print(myc.area())