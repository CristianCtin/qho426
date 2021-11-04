print("Program started!")
print("Please enter an ASCII code: ")
code = int(input())

if(code>32 and code<126):
  print("The character represented by the ASCII code {} is: {}. ".format (code, chr(code)))
  
  

else:
  print("No character!")

print ("Program ended!")