#   a123_apple_1.py
import turtle as trtl

#-----setup-----
apple_image = "Trinket Download-NEWa123_apple_1-74f6bc04d4/pear.gif" # Store the file name of your shape

wn = trtl.Screen()
wn.setup(width=1000, height=500)
wn.addshape(apple_image) # Make the screen aware of the new file
wn.bgpic('Trinket Download-NEWa123_apple_1-74f6bc04d4/background.gif')
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
  trtl.write('A')

#-----function calls-----
draw_apple(apple)
keyToPress()

wn.mainloop()