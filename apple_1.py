#   a123_apple_1.py
import turtle as t
import random
import string 

#-----setup-----
apple_image = "apple.gif" # Store the file name of your shape

wn = t.Screen()
wn.setup(width=1000, height=500)
wn.addshape(apple_image) # Make the screen aware of the new file
wn.bgpic("background.gif")

class apple():
  def __init__(self):
    self.apple = t.Turtle()
    self.letter = t.Turtle()
    self.letter.hideturtle()
    self.xpos, self.ypos = random.randint(-200,220), 0
    self.letter_to_press = random.choice(string.ascii_lowercase)
  
  def show_letter(self):
    self.letter.penup()
    self.letter.goto(self.xpos-5, self.ypos-10)
    self.letter.write(str(self.letter_to_press), font=("Arial", 16))
    self.letter.pendown()

  def move_apple(self):
    self.apple.penup()

    self.apple.seth(270)
    self.apple.fd(200)
    self.letter.clear()
    self.apple.clear()

    self.apple.pendown()

    if self.apple.ycor() <= -200:
      self.apple.hideturtle()

  def draw_apple(self):
    self.apple.goto(self.xpos, self.ypos)
    self.apple.shape(apple_image)
    self.show_letter()
    wn.onkeypress(self.move_apple, str(self.letter_to_press))
    wn.update()

apples = []

for i in range(5):
  apples.append(apple())

for x in apples:
  x.draw_apple()

wn.listen()
wn.mainloop()