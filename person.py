#The class person which will be a blueprint/template for my object to store information about humans
class Person:

  #Class atribute -> constant, witch is visible to all objects of the class
  MAX_ENERGY = 100

  #Static method -> Utility function, which does not require an object to exist
  @staticmethod
  def is_mature(age):
    if age >= 35:
      return True
    else:
      return False

  #a initialiser/constructor -> a function that is used immediately hen the object is created
  def __init__(self, name = "", age = 1, job ="None", weight = 5, energy = 100):
    #These ill be instance attributes (features of each object)
    self.name = name 
    self.age = age
    self.job = job
    self.weight = weight
    if energy > Person.MAX_ENERGY:
      self.energy = Person.MAX_ENERGY
    else:
      self.energy = energy

  #Magic method __str__ witch is invokes by print() function automatically
  def __str__(self):
    return f"Name:{self.name} Age:{self.age} Job:{self.job} Weight: {self.weight} Energy: {self.energy}"

  #Instance method that works on each object of the class
  def hello(self):
    print(f"Hello! My name is {self.name}. I am {self.age}. I work as {self.job}. I weight {self.weight}. My energy is {self.energy}. Nice to meet you!")

  def grow(self, years):
    self.age += years

  def eat(self, food, w):
    print(f"{self.name} have eaten {food}.")
    self.weight += w
    print(f"They now weight {self.weight}kg")

p1 = Person("Alessandro", 28, "driver", 68, 99)
p2 = Person("Dawid", 22, "Clerk", 55, 20)
#print(f"The new person is called {p1.name}. They are {p1.age} years old and they weight {p1.weight} kg. They work as {p1.job}")
#print(f"The new person is called {p2.name}. They are {p2.age} years old and they weight {p2.weight} kg. They work as {p2.job}")
#p1.hello()
#p2.hello()
#p1.job = "IT Consultant"
#p1.energy = 25
#p1.age += 1
#p2.eat("Lassagne", 3)
#p2.grow(20)
#p2.hello()

print(p1)
print(p2)
p1.hello()
print(f"{Person.is_mature(50)}")
print(f"{Person.is_mature(32)}")
print(f"{Person.is_mature(p2.age)}")




