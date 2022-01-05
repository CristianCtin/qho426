from person import Person
from database import Database

db = Database()
print (f"Welcome to {db.name}!!!")

while True:
  print('''\nChoose one of the following options:
        1-Add a member
        2-Remove a member
        3-Display all members
        4-Exit
  ''')
  opt = int(input("Choose an option: "))
  if opt == 1:
    name = input("Enter their name: ")
    age = int(input("Enter their age:"))
    job = input("eNTER THEIR JOB")
    P = pERSON(NAME, AGE, JOB, WEIGHT)
    db.add_person(p)
  elif opt == 2:
    name = input("Enter name of a person to be removed: ")
    for person in db.people:
      if person.name == name:
        db.remove_person(person)
  elif opt == 3:
    db.display_all()
  elif opt == 4:
    break
  else:
    print("Invalide Option. Choose number from 1 to 4")