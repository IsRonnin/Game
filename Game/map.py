from utils import randbool, randcell, randcell2
# карта
# 🌳 🌊 🚁 🟩 🔥 🏥 💛 💵 📦 ⚡ 🏆 ⛅ ⬜ ⬛ 🪣
# 0 поля
# 1 дерево
# 2 река
# 3 госпиталь
# 4 магазин улучшений
# 5 Огонь просто!
# 6 - 7 - граница
# 8 Хеликоптер Хеликоптер!
# 9 ведёрко!
# 10 искал медь а нашёл золото ;3

ASSETS = "🟩🌳🌊🏥📦🔥⬜⬛🚁🪣🏆" # пак ассетов для кратенькой рисовашки
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


    def print_map(self, helico): 

        print(ASSETS[7] * (self.w + 2))
        for ri in range(self.h):
            print(ASSETS[7], end='')
            [print(ASSETS[8] if (helico.x == ri and helico.y == ci)
                    else ASSETS[self.cells[ri][ci]], end='') for ci in range(self.w)] 
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

    def __init__(self, h, w):
        self.w = w
        self.h = h
        self.cells = [[0 for _ in range(w)] for _ in range(h)]

