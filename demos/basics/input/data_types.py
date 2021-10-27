print('What is your name human?')
name = input() #String reprezentation
print('How old are you (in years)?')
age = int(input()) #Integer
print('How tall are you (in meters)?')
height = float(input())
print('How much do you weight (in kilograms)?')
weight = int(input())

BMI = float(weight / height**2)
print(name, "your age is " + str(age), 'years old and your BMI is', BMI)

#print(f'{name} you are {age} years old. Your BMI is {BMI}')