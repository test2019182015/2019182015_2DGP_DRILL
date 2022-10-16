import random
from pico2d import *
from dataclasses import dataclass

back_WIDTH, back_HEIGHT = 600, 600
map_state=1
run_move=0
stay_move=0
run_jump=0
move_dir=0
move_to=1
jump_to=0
jump_tr=2
jump_up=5
jump_now_y1=0
jump_now_y2=0
jump_sta=0
# 710, 896

def draw_back():
    clear_canvas()
    move_map()
    if map_state==1:
        map_1.draw(back_WIDTH // 2, back_HEIGHT // 2,2000,back_HEIGHT)
    elif map_state==2:
        map_2.draw(back_WIDTH // 2, back_HEIGHT // 2, 2000, back_HEIGHT)
    grass.draw(550, 50,1100,200)
    update_canvas()
def move_map():
    global map_state
    if (boshy_ch.X > 1100 and map_state == 1):
        map_state = 2
        boshy_ch.X = 10
    if (boshy_ch.X < 0 and map_state == 2):
        map_state = 1
        boshy_ch.X = 1090
def run_draw_move():
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
def run_draw_up():
    global frame
    global move_to
    global jump_now_x
    global jump_up
    global jump_sta
    global jump_tr
    global run_jump
    handle_events()
    draw_back()
    boshy_ch.Y = boshy_ch.Y + jump_up
    print(jump_now_y2,boshy_ch.Y,jump_up)
    if(boshy_ch.Y < jump_now_y1 + 200):
        if move_to == 0:  # left run
            character.clip_draw(frame * 128, 1280, 128, 130, boshy_ch.X, boshy_ch.Y+jump_up, 30, 30)
            update_canvas()
            frame = (frame + 1) % 6
    #                      프레임      줄   크기   높이   x   y    w   h
    # 줄 128의 배수
        elif move_to == 1:  # right run
            character.clip_draw(frame * 128, 1280, 128, 130, boshy_ch.X, boshy_ch.Y+jump_up, 30, 30)
            update_canvas()
            frame = (frame + 1) % 6 + 6
    elif boshy_ch.Y > jump_now_y1 + 200:
        jump_sta = 1
        jump_up=-5
    if boshy_ch.Y<=jump_now_y2:
        jump_up = 0
        jump_tr=2
        run_jump = 0




def shot():
    bul.draw()
    bul.shot()
    character.clip_draw(frame * 128, 1280, 128, 130, boshy_ch.X, boshy_ch.Y, 30, 30)
    update_canvas()
    handle_events()
def run():
    if run_move == 1:
        run_draw_move()
    if stay_move == 1:
        stay_draw()


def start_run():
    global frame
    draw_back()
    frame = 7
    character.clip_draw(frame * 128, 1280, 128, 130, boshy_ch.X, boshy_ch.Y, 30, 30)
    handle_events()
    update_canvas()

def handle_events():
     global running
     global run_move
     global move_to
     global move_dir
     global stay_move
     global run_jump
     global jump_tr
     global jump_now_x
     global jump_now_y1
     global jump_now_y2
     global jump_up
     global jump_sta
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
                if jump_tr>0:

                    jump_up = 5
                    jump_sta=0
                    jump_tr -= 1
                    jump_now_y1 = boshy_ch.Y
                    if jump_tr==1:
                        jump_now_y2=boshy_ch.Y
                    print(jump_now_y2)
                    stay_move = 0
                    run_jump=2
            if event.key == SDLK_x:
                shot()

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



class bullet:
    def __init__(self):
        self.image = load_image('bullet.png')
        self.Sh=0
        self.st=1
        self.shot_now_x=1
        self.shot_now_y = 0

    def shot(self):
        if self.st==1:
            self.shot_now_x = boshy_ch.X
            self.shot_now_y= boshy_ch.Y
            self.st=0
        if(self.Sh<=1000):
            self.Sh+=3
        if(self.Sh>=1000):
            self.st =1
            self.Sh = 0


    def draw(self):
        draw_back()
        self.image.draw(self.shot_now_x+15+self.Sh,self.shot_now_y,7,7)
        update_canvas()
class boshy_ch:
    X: int = 30
    Y: int = 160
    move_to:int =0

open_canvas(back_WIDTH+500, back_HEIGHT)
grass=load_image('grass1.png')
map_1 = load_image('map_1.png')
map_2 = load_image('map_2.png')
map_3 = load_image('map_3.png')
map_4 = load_image('map_4.png')
map_5 = load_image('map_5.png')
character = load_image('bosh.png')

running = True
frame=0
bul=bullet()
start_run()
while running:
    run()
    handle_events()
    # delay(0.01)
    if run_jump > 0 and jump_tr>=0:
        run_draw_up()
    shot()

close_canvas()




