import random
from pico2d import *

back_WIDTH, back_HEIGHT = 600, 600



# 710, 896

def draw_back():
    clear_canvas()
    TUK_ground.draw(back_WIDTH // 2, back_HEIGHT // 2)
    grass.draw(350, 50)
    update_canvas()


def run_draw_move():
    global y
    global x
    global frame
    draw_back()
    character.clip_draw(frame * 100, 100, 100, 100, x, y)
    update_canvas()
    handle_events()
    x+=dir*5
    frame = (frame + 1) % 8

    delay(0.01)

def stay_draw():
     delay(1)
def run_draw_up():
    delay(1)
def run():
    if run_move==1:
        run_draw_move()
    elif run_jump==1:
        run_draw_up()
    elif stay_move==1:
        stay_draw()


def handle_events():
     global running

     events = get_events()
     for event in events:
         if event.type == SDL_QUIT:
             running = False
         elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_RIGHT:
                run()
            elif event.key == SDLK_LEFT:
                run()
            elif event.key == SDLK_UP:
                run()
            elif event.key == SDLK_ESCAPE:
                running = False
         elif event.type == SDL_KEYUP:
              if event.key == SDLK_RIGHT:
                  run()
              elif event.key == SDLK_LEFT:
                  run()
              elif event.key == SDLK_UP:
                  run()










run_move=0
stay_move=0
run_jump=0
move_dir=0
jump_dir=0
move_to=0
jump_to=0
open_canvas(back_WIDTH, back_HEIGHT)

grass=load_image('grass1.png')
TUK_ground = load_image('bg2.png')
character = load_image('bosh.png')
running = True
frame=0
while running:
    draw_back()
    character.clip_draw(frame * 128, 1152, 128, 130, 330, 125, 30, 30)
    #                      프레임      줄   크기   높이   x   y    w   h
    #줄 128의 배수
    update_canvas()
    frame = (frame + 1) % 4
    handle_events()
    delay(0.)

close_canvas()




