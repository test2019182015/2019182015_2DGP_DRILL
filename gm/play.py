import random
from pico2d import *
from dataclasses import dataclass
#import map_1_state
back_WIDTH, back_HEIGHT = 600, 600
map_state=1
run_move=None
stay_move=0
run_jump=0
move_dir=0
move_to=1
jump_to=0
jump_tr=2
jump_up=10
jump_now_y1=0
jump_now_y2=0
save_x=0
save_y=0
save_map=0
jump_sta=0
map_4_save = 0
# 710, 896

def map_fir_1_draw():
    map_1.draw(back_WIDTH // 2, back_HEIGHT // 2, 2000, back_HEIGHT)
    grass.draw(550, 0,1100,70)

def map_fir_2_draw():
    map_1.draw(back_WIDTH // 2, back_HEIGHT // 2, 2000, back_HEIGHT)
    niddle.draw(340, 60)
    niddle.draw(400, 60)
    niddle.draw(460, 60)
    niddle.draw(520, 60)
    up_block.draw(800, 220)
    up_block.draw(860, 220)
    up_block.draw(920, 380)
    up_block.draw(980, 380)
    up_block.draw(1040, 380)
    up_block.draw(1100, 380)
    grass.draw(350, 0, 800, 70)


def map_fir_3_draw():
    map_1.draw(back_WIDTH // 2, back_HEIGHT // 2, 2000, back_HEIGHT)
    up_block.draw(0, 380)
    up_block.draw(60, 380)
    up_block.draw(120, 380)
    up_block.draw(180, 380)
    more_jump.draw(500,400,20,20)
    more_jump.draw(650, 400, 20, 20)
    more_jump.draw(800, 400, 20, 20)
    up_block.draw(920, 380)
    up_block.draw(980, 380)
    up_block.draw(1040, 380)
    up_block.draw(1100, 380)


def map_fir_4_draw():
    global map_4_save
    global save_x
    global save_y
    global save_map
    map_1.draw(back_WIDTH // 2, back_HEIGHT // 2, 2000, back_HEIGHT)
    up_block.draw(0, 380)
    up_block.draw(60, 380)
    up_block.draw(120, 380)
    up_block.draw(180, 380)
    up_block.draw(240, 320)
    up_block.draw(300, 320)
    up_block.draw(360, 320)
    if map_state==4:
        if 860>bul.shot_now_x+bul.Sh>820and 480>bul.shot_now_y>400:
            map_4_save=1
            save_x = boshy_ch.X
            save_y = boshy_ch.Y
            save_map = map_state
            print('save')
    if map_4_save==0:
        No_save.draw(860,440,40,40)
    elif map_4_save==1:
        Yes_save.draw(860,440,40,40)

    up_block.draw(860, 380)
    up_block.draw(920, 380)
    up_block.draw(980, 380)
    up_block.draw(1040, 380)
    up_block.draw(1100, 380)


def draw_back():
    clear_canvas()
    move_map()
    if map_state==1:
       map_fir_1_draw()
       #map_1_state.map_fir_1_draw()
    elif map_state==2:
        map_fir_2_draw()
    elif map_state==3:
        map_fir_3_draw()
    elif map_state==4:
        map_fir_4_draw()
    update_canvas()
def move_map():
    global map_state
    if (boshy_ch.X > 1100 and map_state == 1):
        map_state = 2
        boshy_ch.X = 10
    if (boshy_ch.X < 0 and map_state == 2):
        map_state = 1
        boshy_ch.X = 1090
    if (boshy_ch.X > 1100 and map_state == 2):
        map_state = 3
        boshy_ch.X = 10
    if (boshy_ch.X < 0 and map_state == 3):
        map_state = 2
        boshy_ch.X = 1090
    if (boshy_ch.X > 1100 and map_state == 3):
        map_state = 4
        boshy_ch.X = 10
    if (boshy_ch.X < 0 and map_state == 4):
        map_state = 3
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
    if(boshy_ch.Y < jump_now_y1 + 120):
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
    elif boshy_ch.Y > jump_now_y1 + 120:
        jump_sta = 1
        jump_up=-10
    if boshy_ch.Y<=jump_now_y2:
        jump_up = 0
        jump_tr=2
        run_jump = 0




def shot():
  if ballet !=None:
    for bul in ballet:
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
     global shot_on
     global ballet
     global save_x
     global save_y
     global save_map
     global map_state
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
                    jump_up = 10
                    jump_sta=0
                    jump_tr -= 1
                    jump_now_y1 = boshy_ch.Y
                    if jump_tr==1:
                        jump_now_y2=boshy_ch.Y
                    stay_move = 0
                    run_jump=2
            if event.key == SDLK_x:
                shot_on+=1
                ballet = [bul for i in range(shot_on)]
            if event.key == SDLK_r:
                boshy_ch.X=save_x
                boshy_ch.Y=save_y
                map_state=save_map
                print('load')


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
        self.shot_move=0
    def shot(self):
        global shot_on
        global ballet
        if self.st==1:
            self.shot_now_x = boshy_ch.X
            self.shot_now_y = boshy_ch.Y
            self.st-=1
            self.shot_move=move_to
        if(self.Sh<=1000 or self.Sh>=-1000):
            if self.shot_move==0:
                self.Sh -=15
            elif self.shot_move==1:
                self.Sh += 15
        if(self.Sh>=1000 or self.Sh<=-1000):
            self.st =1
            self.Sh = 0
            shot_on-=1
            ballet = [bul for i in range(shot_on)]


    def draw(self):
        draw_back()
        self.image.draw(self.shot_now_x+self.Sh,self.shot_now_y,7,7)
        update_canvas()
class boshy_ch:
    X: int = 30
    Y: int = 350
    move_to:int =0
open_canvas(back_WIDTH+500, back_HEIGHT)
grass=load_image('grass1.png')
map_1 = load_image('map_1.png')
map_2 = load_image('map_2.png')
map_3 = load_image('map_3.png')
map_4 = load_image('map_4.png')
map_5 = load_image('map_5.png')
character = load_image('bosh.png')
up_block=load_image('up_block.png')
niddle= load_image('niddle_test.png')
more_jump=load_image('more_jump.png')
Yes_save=load_image('Yes_save.png')
No_save=load_image('No_save.png')

running = True
frame=0
shot_on = 0
start_run()
bul = bullet()
ballet=None
while running:
    run()
    handle_events()
    # delay(0.01)
    if run_jump > 0 and jump_tr>=0:
        run_draw_up()
    shot()
    delay(0.01)
close_canvas()




