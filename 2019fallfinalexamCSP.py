#2019-20 Fall Computer Science Principles Final Exam

#Ms. Haubold


#Name
# Conor Dycus
#Date
# 19/12/2019


#### INSTRUCTIONS ####
#Create an etch a sketch turtle game
#The turtle should move with the arrow keys (up, down, left and right), and draw
#Space should clear the screen
#o and p should make the pen size bigger and smaller
#u should pick the pen up or put the pen down
#All code must be commented
#BONUS
#Add a feature to change colors
#

#import required libraries
import turtle as trtl

#create turtle
sketch = trtl.Turtle()
sketch.shape("turtle")


#movement functions
sketch.left(90)
#Makes the turtle move forward, backwards, left, and right
def Up():
    sketch.forward(10)
def Down():
    sketch.backward(10)
def Left():
    sketch.left(90)
def Right():
    sketch.right(90)
#Resets the screen
def space():
    sketch.reset()
    sketch.left(90)
#color/drawing functions
#Makes the pen size get bigger and smaller
def o():
    sketch.pensize(5)
def p():
    sketch.pensize(1)
#Makes the pen go up and down
def u():
    if sketch.isdown():
        sketch.penup()
    else:   
        sketch.pendown()
#Makes the pen color different colors
def c():
    sketch.pencolor("green")
def v():
    sketch.pencolor("red")
def b():
    sketch.pencolor("black")
def n():
    sketch.pencolor("blue")







#create screen
wn = trtl.Screen()
#bind to keypresses
#The keys that make the turtle move
wn.onkeypress(Up,"Up")
wn.onkeypress(Down,"Down")
wn.onkeypress(Left,"Left")
wn.onkeypress(Right,"Right")
#The key that resets the screen
wn.onkeypress(space,"space")
#The keys that changes the size
wn.onkeypress(o,"o")
wn.onkeypress(p,"p")
#The key that makes the pen go up and down
wn.onkeypress(u,"u")
#The keys that change the color
wn.onkeypress(c,"c")
wn.onkeypress(v,"v")
wn.onkeypress(b,"b")
wn.onkeypress(n,"n")
#listen
wn.listen()

#mainloop
wn.mainloop()