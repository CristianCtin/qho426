salary = float(input('Enter your salary: '))
years = int(input(' How long are you with the company? '))

if years > 2:
  if salary < 25000: #Indentation (Tab)
    salary *=1.1
  else:
    salary +=100
elif years > 1:
  print('No salary increase for you!')
else:
  if salary < 15000:
    print ('Apologies this was an error. You shall earn £20.000')
    salary = 20000
print('Let us work for the good of the corporation')
