

from pico2d import *
import  game_framework
import title_state
import play_state
# running=True
image=None
logo_time=0.0

def enter():
    global image
    image = load_image('tuk_credit.png')
    pass

def exit():
    global image
    del image
    pass

def update():
    # 로고타임계산하고 그 결과에따라 런닝을 false로
    global logo_time,running
    delay(0.01)
    logo_time+=0.05
    if logo_time>=1.0:
        logo_time=0
        game_framework.change_state(title_state)
    pass

def draw():
    clear_canvas()
    image.draw(400,300)
    update_canvas()
    pass

def handle_events():
    events = get_events()





