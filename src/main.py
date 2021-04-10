# -*- coding: utf-8 -*-
"""
Created on Sat Feb 13 17:18:22 2021

@author: Nico
"""
import numpy as np
import PCCH
import readfile
import descriptionTrajectoire as dt
from math import sqrt
import game2
import descriptionTrajectoire2
import Traduction
from tools import *    
def main():
    
    file = '../ressource/zone_a_danger(rocher).tmx'
    map = readfile.read_map_tmx(file)
    label = readfile.read_desc_xml('../ressource/descripteur.tsx')
    path = blue_path(map, label)
    #print("Path Blue :", path)
    dt = descriptionTrajectoire2.DescriptionTrajectoire(map, path, label)
    
    description_list = dt.descriptiontTrajectoirePlusExplication(2)
    
    
    print(description_list)
    i = 0
    for gen in description_list:
        print(i,':', gen)
        i+=1

    
    print("\n-----Traduction.Description_to_Txt-----\n")
    print(Traduction.Description_to_Txt2(description_list,label))
    
    """
    print("\n-----Traduction.Description_to_path-----\n")
    Desc_to_path = Traduction.Description_to_path(description_list,path[0])
    print(Desc_to_path)
    print("\nIf initial path == Traduction.Description_to_path\n")
    print(path == Desc_to_path)
    
    
    g = game2.Game(file, map, path, label, 2)
    g.on_execute()
    
    
    start, end = get_start_end(map, label)
    wall = get_wall(map, label)
    weight = get_weight(map, label)
    print(weight)

    path = PCCH.a_start(start, end, len(map),len(map[0]),wall)
    #path = blue_path(map, label)
    print("Path PCCH :", path)
    affichage_console(map, path, label)
    
    path = PCCH.a_start(start, end, len(map),len(map[0]), wall, weight)
    #path = blue_path(map, label)
    print("Path PCCH safe :", path)
    affichage_console(map, path, label)
    
    dt.descriptiontTrajectoire(map,path,label)
    
    
    
    map = readfile.read_map_tmx('../ressource/map1.tmx')
    label = readfile.read_desc_xml('../ressource/descripteur.tsx')
    #print(label)
    start, end = get_start_end(map, label)
    wall = get_wall(map, label)

    #path = PCCH.a_start(start, end, len(map),len(map[0]),wall)
    path = blue_path(map, label)
    print("Path PCCH :", path)
    affichage_console(map, path, label)
    
    d1 = dt.DescriptionTrajectoire(map,path,label)
    d1.descriptiontTrajectoireActif(4)
    """
    
if __name__ == '__main__':
    main()
    map = readfile.read_map_tmx('../ressource/map1.tmx')
    label = readfile.read_desc_xml('../ressource/descripteur.tsx')
    

