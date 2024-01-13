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

class Student(Person): #child class
  def __init__(self,first_name, age): #overrides the parent's __init__()
  super().__init__(first_name, age) #super() function that will make the child class inherit all the methods and properties from its parent:

y = Student("John", 19)
y.greet()
