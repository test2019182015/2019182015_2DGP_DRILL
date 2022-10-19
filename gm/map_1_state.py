from pico2d import *

import game_framework
back_WIDTH, back_HEIGHT = 600, 600
def handle_events():
    global running
    events = pico2d.get_events()
    for event in events:
        if event.type == pico2d.SDL_QUIT:
            running = False
        elif event.type == pico2d.SDL_KEYDOWN:
            if event.key == pico2d.SDLK_SPACE:
                pass# game_framework.change_state(play)
open_canvas(1100,600)
def draw():
    map_1.draw(back_WIDTH // 2, back_HEIGHT // 2, 2000, back_HEIGHT)
    map_fir_1_draw()
    update_canvas()



running = True
map_1 = load_image('map_1.png')
niddle= load_image('niddle_test.png')
grass=load_image('grass1.png')
def map_fir_1_draw():
    niddle.draw(340, 60)
    niddle.draw(400, 60)
    niddle.draw(460, 60)
    niddle.draw(520, 60)
    grass.draw(350, 0, 800, 70)


def map_fir_2_draw():
     map_1.draw(back_WIDTH // 2, back_HEIGHT // 2, 2000, back_HEIGHT)
     grass.draw(350, 0, 800, 70)

def map_fir_3_draw():
     map_1.draw(back_WIDTH // 2, back_HEIGHT // 2, 2000, back_HEIGHT)
     grass.draw(350, 0, 800, 70)

def map_fir_4_draw():
     map_1.draw(back_WIDTH // 2, back_HEIGHT // 2, 2000, back_HEIGHT)
     grass.draw(350, 0, 800, 70)
running = True
