

from pico2d import *
import  game_framework
import title_state
import play_state
# running=True
image=None

def enter():
    global image
    image = load_image('add_delete_boy.png')
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
                case pico2d.SDLK_j:
                    play_state.num+=1
                    game_framework.pop_state()
                    play_state.add()
                    break
                case pico2d.SDLK_k:
                    if play_state.num>1:
                        play_state.num-=1
                        game_framework.pop_state()
                        play_state.add()
                        break





