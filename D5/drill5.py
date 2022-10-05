import turtle

def turtle_move_to_w():
   turtle.stamp()
   turtle.setheading(90)
   turtle.forward(50)
def turtle_move_to_a():
   turtle.stamp()
   turtle.setheading(180)
   turtle.forward(50)
def turtle_move_to_s():
   turtle.stamp()
   turtle.setheading(270)
   turtle.forward(50)
def turtle_move_to_d():
   turtle.stamp()
   turtle.setheading(0)
   turtle.forward(50)

def turtle_re():
   turtle.reset()
   
turtle.shape('turtle')

turtle.onkey(turtle_move_to_w,'w')

turtle.onkey(turtle_move_to_a,'a')

turtle.onkey(turtle_move_to_s,'s')

turtle.onkey(turtle_move_to_d,'d')

turtle.onkey(turtle_re,'Escape')

turtle.listen()
