import pygame as pg
import numpy as np
import math

class Matrix:
    @staticmethod
    def rotate(angle):
        return np.array([  
            [math.cos(angle), math.sin(angle), 0],
            [-math.sin(angle), math.cos(angle), 0],
            [0, 0, 1]
            ])
    
    @staticmethod
    def displacement(x, y):
        return np.array([
            [1, 0, 0],
            [0, 1, 0],
            [x, y, 1]
            ])
    
    @staticmethod
    def rotByAxis(angle, POS):
        x, y = POS[0], POS[1]
        return Matrix.displacement(-x, -y) @ Matrix.rotate(angle) @ Matrix.displacement(x, y)