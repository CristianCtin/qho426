#[Tasks]

#We wish to create a program that allows us to help Beep learn to paint.

##The program should start by prompting the user for a direction to move the paint brush (up, down, left or right).
#The program should then work out in which direction Beep should paint and display a suitable message.

#An example run of such a program is shown below:


#Towards which direction should I paint (up, down, left or right)?
#up
#I am painting in the upward direction!



direction = input('Towards which direction should I paint (up, down, left or right) \n')
if direction == 'up':
  print('I am painting in the upward direction!')
elif direction == 'down':
  print('I am painting in the downward direction!')
elif direction == 'left':
  print('I am painting in the left direction!')
elif direction == 'right':
  print('I am painting in the downward direction!')
else:
  print('Bad direction!!!')
