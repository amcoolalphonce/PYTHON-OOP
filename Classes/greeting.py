class Person:
  pass # for an empty class to avoid errors
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def greet(self):
    print(f'My name is {self.name} and I am {self.age} years old')

person1 = Person()
person1.greet()

del person1.age # deletes the age of person1

class Student(Person):
  pass
