class Robot:
  def introduce_self(self):
    print('My name is ' + self.name)

r1 = Robot()# create a new object from the class Robot
r1.name = "Eva"
r1.color = "Brown"
r1.weight = 3

r2 = Robot()
r2.name = "Chui"
r2.color = "White"
r2.weight = 4.5

r1.introduce_self() #  prints my name is Eva
