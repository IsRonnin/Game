# майн фю.. тьфу блин, мэйн файл!
from pynput import keyboard
from map import Map # Дэкларация неза... Класса Map из файла main.py
from helicopter import Helicopter
from config import *
from clouds import *
import os, time
import json
 
# Ну пусть - логика...
tick = 0
clouds = Clouds(MAP_W, MAP_H)
m = Map(MAP_H, MAP_W)             
helico = Helicopter(MAP_W, MAP_H)

false = True # сюда не смотреть! идите дальше! /-_-\
m.generate_forests(3, 10) # генерация леса     \___/
m.generate_rivers(10) # Генерация реки
m.generate_upgrade_shop()
m.generate_hospital()

def process_key(key):
    global tick
    c = key.char.lower()
    if c in MOVES.keys():
        helico.move(MOVES[c][0], MOVES[c][1])
    if c == 'f':            #Press F... to save!
        data = {'helicopter': helico.export_data(), 'clouds': clouds.export_data(), 'map': m.export_data(), 'tick': tick}
        with open('level.json', 'w') as lvl:
            json.dump(data, lvl)

    if c == 'l':
        with open('level.json', 'r') as lvl:
            data = json.load(lvl)
            m.import_data(data['map'])
            helico.import_data(data['helicopter'])
            clouds.import_data(data['clouds'])
            tick = data['tick'] or 1

listner = keyboard.Listener(
    on_release=process_key)
listner.start()

while false:
    #os.system("cls")
    m.process_helicopter(helico, clouds)
    print("TICK", tick)
    if tick % TREE_UPDATE == 0:
        m.generate_tree()
    if tick % FIRE_UPDATE == 0:
        m.update_fire()
    if tick % CLOUDS_UPDATE == 0:
        clouds.update()
    helico.print_stats()
    print()
    m.print_map(helico, clouds)
    tick += 1
    time.sleep(TIME_SLEEP) # Приемлемо... 

    
