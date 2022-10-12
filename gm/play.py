import random
from pico2d import *

TUK_WIDTH, TUK_HEIGHT = 710, 896



# 710, 896
def handle_events():
    global running
    global x, y
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        # elif event.type == SDL_MOUSEMOTION:
        #     x, y = event.x, TUK_HEIGHT - 1 - event.y
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False
    pass




def reset_world():
    global ax,ay
    global t
    global sx,sy

    ax= (random.randint(0, TUK_WIDTH))
    ay = (random.randint(0, TUK_HEIGHT))
    t=0
    sx,sy=x,y
    pass






open_canvas(TUK_WIDTH, TUK_HEIGHT)


TUK_ground = load_image('bg2.png')
character = load_image('bosh.png')
hand = load_image('hand_arrow.png')
running = True
sx, sy = TUK_WIDTH // 2, TUK_HEIGHT // 2
x,y= sx,sy
ax,ay=x,y
frame = 0
hide_cursor()
arrive =True

t=0
def update_world():
    global x,y
    global t
    t +=0.001
    x= (1-t)*sx + t*ax
    y = (1 - t) * sy + t * ay

    if(t>=1.0):
        reset_world()


reset_world()
while running:
    update_world()

    clear_canvas()
    TUK_ground.draw(TUK_WIDTH // 2, TUK_HEIGHT // 2)
    hand.draw_now(ax,ay)
    # if(ax>=x):
    #    character.clip_draw(frame * 100, 100 * 1, 100, 100, x, y)
    # elif(ax<=x):
    #     character.clip_draw(frame * 100, 0 * 1, 100, 100, x, y)
    character.clip_draw(frame * 128, 1280, 128, 130, 400, 400, 30, 30)
    #                      프레임      줄   크기   높이   x   y    w   h
    #줄 128의 배수
    update_canvas()
    frame = (frame + 1) % 12
    handle_events()
    delay(0.1)

close_canvas()




