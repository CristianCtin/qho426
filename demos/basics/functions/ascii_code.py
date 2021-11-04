print("Program started!")
print("Please enter a standar character:\n ")
character = input()

if(len(character) == 1):
  print("The ASCII code for{} is {}.".format(character, ord(character)))
else:
  print("Program Ended!")

print("Program ended")