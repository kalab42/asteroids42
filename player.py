import pygame as pg
import numpy as np
from geometry import *

class Player:
    def __init__(self, px, py, color):
        self.px, self.py = px, py
        self.color = color
        self.playerShapeMatrix = np.array([
            [px-10, py + 10],
            [px, py+8],
            [px+10, py + 10],
            [px, py - 20]])
        self.size = self.playerShapeMatrix.shape
        self.sizeX = self.size[1]
        self.sizeY = self.size[0]
        self.playerProj = np.zeros(self.size)
        self.vx, self.vy = 0, 0
        
    def draw(self, surface):
        for i in range(0, self.sizeY):
            for j in range(0, self.sizeX):
                self.playerProj[i][j] = self.playerShapeMatrix[i][j]
        pg.draw.polygon(surface, self.color, self.playerProj)
    
    def clip(self, RES):
        if sefl.px < RES[0]:
            self.px = RES[
    
    def move(self):
        self.px += self.vx
        self.py += self.vy
        self.playerShapeMatrix = np.array([
            [self.px-10, self.py + 10],
            [self.px, self.py+8],
            [self.px+10, self.py + 10],
            [self.px, self.py - 20]])
        
    def delta(self, dvx, dvy):
        self.vx += dvx
        self.vy += dvy