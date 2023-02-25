from utils import randbool, randcell, randcell2
from config import *


class Map():

    def generate_rivers(self, l):
        rc = randcell(self.h, self.w) # У вас была ошибка в записи т.к. происходила инверсия параметров в следствии чего карта при неравных размерах по координате выдавала ошибку выхода за границу list-а
        rx, ry = rc[0], rc[1]
        self.cells[rx][ry] = 2
        while l > 0:
            rc2 = randcell2(rx,ry)
            rx2, ry2 = rc2[0], rc2[1]
            if self.check_bounds(rx, ry) and self.check_bounds(rx2, ry2):
                self.cells[rx2][ry2] = 2
                rx, ry = rx2, ry2
                l -= 1


    def generate_forests(self, r, rw):
        for ri in range(self.h):
            for ci in range(self.w):
                if randbool(r, rw):
                    self.cells[ri][ci] = 1

    def generate_tree(self): # душнить как при прошлом комите не буду. уже просто лень...
        rc = randcell(self.h, self.w) 
        rx, ry = rc[0], rc[1]
        if self.check_bounds(rx, ry) and self.cells[rx][ry] == 0:
            self.cells[rx][ry] = 1 


    def print_map(self, helico, clouds): 
        print(ASSETS[7] * (self.w + 2))
        for ri in range(self.h):
            print(ASSETS[7], end='')
            for ci in range(self.w):
                cell = self.cells[ri][ci]
                if clouds.cells[ri][ci] == 11 and self.cells[ri][ci] in [0, 1]:
                    print(ASSETS[clouds.cells[ri][ci]], end='')
                elif clouds.cells[ri][ci] == 12 and self.cells[ri][ci] in [1, 2]:
                    print(ASSETS[clouds.cells[ri][ci]], end='')
                elif (helico.x == ri and helico.y == ci):
                    print(ASSETS[8], end='')
                elif cell >= 0 and cell < len(ASSETS):
                    print(ASSETS[cell], end='')
            print(ASSETS[7])
        print(ASSETS[7] * (self.w + 2))

    def check_bounds(self, x, y):    
        if x < 0 or y < 0 or x >= self.h or y >= self.w:
            return False
        return True
    
    def add_fire(self):
        rc = randcell(self.h, self.w)
        rx, ry = rc[0], rc[1]
        if self.check_bounds(rx, ry) and self.cells[rx][ry] == 1:
            self.cells[rx][ry] = 5

    def update_fire(self):
        for ri in range(self.w):
            for ci in range(self.h):
                cell = self.cells
                if cell[ri][ci] == 5:
                    cell[ri][ci] = 0
                    self.cells[ri][ci] = cell[ri][ci] # вы пытались присвоить к списку int.

        for _ in range(5):
            self.add_fire() # ай йа йай костыль! незя так! ну... вам незя а мне можно.
    
    def process_helicopter(self, helico):
        if self.cells[helico.x][helico.y] == 2:
            helico.tank = helico.mxtank
        elif self.cells[helico.x][helico.y] == 5 and helico.tank > 0:
            helico.score += TREE_BONUS
            helico.tank -= 1
            self.cells[helico.x][helico.y] = 1
        elif self.cells[helico.x][helico.y] == 4 and helico.score >= (UPGRADE_COST * helico.mxtank ) / 2:
            helico.score -= (UPGRADE_COST * helico.mxtank ) / 2
            helico.mxtank += 1

    
    def generate_upgrade_shop(self):
        rc = randcell(self.h, self.w)
        rx, ry = rc[0], rc[1]
        self.cells[rx][ry] = 4

    def generate_hospital(self):
        rc = randcell(self.h, self.w)
        rx, ry = rc[0], rc[1]
        if self.cells[rx][ry] != 4:
            self.cells[rx][ry] = 3
        else:
            self.generate_hospital()

    def __init__(self, h, w):
        self.w = w
        self.h = h
        self.cells = [[0 for _ in range(w)] for _ in range(h)]

