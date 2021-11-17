def simple_tuples():
  person = ("Cristian", 38, False)
  print(person)
  #printing a tuple
  print(type(person))
  #acces elements via IndexError
  print(f"{person[0]} is {person[1]} years old")
  #no mutation possible
  if person[2]:
    print("You have a doggo!")
  else:
    print("No dogo no fun!")
  #Tuples can be concateneted (joined) - but this create a different tuple
  p1 = person + (20, "none")
  print(p1)
  print(person)
  t = (16, 6, 4, 22, 66)
  print(max(t))
  print(min(t))



simple_tuples(person)