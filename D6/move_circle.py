from pico2d import *
import math
open_canvas()

grass=load_image('grass.png')
character=load_image('character.png')

x=400
y=90
C=180
r=20
while(1):
    clear_canvas_now()
    grass.draw_now(400,30)
    x=-math.cos(C/360*math.pi)*200+400
    y=math.sin(C/360*math.pi)*200+290
    character.draw_now(x,y)
    C=C+10
    delay(0.1)

close_canvas()
