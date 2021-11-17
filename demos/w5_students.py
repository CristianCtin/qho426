def generate_sts():
  print("Enter the name: ")
  name = input()
  print("Enter the mark: ")
  grade = float(input())
  return (name, grade)


def add_multiple_sts():
  all_sts = []
  while True:
    all_sts.append(generate_sts())
    print("To stop, enter 99")
    x = int(input())
    if x == 99:
      break
  return all_sts


def print_sts(lista):
  for std in lista:
    print(f"{std[0]}earned {std[1]} marks on their exam")

def avg_mark(lista):
  total = 0
  for person in lista:
    total += person[1]
  return total/len(lista)

def run():
  listb = add_multiple_sts()
  print_sts(listb)
  print(f"The average mark is {avg_mark(listb)}")

run()
