import pgzrun
import random

TITLE = "good shot game by xavier"
WIDTH = 500
HEIGHT = 500

alien = Actor("alien.png")
def draw():
    screen.clear()
    screen.fill("black")
    alien.draw()
pgzrun.go()