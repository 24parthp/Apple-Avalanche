#   a123_apple_1.py
import turtle as trtl
import random
import string 

#-----setup-----
apple_image = "Apple-Avalanche/apple.gif" # Store the file name of your shape

wn = trtl.Screen()
wn.setup(width=1000, height=500)
wn.addshape(apple_image) # Make the screen aware of the new file
wn.bgpic("Apple-Avalanche/background.gif")

class apple():
  apple = trtl.Turtle()

  def __init__(self):
    self.xpos, self.ypos = random.randint(-200,220), 0
    self.letter = random.choice(string.ascii_letters)
  
  def show_letter(self):

  def draw_apple(active_apple, self):
    active_apple.shape(apple_image)
    self.show_letter()
    wn.update()

  def move_turtle(self):
    apple.seth(270)
    apple.fd(100)
    apple.clear()

wn.listen()
wn.mainloop()