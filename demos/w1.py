name = input( "What is your name? ")
job = input("What is yout ocupation? ")
salary = float(input("How much do you earn?"))

salary = salary - 0.1*salary

print(type(salary))
print("Welcome!")
print(f"Nice to meet you {name}. Do you like your job asa a {job}?")
#print(f"Nice to meet you {}. Do you like your job asa a {}".format(name,job))

