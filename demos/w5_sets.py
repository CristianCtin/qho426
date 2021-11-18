#Initialise empty set
s = set()

#Check the tipe is set
print(type(s))

#Initialise non-empty set
colours = {"blue", "yellow", "red", "purple", "green"}

print(colours)

#Adding elements to a set
colours.add("black")
colours.add("pink")

print(colours)

#DELETE AN ELEMENT OF A SET
colours.remove("blue")


#CHECHING MEMBERSHIP
if "blue in colours":
  print("Yay - my favorite colour is here!")
else:
  print("You are missing an important colour")

colors = {"yellow", "black", "red", "cyan"}

#take union of two sets- join them together but no duplicates
print(colours.union(colors))

#Take intersection of two sets
print(colours.intersection(colors))

#take set difference -keep only elements not in other collection
print(colours.difference(colors))



