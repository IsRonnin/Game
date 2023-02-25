from utils import randbool, randcell, randcell2
from map import ASSETS
class Helicopter:
    tank = 0 # вода
    mxtank = 1 # макс воды
    score = 0 # очки! всем нужны, мне кстати тоже (0-0)

    def __init__(self, w, h):
        self.w = w
        self.h = h
        rc = randcell(self.h, self.w)
        rx, ry = rc[0], rc[1]
        self.x, self.y = rx, ry
    def move(self, dx, dy):
        nx, ny = dx + self.x, dy + self.y
        if nx >= 0 and ny >= 0 and nx < self.h and ny < self.w:
            self.x, self.y = nx, ny
    
    def print_stats(self):
        print(ASSETS[9], self.tank, '/', self.mxtank, end='|')
        print(ASSETS[10], self.score, end='|')
