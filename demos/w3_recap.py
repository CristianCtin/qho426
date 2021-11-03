#Program which creates a menu, where user can either get a nice meggage, calculate an area of rectangle/triangle or rptint out atimes table for a number.

while True:

  print("Please choose one of the following options:\n\n1-Nice message\n2-Area of a rectangle\n3-Area of a triangle\n4-Times table\n0-Exit")

  opt = int(input())

  if opt == 1:
    print("You do not smell so bad today!")
  elif opt ==2:
    w = float(input("Enter the width of the rectangle: "))
    l = float(input("Enter de lenght of the rectangle: "))
    area = w*1
    print("The area is {}".format(area))
  elif opt == 3:
    l = float(input("Enter de lenght of the triangle: "))
    h = float(input("Enter the height of the triangle: "))
    area = h*1/2
    print("The area is {}".format(area))
  elif opt == 4:
    n = int(input("Enter a whole number: "))
    for i in range(1, 11):
      print(f"{i}x{n} = {i*n}")
    print("This is it")
  elif opt == 0:
    break
  else:
    print("Whoopsie - no such option available")