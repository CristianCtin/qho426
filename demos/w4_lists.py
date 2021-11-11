#Declare empty list
hated = []

#Declare non-empty list
fav = ["carbonara","Pizza","Casatiello","Pierogi"]

#Print full list
print(fav)

#Print a single element
print(fav[2])

#Add elements at the end of the list
hated.append("Tofu")
hated.append("Beans")
fav.append("Lasagne")

###print(fav)
###print(hated)

#Appending using a loop and user input
for i in range(2):
  print("Enter another hated dish: ")
  dish = input()
  hated.append(dish)

#Print the lenght/size of my list
print(len(hated))

print(hated)

#Insert data at any position on the list
fav.insert(1,"Korma")
print(f"The number of favorite dishes in : {len(fav)} ")
print(fav)
fav.insert(3,"Pancakes")
print(fav)
print(f"The number of favorite dishes in : {len(fav)} ")

#Remove items from the list
fav.remove("Casatiello")

print(fav)

#Remove by index
fav.pop(1)

#Delete an item via index(forever)
del fav[2]


print(fav)

#Slicing
print(hated[1:])
#print(hated[::-1]) backowrdds

for i in range(len(fav)):
  if fav[i] == "Pizza" :
    print(f"Pizza is located in position {i}")