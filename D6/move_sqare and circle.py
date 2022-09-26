from pico2d import *
import math
open_canvas()

grass=load_image('grass.png')
character=load_image('character.png')

x=400
y=90
C=180
r=25
while(1):
 C=180
 while(x<800):
    clear_canvas_now()
    grass.draw_now(400,30)
    character.draw_now(x,y)
    x=x+2
    delay(0.001)
 while(y<600):
    clear_canvas_now()
    grass.draw_now(400,30)
    character.draw_now(x,y)
    y=y+2
    delay(0.001)
 while(x>0):
    clear_canvas_now()
    grass.draw_now(400,30)
    character.draw_now(x,y)
    x=x-2
    delay(0.001)
 while(y>90):
    clear_canvas_now()
    grass.draw_now(400,30)
    character.draw_now(x,y)
    y=y-2
    delay(0.001)
 while(x<400):
    clear_canvas_now()
    grass.draw_now(400,30)
    character.draw_now(x,y)
    x=x+2
    delay(0.001)
 while(C<900):
    clear_canvas_now()
    grass.draw_now(400,30)
    x=-math.cos(C/360*math.pi)*200+400
    y=-math.sin(C/360*math.pi)*200+290
    character.draw_now(x,y)
    C=C+10
    delay(0.01)

    
close_canvas()
