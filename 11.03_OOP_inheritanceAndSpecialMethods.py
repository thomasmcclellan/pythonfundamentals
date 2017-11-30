# Inheritance => way to form new classes using old classes already defined
# Newly created classes called Derived Classes => classes derived from called Base Classes
# Important benefits are code reuse and reduction of program base code

class Animal():

  def __init__(self):
    print('Animal Created')

  def whoAmI(self):
    print('Animal')

  def eat(self):
    print('Eating')

  