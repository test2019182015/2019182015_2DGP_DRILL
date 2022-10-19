

from pico2d import *
import  game_framework
import title_state
import play_state
# running=True
image=None
def pause():
    pass
def enter():
    global image
    image = load_image('item_select.png')
    pass

def exit():
    global image
    del image

def update():
    play_state.update()
    pass

def draw():
    clear_canvas()
    play_state.draw_world()
    image.draw(400,300)
    update_canvas()

def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_ESCAPE:
                game_framework.pop_state()#이전상태인 플레이 스테이트로 복귀
            match event.key:
                case pico2d.SDLK_0:
                    play_state.boy.item=None
                    game_framework.pop_state()
                    break
                case pico2d.SDLK_1:
                    play_state.boy.item='Ball'
                    game_framework.pop_state()
                    break
                case pico2d.SDLK_2:
                    play_state.boy.item='BigBall'
                    game_framework.pop_state()
                    break





