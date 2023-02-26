from utils import randbool
from config import *

class Clouds:
    def __init__(self, w, h):
        self.w = w
        self.h = h
        self.cells = [[0 for _ in range(w)] for _ in range(h)]
    def update(self, r = 2, rw = 10, g = 1, gw = 10):
        for ri in range(self.h):
            for ci in range(self.w):
                if randbool(r, rw):
                    self.cells[ri][ci] = 11
                    if randbool(g, gw):
                        self.cells[ri][ci] = 12
                else:
                    self.cells[ri][ci] = 0
    def export_data(self):
        return {'cells': self.cells}
    
    def import_data(self, data):
        self.cells = data['cells'] or [[0 for _ in range(self.w)] for _ in range(self.h)]                