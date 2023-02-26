from utils import randbool, randcell, randcell2
from config import *
import os
class Helicopter:
    tank = 0 # вода
    mxtank = 1 # макс воды
    score = 0 # очки! всем нужны, мне кстати тоже (0-0)
    lifes = 30
    def __init__(self, w, h):
        self.w = w
        self.h = h
        rc = randcell(self.h, self.w)
        rx, ry = rc[0], rc[1]
        self.x, self.y = rx, ry

    # Вот енто стыбжено с lms  
    def move(self, dx, dy):
        nx, ny = dx + self.x, dy + self.y
        if nx >= 0 and ny >= 0 and nx < self.h and ny < self.w:
            self.x, self.y = nx, ny
    def game_over(self):
        os.system('cls')
        print('|Your score',ASSETS[10], self.score, end='|')
        print("\nGame has been over.")
        exit(0)

    def print_stats(self):
        print(ASSETS[9], self.tank, '/', self.mxtank, end='|')
        print(ASSETS[10], self.score, end='|')
        print(ASSETS[13], self.lifes, end = '|')
    
    def export_data(self):
        return {'score': self.score,
                'x': self.x, 'y': self.y,
                'lifes': self.lifes, 'tank': self.tank,
                'mxtank': self.mxtank}

    def import_data(self, data):
        self.score = data['score'] or 0
        self.x = data['x'] or 0
        self.y = data['y'] or 0
        self.lifes = data['lifes'] or 30
        self.tank = data['tank'] or 0
        self.mxtank = data['mxtank'] or 1