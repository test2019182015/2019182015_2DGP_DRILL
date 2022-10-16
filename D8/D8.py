from pico2d import *
def run_draw_left():
    global y
    global frame
    global x
    clear_canvas()
    tuk_ground.draw(TUK_WIDTH // 2, TUK_HEIGHT // 2)
    character.clip_draw(frame * 100, 0, 100, 100, x, y)
    update_canvas()
    handle_events()
    x+=dir*5
    frame = (frame + 1) % 8

    delay(0.01)

def run_draw_right():
    global y
    global x
    global frame
    clear_canvas()
    tuk_ground.draw(TUK_WIDTH // 2, TUK_HEIGHT // 2)
    character.clip_draw(frame * 100, 100, 100, 100, x, y)
    update_canvas()
    handle_events()
    x+=dir*5
    frame = (frame + 1) % 8

    delay(0.01)

def stay_draw_right():
    global y
    global x
    global frame
    clear_canvas()
    tuk_ground.draw(TUK_WIDTH // 2, TUK_HEIGHT // 2)
    character.clip_draw(frame * 100, 300, 100, 100, x, y)
    update_canvas()
    handle_events()
    x+=dir*5
    frame = (frame + 1) % 8

    delay(0.01)

def stay_draw_left():
    global y
    global x
    global frame
    clear_canvas()
    tuk_ground.draw(TUK_WIDTH // 2, TUK_HEIGHT // 2)
    character.clip_draw(frame * 100, 200, 100, 100, x, y)
    update_canvas()
    handle_events()
    x+=dir*5
    frame = (frame + 1) % 8

    delay(0.01)

def run_draw_up_down_left():
    global y
    global x
    global frame
    clear_canvas()
    tuk_ground.draw(TUK_WIDTH // 2, TUK_HEIGHT // 2)
    character.clip_draw(frame * 100, 0, 100, 100, x, y)
    update_canvas()
    handle_events()
    y+=dir*5
    frame = (frame + 1) % 8

    delay(0.01)

def run_draw_up_down_right():
    global y
    global x
    global frame
    clear_canvas()
    tuk_ground.draw(TUK_WIDTH // 2, TUK_HEIGHT // 2)
    character.clip_draw(frame * 100, 100, 100, 100, x, y)
    update_canvas()
    handle_events()
    y+=dir*5
    frame = (frame + 1) % 8

    delay(0.01)


def run():
     global run_left
     global run_right
     global stay_right
     global stay_left
     global run_up_down_left
     global run_up_down_right
     if(run_left==1 and x>0):
        run_draw_left()
     if(run_right==1 and x<800):
        run_draw_right()
     if(stay_right==1):
        stay_draw_right()
     if(stay_left==1):
        stay_draw_left()
     if(run_up_down_left==1 and y>=0 and y<=600):
        run_draw_up_down_left()
     elif(y<0):
         y=y+2
     elif (y >600):
         y = y - 2  
     if(run_up_down_right==1 and y>=0 and y<=600):
        run_draw_up_down_right()
     elif(y<0):
         y=y+2
     elif (y >600):
         y = y - 2  
def handle_events():
     global running
     global dir
     global run_left
     global run_right
     global stay_right
     global stay_left
     global run_up_down_left
     global run_up_down_right
     events = get_events()
     for event in events:
         if event.type == SDL_QUIT:
             running = False
         elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_RIGHT:
                dir += 1
                run_left=0
                run_right=1
                stay_right=0
                stay_left=0
                run_up_down_left=0
                run_up_down_right=0
            elif event.key == SDLK_LEFT:
                dir -= 1
                run_left=1
                run_right=0
                stay_right=0
                stay_left=0
                run_up_down_left=0
                run_up_down_right=0
            elif event.key == SDLK_UP:
                 if (run_left==1 or stay_left==1):
                     dir += 1
                     run_left=0
                     run_right=0
                     stay_right=0
                     stay_left=0
                     run_up_down_left=1
                     run_up_down_right=0
                 elif(run_right==1 or stay_right==1):
                     print("up up")
                     dir += 1
                     run_left=0
                     run_right=0
                     stay_right=0
                     stay_left=0
                     run_up_down_left=0
                     run_up_down_right=1

            elif event.key == SDLK_DOWN:
                 if(run_right==1 or stay_right==1):
                     dir -= 1
                     run_left=0
                     run_right=0
                     stay_right=0
                     stay_left=0
                     run_up_down_left=0
                     run_up_down_right=1
                 if (run_left==1 or stay_left==1):
                     dir -= 1
                     run_left=0
                     run_right=0
                     stay_right=0
                     stay_left=0
                     run_up_down_left=1
                     run_up_down_right=0

            elif event.key == SDLK_ESCAPE:
                running = False
         elif event.type == SDL_KEYUP:
              if event.key == SDLK_RIGHT:
                 dir =0
                 run_left=0
                 run_right=0
                 stay_right=1
                 stay_left=0
                 run_up_down_left=0
                 run_up_down_right=0
              elif event.key == SDLK_LEFT:
                 dir =0
                 run_left=0
                 run_right=0
                 stay_right=0
                 stay_left=1
                 run_up_down_left=0
                 run_up_down_right=0
              elif event.key == SDLK_UP:

                 if run_up_down_left==1:

                    dir =0
                    run_left=0
                    run_right=0
                    stay_right=0
                    stay_left=1
                    run_up_down_left=0
                    run_up_down_right=0
                 elif run_up_down_right==1:

                    dir =0
                    run_left=0
                    run_right=0
                    stay_right=1
                    stay_left=0
                    run_up_down_left=0
                    run_up_down_right=0

              elif event.key == SDLK_DOWN:

                 if run_up_down_right==1:

                    dir =0
                    run_left=0
                    run_right=0
                    stay_right=1
                    stay_left=0
                    run_up_down_left=0
                    run_up_down_right=0
                 elif run_up_down_left==1:

                    dir =0
                    run_left=0
                    run_right=0
                    stay_right=0
                    stay_left=1
                    run_up_down_left=0
                    run_up_down_right=0
running = True
x = 800 // 2
frame = 0
dir = 0
tuk_ground=load_image('map_1.png')
grass=load_image('bg2')
while running:
    clear_canvas()
    grass.draw(400, 30)
    character.clip_draw(frame * 100, 0, 100, 100, x, 90)
    update_canvas()
    handle_events()
    frame = (frame + 1) % 8
    x += dir * 5
    delay(0.01)