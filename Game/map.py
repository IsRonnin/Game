from utils import randbool

# карта
# 🌳 🌊 🚁 🟩 🔥 🏥 💛 💵 📦 ⚡ 🏆 ⛅ ⬜ ⬛
# 0 поля
# 1 дерево
# 2 река
# 3 госпиталь
# 4 магазин улучшений
# 5 Огонь просто!
# 6 - 7 - граница

ASSETS = "🟩🌳🌊🏥📦🔥⬜⬛" # пак ассетов для кратенькой рисовашки
class Map:

    #def generate_rivers(self):

    def generate_forests(self, r, rw):
        for ri in range(self.h):
            for ci in range(self.w):
                if randbool(r, rw):
                    self.cells[ri][ci] = 1


    def print_map(self):
        print(ASSETS[7] * (self.w + 2))
        for row in self.cells:
            print(ASSETS[7], end='')
            [print(ASSETS[cells], end='')for cells in row] # кратенькая запись рисовашки строк udp(Была написана до того как вы использовали константную запись и опиралась на список) !ЗАЩИТЫ ОТ ДУРАКА (меня...) НЕТ!
            print(ASSETS[7])
        print(ASSETS[7] * (self.w + 2))

    def check_bounds(self, x, y):    
        if x < 0 or y < 0 or x >= self.h or y >= self.w:
            return False
        return True

    def __init__(self, h, w):
        self.w = w
        self.h = h
        self.cells = [[0 for _ in range(w)] for _ in range(h)]

m = Map(10, 15)

# m.print_map()
# m.cells[1][1] = 1
m.cells[3][5] = 2
m.generate_forests(3, 10)
print(m.check_bounds(20, 30))
m.print_map()

