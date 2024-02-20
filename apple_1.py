#   a123_apple_1.py
import turtle as trtl
import string

#-----setup-----
apple_image = "Apple-Avalanche/apple.gif" # Store the file name of your shape

wn = trtl.Screen()
wn.setup(width=1000, height=500)
wn.addshape(apple_image) # Make the screen aware of the new file
wn.bgpic('Apple-Avalanche/background.gif')
wn.tracer(False)

apple = trtl.Turtle()
appleYpos = apple.ycor()
appleXpos = apple.xcor()

#-----functions-----
# given a turtle, set that turtle to be shaped by the image file
def draw_apple(active_apple):
  trtl.goto(appleXpos, appleYpos)
  active_apple.shape(apple_image)
  wn.update()

def keyToPress():
  global wn

  apple.write('A')
  wn.onkey(apple.clear(), 'a')

#-----function calls-----
draw_apple(apple)
keyToPress()

wn.listen()
wn.mainloop()