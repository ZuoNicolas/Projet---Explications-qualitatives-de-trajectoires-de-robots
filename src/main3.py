import numpy as np
import PCCH
import readfile
import descriptionTrajectoire as dt
from math import sqrt
import game2
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
    g = game2.Game(file, map, label, 2)
    g.on_execute()
    
    
if __name__ == '__main__':
    main()
    map = readfile.read_map_tmx('../ressource/zone_a_danger(rocher).tmx')
    label = readfile.read_desc_xml('../ressource/descripteur.tsx')
   