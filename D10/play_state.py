from pico2d import *
import game_framework
import title_state
import item_state
import add_delete_boy
import random
import logo_state
team=None
num=1
class Grass:
    def __init__(self):
        self.image = load_image('grass.png')

    def draw(self):
        self.image.draw(400, 30)

class Boy:
    def __init__(self):
        self.x, self.y =  random.randint(100, 700), 90
        self.frame = 0
        self.image = load_image('animation_sheet.png')
        self.dir =1
        self.ball_image = load_image('ball21x21.png')
        self.big_ball_image = load_image('ball41x41.png')


        self.item = None


    def update(self):
        self.frame = (self.frame + 1) % 8
        self.x += self.dir*3
        if self.x>800:
            self.x=800
            self.dir=-1
        elif self.x<0:
            self.x=0
            self.dir=1

    def draw(self):
        if self.dir==1:
            self.image.clip_draw(self.frame*100, 100, 100, 100, self.x, self.y)
        elif self.dir==-1:
            self.image.clip_draw(self.frame*100, 0, 100, 100, self.x, self.y)
        if self.item == 'BigBall':
            self.big_ball_image.draw(self.x+10,self.y+50)
        if self.item == 'Ball':
            self.ball_image.draw(self.x+10,self.y+50)



def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_ESCAPE:
                game_framework.change_state(title_state)
            elif event.key==SDLK_i:
                game_framework.push_state(item_state)
            elif event.key==SDLK_b:
                game_framework.push_state(add_delete_boy)
    delay(0.01)

boy=None#c에선 널
grass = None
# running=True


def enter():
    global grass, running,boy
    global team
    boy = Boy()
    grass = Grass()
    team = [Boy() for i in range(num)]
    running = True

def exit():
    global boy,grass
    del boy
    del grass

# 월드에 존재하는 객체들을 업데이트 한다
def update():
    print(num)
    for boy in team:
        boy.update()
    #grass는 업데이트가 필요없음


# 월드를 그린다
def draw():
    clear_canvas()
    draw_world()
    update_canvas()


def draw_world():
    grass.draw()
    for boy in team:
       boy.draw()


def pause():
    pass

def resume():
    pass

def add():
    global team
    team = [Boy() for i in range(num)]
    pass

