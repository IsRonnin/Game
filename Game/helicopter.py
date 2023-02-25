from utils import randbool, randcell, randcell2

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
        # Походу полётов не будет...
