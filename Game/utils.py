from random import randint as rand

def randbool(r, mxr): # Лямбду в студию! lambda r, mxr: rand(0, mxr) <= r
    t = rand(0, mxr)
    return t <= r

def randcell(w, h): # также как и выше можно впихнуть и в лямбду? lambda w, h: (rand(0, w-1), rand(0, h-1))
    tw = rand(0, w-1)
    wh = rand(0, h-1)
    return(tw, wh)

# Памятка 0 - вверх! 1 - Право руля! 2 - ВНИЗ! 3 - все ходят налево!

def randcell2(x, y): # здесь возмущатся не буду в лямду пихать уже не удобно - много буков!
    moves = [[-1,0], [0,1], [1, 0], [0,-1]] # хм это же можно и генерировать не?
    t = rand(0, 3)
    dx, dy = moves[t][0], moves[t][1] # Вах а тут красиво записано!
    return (x + dx, y + dy)


