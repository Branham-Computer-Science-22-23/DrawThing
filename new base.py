#import
import random as rand
import turtle as t
wn = t.Screen()
#setup
t.speed(5)
detail = 5
shapes = ["arrow", "turtle", "circle", "square", "triangle", "classic", "arrow", "classic"]
default_shape = 0
colours = ["red", "blue", "green", "black", "yellow", "purple", "orange", "red", "orange"]
default_colour = 3


#functions
def buttons():
  #set up
  import turtle as trtl
  keybinds = trtl.Turtle()
  colour = trtl.Turtle()
  colour_1 = trtl.Turtle()
  shape = trtl.Turtle()
  shape_1 = trtl.Turtle()
  keybinds.speed(0)
  colour.speed(0)
  shape.speed(0)
  shape_1.speed(0)  
  
  def everything_setup():
    #shape
    shape.hideturtle()
    shape.shape("triangle")
    shape.shapesize(1)
    shape.penup()
    shape.goto(100, 80)
    shape.left(90)
    shape.showturtle()
  
    #shape1
    shape_1.hideturtle()
    shape_1.shape("triangle")
    shape_1.shapesize(1)
    shape_1.penup()
    shape_1.goto(100, 50)
    shape_1.right(90)
    shape_1.showturtle()
    
    #colour
    colour.hideturtle()
    colour.shape("triangle")
    colour.shapesize(1)
    colour.penup()
    colour.goto(100, 0)
    colour.left(90)
    colour.showturtle()
  
    #colour_1
    colour_1.hideturtle()
    colour_1.shape("triangle")
    colour_1.shapesize(1)
    colour_1.penup()
    colour_1.goto(100, -15)
    colour_1.right(90)
    colour_1.showturtle()
    
    #keybinds
    keybinds.hideturtle()
    keybinds.shape("square")
    keybinds.shapesize(1)
    keybinds.penup()
    keybinds.goto(100, -150)
    keybinds.showturtle()
  
  def keybinds_clicked(x,y): #shows keybinjds
    print("Arrow keys to move \ndetail level: m \ncolour: n \npenup: b \npendown: v \nkeybinds: k \npen size: t \nremove colour: i \nremove shape: e")
  
  def colour_clicked(x,y): #changes colour
    global colours, default_colour    
    if default_colour < 6:
      t.color(colours[default_colour + 1])
      default_colour += 1
      colour_1.color(colours[default_colour - 1])
      colour.color(colours[default_colour + 1])
  
  def shape_clicked(x,y):# cahnges shapes
    global shapes, default_shape
    if default_shape < 5:
      t.shape(shapes[default_shape + 1])
      default_shape += 1
      shape_1.shape(shapes[default_shape - 1])
      shape.shape(shapes[default_shape + 1])
  
  def colour_1_clicked(x,y): #changes colour
    global colours, default_colour
    if default_colour > 0:
      t.color(colours[default_colour - 1])
      default_colour -= 1
      colour_1.color(colours[default_colour - 1])
      colour.color(colours[default_colour + 1])
  
  def shape_1_clicked(x,y): #changes shape
    global shapes, default_shape
    if default_shape > 0:
      t.shape(shapes[default_shape - 1])
      default_shape -= 1
      shape_1.shape(shapes[default_shape - 1])
      shape.shape(shapes[default_shape + 1])


#all the on click stufff
  everything_setup()
  keybinds.onclick(keybinds_clicked)
  colour.onclick(colour_clicked)
  shape.onclick(shape_clicked)
  colour_1.onclick(colour_1_clicked)
  shape_1.onclick(shape_1_clicked)

def det(): #detail level
  global detail
  detail = int(input("pixels: "))
  return(detail)

def f(): #go up
  global detail
  x = t.xcor()
  y = t.ycor()
  t.setpos(x, y + detail)

def l(): #left
  global detail
  x = t.xcor()
  y = t.ycor()
  t.setpos(x - detail, y)

def r(): #right
  global detail
  x = t.xcor()
  y = t.ycor()
  t.setpos(x + detail, y)

def b(): #down
  global detail
  x = t.xcor()
  y = t.ycor()
  t.setpos(x, y - detail)

def remove_colour():
  temp_remove = str(input("colour to remove (might break code lol): "))
  colours.remove(temp_remove)

def remove_shape():
  temp_remove = str(input("shape to remove (might break code lol): "))
  shapes.remove(temp_remove)

def col(): #colour
  colour = input("colour: ")
  t.pencolor(colour)

def keybinds(): #show keybinds
  print("Arrow keys to move \ndetail level: m \ncolour: n \npenup: b \npendown: v \nkeybinds: k \npen size: t \nremove colour: i \nremove shape: e")

def pensize(): #pensize
  t.pensize(int(input("pensize: ")))

def apple(): #random apple she really wanted to add
  aple.showturtle()
  aple.goto(rand.randint(-200, 200), rand.randint(-200, 200))

#apple setup
wn.addshape("apple2.gif")
aple = t.Turtle()
aple.hideturtle()
aple.shape("apple2.gif")
aple.penup()
aple.speed(0)


#executions

buttons()
keybinds()
t.ondrag(t.goto)
wn.onkey(f, "Up")
wn.onkey(l, "Left")
wn.onkey(r, "Right")
wn.onkey(b, "Down")
wn.onkey(det, "m")
wn.onkey(col, "n")
wn.onkey(t.penup, "b")
wn.onkey(t.pendown, "v")
wn.onkey(keybinds, "k")
wn.onkey(pensize, "t")
wn.onkey(apple, "u")
wn.onkey(remove_colour, "i")
wn.onkey(remove_shape, "e")

wn.listen()
wn.mainloop()
