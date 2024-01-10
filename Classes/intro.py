class Robot:
  def __init__(self, name, color, weight):
    self.name = name
    self.color = color
    self.weight = weight
    
  def introduce_self(self):
    print('My name is ' + self.name)

#r1 = Robot()# create a new object from the class Robot
#r1.name = "Eva"
#r1.color = "Brown"
#r1.weight = 3
r1 = Robot("Eva", "Brown", 3)
r2 = Robot("Chui", "White", 4.5)
#RESTART KERNEL AND CLEAR ALL OUTPUT VARIABLES
#r2 = Robot()
#r2.name = "Chui"
#r2.color = "White"
#r2.weight = 4.5

r1.introduce_self() #  prints my name is Eva
r2.introduce_self() # prints my name is Chui
