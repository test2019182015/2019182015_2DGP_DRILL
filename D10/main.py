import pico2d
import play_state
import logo_state
import title_state
states=[logo_state,title_state,play_state]#모듈을 변수로

pico2d.open_canvas()

for state in states:
    state.enter()
    while state.running:
        state.handle_events()
        state.update()
        state.draw()
    state.exit()
# finalization code
pico2d.close_canvas()