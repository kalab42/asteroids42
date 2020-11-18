import numpy as np
import pygame as pg


x = 40
y = 40

borderx = 100
bordery = 100


def move(dx, dy):
    x += dx
    y += dy

if __name__ == "__main__":
    pg.init()
    while True:
        for i in pg.event.get():
            if i.type == pg.QUIT:
                exit()
            elif i.type == pg.KEYDOWN:
                if i.key == pg.K_w:
                    move(0, -1)
                elif i.key == pg.K_d:
                    move(1, 0)
                elif i.key == pg.K_s:
                    move(0, 1)
                elif i.key == pg.K_q:
                    move(-1, 0)
    print("({0};{1})".format(x, y))