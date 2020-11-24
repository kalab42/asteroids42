import pygame as pg
import numpy as np
import math
from geometry import *

class Player:
    def __init__(self, px, py, color):
        self.px, self.py = px, py
        self.color = color
        self.playerShapeMatrix = np.array([
            [self.px-10, self.py + 10, 1],
            [self.px, self.py+8, 1],
            [self.px+10, self.py + 10, 1],
            [self.px, self.py - 20, 1]])
        self.sizeY, self.sizeX = self.playerShapeMatrix.shape
        self.playerProj = np.zeros((self.sizeY, self.sizeX-1))
        self.angle = math.pi / 2
        print(self.playerShapeMatrix)
        print()
        print(self.playerProj)
        self.vel = 0.5
        self.vx, self.vy = self.vel * math.cos(self.angle), self.vel * math.sin(self.angle)
        self.deltaV = 0.1
    
    def debug(self):
        print(pg.mouse.get_pos())
        
    def draw(self, surface):
        
        for i in range(0, self.sizeY):
            for j in range(0, self.sizeX-1):
                self.playerProj[i][j] = self.playerShapeMatrix[i][j]
        pg.draw.polygon(surface, self.color, self.playerProj)
    
    def clip(self, RES):
        width, height = RES
        if self.px < 0:
            self.px = width
        elif self.px > width:
            self.px = 0
        if self.py < 0:
            self.py = height
        elif self.py > height:
            self.py = 0    
            
    def move(self):
        print(self.vel)
        #FIXME: добавить угол зрения и угол движения отдельно
        self.px += self.vx
        self.py += self.vy  
        self.playerShapeMatrix = np.array([
            [self.px-10, self.py + 10, 1],
            [self.px, self.py+8, 1],
            [self.px+10, self.py + 10, 1],
            [self.px, self.py - 20, 1]])
        x, y = pg.mouse.get_pos()
        self.angle = math.atan2(y - self.py, x - self.px)
        self.playerShapeMatrix = self.playerShapeMatrix @ Matrix.rotByAxis(self.angle + math.pi/2, (self.px, self.py))
    
    def addDeltaV(self):      
        self.vx += self.deltaV * math.cos(self.angle)
        self.vy += self.deltaV * math.sin(self.angle)
        #self.vel = math.sqrt(self.vx * self.vx + self.vy * self.vy)
