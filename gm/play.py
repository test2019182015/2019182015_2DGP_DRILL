import random
from pico2d import *
from dataclasses import dataclass

back_WIDTH, back_HEIGHT = 600, 600

run_move=0
stay_move=0
run_jump=0
move_dir=0
move_to=0
jump_to=0
# 710, 896

def draw_back():
    clear_canvas()
    TUK_ground.draw(back_WIDTH // 2, back_HEIGHT // 2)
    grass.draw(350, 50)
    update_canvas()


def run_draw_move():
    print('move')
    global frame
    draw_back()
    if move_to == 0: #left run
        character.clip_draw(frame * 128, 1280, 128, 130, boshy_ch.X, boshy_ch.Y, 30, 30)
        boshy_ch.X+=move_dir*7
        update_canvas()
        frame = (frame + 1) % 6
    #                      프레임      줄   크기   높이   x   y    w   h
    # 줄 128의 배수
    elif move_to == 1: #right run
        character.clip_draw(frame * 128, 1280, 128, 130, boshy_ch.X, boshy_ch.Y, 30, 30)
        boshy_ch.X += move_dir*7
        update_canvas()
        frame = (frame + 1) % 6+6
    handle_events()

    delay(0.01)

def stay_draw():
    global frame
    draw_back()
    if move_to == 0:  # left run
        frame = 1
        character.clip_draw(frame * 128, 1280, 128, 130,boshy_ch.X, boshy_ch.Y, 30, 30)
        update_canvas()
    #                      프레임      줄   크기   높이   x   y    w   h
    # 줄 128의 배수
    elif move_to == 1:  # right run
        frame = 7
        character.clip_draw(frame * 128, 1280, 128, 130, boshy_ch.X, boshy_ch.Y, 30, 30)
        update_canvas()
    handle_events()
    delay(0.01)
def run_draw_up():
    print('jump')
    global frame
    for boshy_ch.Y in range(boshy_ch.Y,boshy_ch.Y+100,4):
        delay(0.01)
        draw_back()
        if move_to == 0:  # left run
            character.clip_draw(frame * 128, 1280, 128, 130, boshy_ch.X, boshy_ch.Y, 30, 30)
            update_canvas()
            frame = (frame + 1) % 6
    #                      프레임      줄   크기   높이   x   y    w   h
    # 줄 128의 배수
        elif move_to == 1:  # right run
            character.clip_draw(frame * 128, 1280, 128, 130, boshy_ch.X, boshy_ch.Y, 30, 30)
            update_canvas()
            frame = (frame + 1) % 6 + 6

    for boshy_ch.Y in range(boshy_ch.Y,boshy_ch.Y-100,-4):
        delay(0.01)
        draw_back()
        if move_to == 0:  # left run
            character.clip_draw(frame * 128, 1280, 128, 130, boshy_ch.X, boshy_ch.Y, 30, 30)
            update_canvas()
            frame = (frame + 1) % 6
    #                      프레임      줄   크기   높이   x   y    w   h
    # 줄 128의 배수
        elif move_to == 1:  # right run
            character.clip_draw(frame * 128, 1280, 128, 130, boshy_ch.X, boshy_ch.Y, 30, 30)
            update_canvas()
            frame = (frame + 1) % 6 + 6

    handle_events()
    delay(0.1)


def shot():
    draw_back()
    bul.draw()
    bul.update()
    character.clip_draw(frame * 128, 1280, 128, 130, boshy_ch.X, boshy_ch.Y, 30, 30)
    update_canvas()
    delay(0.01)
def run():
    if run_move == 1:
        run_draw_move()
    if run_jump == 1:
        run_draw_up()
    if stay_move == 1:
        stay_draw()


def start_run():
    global frame
    draw_back()
    frame = 7
    character.clip_draw(frame * 128, 1280, 128, 130, boshy_ch.X, boshy_ch.Y, 30, 30)
    update_canvas()

def handle_events():
     global running
     global run_move
     global move_to
     global move_dir
     global stay_move
     global run_jump
     events = get_events()
     for event in events:
         if event.type == SDL_QUIT:
             running = False
         elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_RIGHT:
                stay_move=0
                run_move = 1
                move_to = 1
                move_dir +=1
                run()
            if event.key == SDLK_LEFT:
                stay_move=0
                run_move = 1
                move_to=0
                move_dir -=1
                run()
            if event.key == SDLK_UP:
                stay_move = 0
                run_jump=1
                run()
            elif event.key == SDLK_ESCAPE:
                running = False
         elif event.type == SDL_KEYUP:
              if event.key == SDLK_RIGHT:
                  move_dir -=1
                  run_move = 0
                  stay_move=1
                  run()
              elif event.key == SDLK_LEFT:
                  move_dir += 1
                  run_move = 0
                  stay_move = 1
                  run()
              elif event.key == SDLK_UP:
                  run_jump = 0
                  stay_move = 1





class bullet:
    def __init__(self):
        self.image = load_image('bullet.png')
        self.Sh=0

    def update(self):
        if(self.Sh==50):
            self.Sh=0
        self.Sh+=2
    def draw(self):
        self.image.draw(boshy_ch.X+15+self.Sh,boshy_ch.Y,7,7)
class boshy_ch:
    X: int = 30
    Y: int = 30
    move_to:int =0

open_canvas(back_WIDTH, back_HEIGHT)
grass=load_image('grass1.png')
TUK_ground = load_image('bg2.png')

character = load_image('bosh.png')

running = True
frame=0
bul=bullet()
start_run()
while running:
    shot()
    run()
    handle_events()

    delay(0.03)

close_canvas()




