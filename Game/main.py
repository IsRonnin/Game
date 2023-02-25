# майн фю.. тьфу блин, мэйн файл!
from pynput import keyboard
from map import Map # Дэкларация неза... Класса Map из файла main.py
from helicopter import Helicopter
from config import *
from clouds import *
import os, time

# Ну пусть логика...

c = Clouds(MAP_W, MAP_H)
m = Map(MAP_H, MAP_W)                        #  ___
false = True # сюда не смотреть! идите дальше! /-_-\
m.generate_forests(3, 10) # генерация леса     \___/
m.generate_rivers(10) # Генерация реки
m.generate_upgrade_shop()
helico = Helicopter(MAP_H, MAP_W)
def process_key(key):
    c = key.char.lower()
    if c in MOVES.keys():
        helico.move(MOVES[c][0], MOVES[c][1])
tick = 0

listner = keyboard.Listener(
    on_release=process_key)
listner.start()

while false:
    os.system("cls")
    m.process_helicopter(helico)
    print("TICK", tick)
    if tick % TREE_UPDATE == 0:
        m.generate_tree()
    if tick % FIRE_UPDATE == 0:
        m.update_fire()
    if tick % CLOUDS_UPDATE == 0:
        c.update()
    m.print_map(helico, c)
    helico.print_stats()
    tick += 1
    time.sleep(TIME_SLEEP) # Приемлемо... 

    
