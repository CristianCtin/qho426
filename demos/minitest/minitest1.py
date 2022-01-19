def fav_movie():
  print("What is your favorite movie?")
  response = input()
  print("{response} is terrible!")

#fav_movie()



def imdb_rating(rating):
  if rating > 7:
    print("Lets watch it!")
  else:
    print("not gonna waste my time")
  print("I hope you agree")

#imdb_rating(4)
#imdb_rating(9)



def binge(numb):
  for i in range(numb):
    print(f"Oh-yeah! #{i+1}")
  print(f"there are {numb} episodes in the series")