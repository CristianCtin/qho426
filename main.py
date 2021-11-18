phonebook = {}
d2 = dict()

#Intialise non-empty dictionary
piotr_data = {"Name" : "Piotr", "Age" :55, "Doggo":False, "Title": "Mr"}

#Print full dictionary
print(piotr_data)

#Use part of the dictionary for printing
x = piotr_data["Name"]
y = piotr_data["Age"]
print(f"{x} is {y} yers old")

#Adding elements to a dictionary
phonebook["Max"] = +447789696955
phonebook["Bob"] = +667575748473
phonebook["Son"] = None

print(phonebook)

#Add more people in the phonebook
for i in range(3):
  n = input("enter the name: ")
  numb = input(f"Enter {n}'s numner: ")
  phonebook[n] = numb

name = input("Who would you like to call?\n")

if name in phonebook:
  print(f"Calling {name} with phone no {phonebook['Max']} ")
else:
  print(f"{name} is not in your phonebook")