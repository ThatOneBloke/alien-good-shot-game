import pgzrun
import random

TITLE = "good shot game by xavier"
WIDTH = 500
HEIGHT = 500
message = ""
score = 0

alien = Actor("alien.png")
def draw():
    screen.clear()
    screen.fill("black")
    alien.draw()
    screen.draw.text(message, (300, 100), color = "white", fontsize = 40)
    screen.draw.text(str(score), (300, 150), color = "white", fontsize = 40)

def placealien():
    alien.x = random.randint(50, 450)
    alien.y = random.randint(50, 450)

def on_mouse_down(pos):
    global message
    global score
    if alien.collidepoint(pos):
        placealien()
        message = "good shot"
        score = score + 1
    else:
        message = "missed shot"
        score = score - 1

placealien()
pgzrun.go()
