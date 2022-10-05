import turtle

count=4
while(count>0):
  turtle.right(90)
  turtle.forward(500)
  count -=1

count=5
while(count>0):
  if(count%2==0):
   turtle.left(90)
   turtle.forward(100)
   turtle.left(90)
   turtle.forward(500)
  elif(count%2!=0):
   turtle.right(90)
   turtle.forward(100)
   turtle.right(90)
   turtle.forward(500)
  count -=1

turtle.penup()
turtle.goto(0,-500)
turtle.pendown()

count=5
while(count>0):
  if(count%2==0):
   turtle.left(90)
   turtle.forward(500)
   turtle.right(90)
   turtle.forward(100)
  elif(count%2!=0):
   turtle.right(90)
   turtle.forward(500)
   turtle.left(90)
   turtle.forward(100)
  count -=1

turtle.exitonclick()
