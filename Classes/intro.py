class Robot:
  def introduce_self(self):
    print('My name is ' + self.name)

r1 = Robot()# create a new object from the class Robot
r1.name = "Eva"
r1.color = "Brown"
r1.weight = 3

r1.introduce_self() #  prints my name is Eva
