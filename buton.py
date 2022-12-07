import turtle as trtl


keybinds = trtl.Turtle()
colour = trtl.Turtle()
shape = trtl.Turtle()
pensize = trtl.Turtle()
detail = trtl.Turtle()

#keybinds
keybinds.shape("triangle")
keybinds.shapesize(2)
keybinds.penup()
keybinds.goto(100,100)
keybinds.pendown()

def keybinds_clicked(x,y):
    print("keybinds was clicked")

#colour
colour.shape("circle")
colour.shapesize(2)
colour.penup()
colour.goto(50,100)
colour.pendown()

def colour_clicked(x,y):
  print("colour was clicked")

#shape
shape.shape("square")
shape.shapesize(2)
shape.penup()
shape.goto(0,100)
shape.pendown()

def shape_clicked(x,y):
  print("shape was clicked")

#pensize
pensize.shape("circle")
pensize.shapesize(2)
pensize.penup()
pensize.goto(-50,100)
pensize.pendown()

def pensize_clicked(x,y):
  print("pensize was clicked")

#detail level
detail.shape("triangle")
detail.shapesize(2)
detail.penup()
detail.goto(-100,100)
detail.pendown()

def detail_clicked(x,y):
  print("detail level was clicked")

import turtle as trtl


keybinds = trtl.Turtle()
colour = trtl.Turtle()
shape = trtl.Turtle()
pensize = trtl.Turtle()
detail = trtl.Turtle()

#keybinds
keybinds.shape("triangle")
keybinds.shapesize(2)
keybinds.penup()
keybinds.goto(100,100)
keybinds.pendown()

def keybinds_clicked(x,y):
    print("keybinds was clicked")

#colour
colour.shape("circle")
colour.shapesize(2)
colour.penup()
colour.goto(50,100)
colour.pendown()

def colour_clicked(x,y):
  print("colour was clicked")

#shape
shape.shape("square")
shape.shapesize(2)
shape.penup()
shape.goto(0,100)
shape.pendown()

def shape_clicked(x,y):
  print("shape was clicked")

#pensize
pensize.shape("circle")
pensize.shapesize(2)
pensize.penup()
pensize.goto(-50,100)
pensize.pendown()

def pensize_clicked(x,y):
  print("pensize was clicked")

#detail level
detail.shape("triangle")
detail.shapesize(2)
detail.penup()
detail.goto(-100,100)
detail.pendown()

def detail_clicked(x,y):
  print("detail level was clicked")


keybinds.onclick(keybinds_clicked)
colour.onclick(colour_clicked)
shape.onclick(shape_clicked)
pensize.onclick(pensize_clicked)
detail.onclick(detail_clicked)
wn = trtl.Screen()
wn.mainloop()
keybinds.onclick(keybinds_clicked)
colour.onclick(colour_clicked)
shape.onclick(shape_clicked)
pensize.onclick(pensize_clicked)
detail.onclick(detail_clicked)
wn = trtl.Screen()
wn.mainloop()
