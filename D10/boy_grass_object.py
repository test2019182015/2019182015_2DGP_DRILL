from pico2d import *








class Grass:
    def __init__(self):
        self.image = load_image('grass.png')

    def draw(self):
        self.image.draw(400, 30)

class Boy:
    def __init__(self):
        self.x, self.y = 0, 90
        self.frame = 0
        self.image = load_image('run_animation.png')

    def update(self):
        self.frame = (self.frame + 1) % 8
        self.x += 1

    def draw(self):
        self.image.clip_draw(self.frame*100, 0, 100, 100, self.x, self.y)


def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False

boy=None#c에선 널
grass = None
running=True



def enter():
    global grass, running,boy
    boy = Boy()
    grass = Grass()
    running = True

def exit():
    global boy,grass
    del boy
    del grass

# 월드에 존재하는 객체들을 업데이트 한다
def update():
    boy.update()
    #grass는 업데이트가 필요없음


# 월드를 그린다
def draw():
    clear_canvas()
    grass.draw()
    boy.draw()
    update_canvas()

open_canvas()
enter()
while running:
    handle_events()
    update()
    draw()
    delay(0.05)

exit()
# finalization code
close_canvas()
