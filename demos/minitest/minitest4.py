from abc import ABC, abstractmethod

class Per(ABC):
  #def __init__(self, name = "Zonk", age = 0, smell = True):
  #  self.name = name
  #  self.age = age
   # self.smell =smell
   def __init__(self, name = "Zonk"):
    self.name = name
    self.age = 1
    self.smell =True

  @abstractmethod
  def sound():
    pass


class Dog(Pet):

  def __init__ (self, name, toy):
    self.toy = toy
    self.dayly_walks = 3
    super().__init__(name)

  def __repr__(self):
    return f"dog(name = {self.name}, toy = {self.toy}, age = {self.age}, smell = {self.smell}, daily_walks = {self.daily_walks} )"


  def __str__(self):
    return f"The husband called {self.name}, it is {self.age} old and it work it {self.daily_walks} times."


  def get_age(self):
    return self.age


  def sound(self):
    print("Woof-woof")


  def wash(self):
    self.smell = False #Assuming washing removes the smell




class Husband(Pet):

  def __init__(self, name, job):
    self.job = job
    super().__init__(name)

  def __repr__(self):
    return f"dog(name = {self.name}, toy = {self.toy}, age = {self.age}, smell = {self.smell}, daily_walks = {self.daily_walks} )"


  def __str__(self):
    return f"The husband called {self.name}, it is {self.age} old and it work it {self.daily_walks} times."

  def get_age(self):
    return self.age


  def sound(self):
    print("Arrrrrr")


  def wash(self):
    self.smell = False





class Jobless_Husband(Husband):

  def __init__(self, name, job = None):
    super().__init__(name, job)


  def __repr__(self):
    return f"dog(name = {self.name}, toy = {self.toy}, age = {self.age}, smell = {self.smell}, daily_walks = {self.daily_walks} )"


  def __str__(self):
    return f"The jobless husband called {self.name}, it is {self.age} old and it work it {self.daily_walks} times."

  def get_job(self, j_name):
    self.job = j_name



if __name__ == "__main__":
  nona = Dog("Nona", 5, "Woody")
  jimmy = Husband("Jimmy")
  ted = Jobless_Husband("Ted")
  nona.sound()
  nona.age+=1
  print(jinny)
  print(ted)
  