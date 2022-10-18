from pico2d import *
back_WIDTH, back_HEIGHT = 600, 600
map_1 = load_image('map_1.png')
niddle= load_image('niddle_test.png')
def map_fir_1_draw():
    map_1.draw(back_WIDTH // 2, back_HEIGHT // 2, 2000, back_HEIGHT)
    niddle.draw(340, 60)
    niddle.draw(400, 60)
    niddle.draw(460, 60)
    niddle.draw(520, 60)

def map_fir_2_draw():
    map_1.draw(back_WIDTH // 2, back_HEIGHT // 2, 2000, back_HEIGHT)

def map_fir_3_draw():
    map_1.draw(back_WIDTH // 2, back_HEIGHT // 2, 2000, back_HEIGHT)

def map_fir_4_draw():
    map_1.draw(back_WIDTH // 2, back_HEIGHT // 2, 2000, back_HEIGHT)