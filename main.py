import pygame as pg
from player import *

class ApplicationWindow:
    
    def __init__(self):
        succ, fail = pg.init()
        print("successes {0}, failures {1}".format(succ, fail))
        self.FPS = 60
        self.RES = self.width, self.height = 900, 500
        self.surface = pg.display.set_mode(self.RES)
        self.clock = pg.time.Clock()
        self.color = (0, 0, 0)
        self.player = Player(self.width//2, self.height//2, (100, 20, 56))
    
    def draw(self):
        self.surface.fill(self.color)
        self.player.move()
        self.player.clip(self.RES)
        self.player.draw(self.surface)
    
    def chkevent(self):
        for i in pg.event.get():
                if i.type == pg.QUIT:
                    exit()    
        pressed = pg.key.get_pressed()
        if pressed[pg.K_SPACE]:
            self.player.addDeltaV()
    
    def run(self):
        while True:
            print('pos({0};{1})'.format(self.player.px, self.player.py))
            self.draw()
            pg.display.set_caption("FPS: {0}".format(int(self.clock.get_fps())))
            self.chkevent()
            pg.display.flip()
            self.clock.tick(self.FPS)
            self.player.debug()

if __name__ == "__main__":
    wnd = ApplicationWindow()
    wnd.run()