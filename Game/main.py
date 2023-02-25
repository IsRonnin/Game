# майн фю.. тьфу блин, мэйн файл!
from pynput import keyboard
from map import Map # Дэкларация неза... Класса Map из файла main.py
from helicopter import Helicopter
import os, time
TIME_SLEEP = 0.1 # Время на сон после кадра
TREE_UPDATE = 50
FIRE_UPDATE = 75
MAP_W, MAP_H = 10, 10
MOVES = {'w': (-1, 0), 'd': (0, 1), 's': (1,0), 'a': (0, -1)}

# Ну пусть логика...
def process_key(key):
    c = key.char.lower()
    if c in MOVES.keys():
        helico.move(MOVES[c][0], MOVES[c][1])

listner = keyboard.Listener(
    on_release=process_key)
listner.start()

m = Map(MAP_H, MAP_W) # Не обращайте внимания - Эксперементы с классами по идее лучше просто создать Config.txt но... "лень"
false = True # сюда не смотреть! идите дальше! /-_-\
m.generate_forests(3, 10) # генерация леса
m.generate_rivers(10) # Генерация реки
helico = Helicopter(MAP_H, MAP_W)

tick = 0

while false:
    os.system("cls")
    print("TICK", tick)
    if tick % TREE_UPDATE == 0:
        m.generate_tree()
    if tick % FIRE_UPDATE == 0:
        m.update_fire()
    m.print_map(helico)
    helico.print_stats()
    tick += 1
    time.sleep(TIME_SLEEP) # Приемлемо... 

    
