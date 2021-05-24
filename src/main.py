import numpy as np
import PCCH
import readfile
import descriptionTrajectoire as dt
from math import sqrt
import game
import descriptionTrajectoire
from tools import * 


def main():

    ### les fichiers disponible
    ## plusieur chemin
    file = '../ressource/monde1.tmx'

    
    #initialisation des données
    map = readfile.read_map_tmx(file)
    label = readfile.read_desc_xml('../ressource/descripteur.tsx')
    g = game.Game(file, map, label, 2)
    g.on_execute()
    
    
if __name__ == '__main__':
    main()
   