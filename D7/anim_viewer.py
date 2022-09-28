from pico2d import *

open_canvas()

grass = load_image('grass.png')
character = load_image('sourse.png')

def DRAW(x,y):
   clear_canvas_now()
   grass.draw(400, 30)
def LED_character():
 frame=0
 for a in  range(0,8,1):
   DRAW(400,70)
   character.clip_draw(frame * 22, 0, 23, 25, 400, 60)
   update_canvas()
   frame = (frame + 1) % 8
   delay(0.2)
   get_events()
def Runshot_and_jump_character():
  frame=0
  for a in  range(0,800,5):
   if(a<670):
    DRAW(400,70)
    character.clip_draw(frame * 29, 239,32,27, a, 70)
    update_canvas()
    frame = (frame + 1) % 4
    delay(0.05)
    get_events()
   elif(a==670):
    for a in  range(0,3,1):
     DRAW(400,70)
     character.clip_draw(frame * 20, 55, 20, 27, 670+a*50, 70+a*50)
     update_canvas()
     frame = (frame + 1) % 3
     delay(0.05)
     get_events()
def Go_and_stop():
  frame=0
  x=100
  for a in  range(100,700,5):
    DRAW(400,70)
    if(frame<4):
     character.clip_draw(frame * 22, 270,20,100, x, 80, 50,50)
     update_canvas()
     frame = (frame + 1) % 6
     delay(0.05)
     get_events()
    elif(frame>3):
     character.clip_draw(frame * 22, 270,20,100, a, 80, 50,50)
     update_canvas()
     frame = (frame + 1) % 6
     x=a
     delay(0.05)
     get_events()
def spawn():
  frame=0
  
  for a in  range(0,3,1):
   DRAW(400,70)
   character.clip_draw(frame * 8+((a*2)^2), 26, 8+((a*2)*(a+1)-1), 27, 400, 60)
   update_canvas()
   frame = (frame + 1) % 3
   delay(0.1)
   get_events()

while (True):
   
   Runshot_and_jump_character()
   Go_and_stop()
   spawn()
   LED_character()
  

close_canvas()

