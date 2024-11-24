import pgzrun
import random

TITLE = "shoot the alien"
WIDTH = 840
HEIGHT = 620

alien = Actor("alien")
alien.pos = (
    random.randint(100,WIDTH-100),
    random.randint(100,HEIGHT-100)
)
message = ""

def draw():
    screen.clear()
    screen.fill(color=(100,0,0))
    screen.draw.text(message, center=(WIDTH/2,HEIGHT/2), fontsize=40)
    alien.draw()


def on_mouse_down(pos):
    global message
    if alien.collidepoint(pos):
        message = "good shot"
        alien.pos = (
            random.randint(100,WIDTH-100),
            random.randint(100,HEIGHT-100)
        )
    else:
        message = "you missed"

pgzrun.go()