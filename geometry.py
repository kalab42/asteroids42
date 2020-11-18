import pygame as pg
import numpy as np

class Matrix:
    def rotate(angle):
        return np.array([  
            [math.cos(angle), math.sin(angle), 0],
            [-math.sin(angle), math.cos(angle), 0],
            [0, 0, 1]
            ])
    