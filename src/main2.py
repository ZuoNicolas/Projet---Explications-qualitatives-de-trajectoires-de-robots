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
import game
import descriptionTrajectoire2
from tools import * 


def main():

    ### les fichiers disponible
    ## plusieur chemin
    #file = '../ressource/zone_non_carre2.tmx'
    ## plusieur chemin avec un rocher
    file = '../ressource/zone_non carre.tmx'
    
    ## zone tres simple
    #file = '../ressource/map1.tmx'
    
    ## pres
    #file = '../ressource/exemple1.tmx'
    
    ## rocher
    #file = '../ressource/zone_a_danger(rocher).tmx'
    
    #initialisation des données
    map = readfile.read_map_tmx(file)
    label = readfile.read_desc_xml('../ressource/descripteur.tsx')
    start, end = get_start_end(map, label)
    print("Start", start, "end", end)
    wall = get_wall(map, label)
    weight = get_weight(map, label)

    ###choix du moyen de recuperer les chemin
    # chemin bleu
    paths = blue_path2(map, label)
    #print("Path Blue v2 :", paths, np.shape(paths))
    wall = transform_wall(map, label, paths)
    print("Wall = ", wall)

    print("=>",find_intercection(map, label, paths))
    affichage_console(map, find_intercection(map, label, paths), label)     

    ##a* classique
    path1, score1 = PCCH.a_start(start, end, len(map), len(map[0]), wall)
    path1 = [path1]
    print("Path PCCH :", path1)
    print("score PCCH :", score1)


    ##a* avec changement de poid
    path2 , score2 = PCCH.a_start(start, end, len(map),len(map[0]), wall, weight)
    path2 = [path2]
    #print("Path PCCH safe :", path2)
    print("score PCCH :", score2)

    res = (path1, path2, paths) # a* a* safe toutles chemin par blue path
    
    paths = res[1]

    with_game = True


    for path in paths:

        if with_game:
            g = game.Game(file, map, path, label, 2)
            g.on_execute()
        
        dt = descriptionTrajectoire2.DescriptionTrajectoire(map, path, label)
    
        dt.descriptiontTrajectoireSimple(2)


        affichage_console(map, path, label)

    
    
if __name__ == '__main__':
    main()
    map = readfile.read_map_tmx('../ressource/map1.tmx')
    label = readfile.read_desc_xml('../ressource/descripteur.tsx')
    

