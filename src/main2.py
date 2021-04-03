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

def get_start_end(map,label):

    for key in label.keys():
        if label.get(key).get('name')=='start':
            start = ( np.where(map==key)[0][0] ,
                      np.where(map==key)[1][0] )
        if label.get(key).get('name')=='end' :
            end = ( np.where(map==key)[0][0] ,
                      np.where(map==key)[1][0] )
    return start, end

def get_wall(map,label):
    wall=[]
    
    for x in range(len(map)):
        for y in range(len(map[x])):
            if not( label.get(map[x][y]).get('canPass') or \
                   label.get(map[x][y]).get('name') == 'start' or \
                   label.get(map[x][y]).get('name') == 'end' ):
                
                wall.append((x,y))
                
    return wall

def get_weight(map,label):
    res = dict()
    for x in range(len(map)):
        for y in range(len(map[x])):
            radius = label.get(map[x][y]).get('danger_area')
            if radius != None:
                radius = int(radius)
                for x2 in range(-radius,radius+1):
                    for y2 in range(-radius,radius+1):
                        x_tmp = x + x2
                        y_tmp = y + y2
                        radius_tmp = (x- x_tmp)**2 + (y-y_tmp)**2
                        #si on est dans la zone
                        if radius_tmp <= radius**2: 
                            # si on ne sort pas de la map
                            if x_tmp >= 0 and y_tmp >= 0 and x_tmp < len(map[x]) and y_tmp < len(map[x]): 
                                if res.get((x_tmp, y_tmp)) == None:
                                    res[(x_tmp, y_tmp)] = radius - sqrt(radius_tmp)
                                else:
                                    res[(x_tmp, y_tmp)] += radius - sqrt(radius_tmp)
    return res


def affichage_console(map,path,label):
    
    print('S = start    E = End     str = mur     chemin = *')
    for x in range(len(map)):
        print('[',end='')
        for y in range(len(map[x])):
            if not( label.get(map[x][y]).get('canPass') or 
                   label.get(map[x][y]).get('name') == 'start' or 
                   label.get(map[x][y]).get('name') == 'end' ):
                print(label.get(map[x][y]).get('name')[0],end='')
            else:
                b=True
                for i,j in path:
                    if x == path[0][0] and y == path[0][1]:
                        print('S',end='')
                        b=False
                        break;
                    elif x == path[-1][0] and y == path[-1][1]:
                        print('E',end='')
                        b=False
                        break;
                    elif i==x and j==y:
                        print('*',end='')
                        b=False
                        break;
                if b:
                    print(' ',end='')
                
        print(']')
        
def affichage_des_walls(wall,x,y):
    
    for i in range(x):
        for j in range(y):
            if (i,j) in wall:
                print(0,end='')
            else:
                print(1,end='')
        print()
        
def blue_path(map,label):
    start, end = get_start_end(map,label)
    x, y = start
    point =()
    path=[start]
    tx = len(map)
    ty = len(map[0])
    
    while True:
        if x+1 < tx and label.get(map[x+1][y]).get('name') == 'tracé' and (x+1,y) not in path:
            point = (x+1,y)
        elif x-1 >= 0 and label.get(map[x-1][y]).get('name') == 'tracé' and (x-1,y) not in path:
            point = (x-1,y)
        elif y+1 < ty and label.get(map[x][y+1]).get('name') == 'tracé' and (x,y+1) not in path:
            point = (x,y+1)
        elif y-1 >= 0 and label.get(map[x][y-1]).get('name') == 'tracé' and (x,y-1) not in path:
            point = (x,y-1)
        else:
            break
        x, y = point
        path.append(point)
        
    path.append(end)
    
    return path
        


def blue_path2(map, label, path = []):
    start, end = get_start_end(map,label)
    if len(path)== 0: 
        path=[start]
    x, y = path[-1]
    tx = len(map)
    ty = len(map[0])
    
    new_path = False

    while not (x,y) == end:
        points= []
        if x+1 < tx and (label.get(map[x+1][y]).get('name') == 'tracé' or (x+1,y) == start or (x+1,y) == end) and (x+1,y) not in path:
            points.append((x+1,y))
        if x-1 >= 0 and (label.get(map[x-1][y]).get('name') == 'tracé' or (x+1,y) == start or (x+1,y) == end) and (x-1,y) not in path:
            points.append((x-1,y))
        if y+1 < ty and (label.get(map[x][y+1]).get('name') == 'tracé' or (x+1,y) == start or (x+1,y) == end) and (x,y+1) not in path:
            points.append((x,y+1))
        if y-1 >= 0 and (label.get(map[x][y-1]).get('name') == 'tracé' or (x+1,y) == start or (x+1,y) == end) and (x,y-1) not in path:
            points.append((x,y-1))
        if len(points) > 1:
            path_tmp = path.copy()
            path = []
            for point in points:
                path_tmp = path_tmp.copy()
                res_tmp = blue_path2(map, label, path_tmp + [point])
                for res in res_tmp:
                    path.append(res)
            return path
        elif len(points) == 1:
            x, y = points[0]
            path.append(points[0])
        else:
            break
    if path[-1] == end:
        return [path]
    return [path]

def transform_wall(map,label, path):
    wall=[]
    path = [elem for e in path for elem in e]
    for x in range(len(map)):
        for y in range(len(map[x])):
            if (x,y) not in path:
                wall.append((x,y))
                
    return wall


def find_intercection(map, label, paths):
    inter = []
    start, end = get_start_end(map,label)
    tx = len(map)
    ty = len(map[0])
    for path in paths: # pour chaque chemin
        for x, y in path:
            tmp = 0
            if x+1 < tx and (label.get(map[x+1][y]).get('name') == 'tracé' or (x+1,y) == start or (x+1,y) == end):
                tmp+=1
            if x-1 >= 0 and (label.get(map[x-1][y]).get('name') == 'tracé' or (x-1,y) == start or (x-1,y) == end):
                tmp+=1
            if y+1 < ty and (label.get(map[x][y+1]).get('name') == 'tracé' or (x,y+1) == start or (x,y+1) == end):
                tmp+=1
            if y-1 >= 0 and (label.get(map[x][y-1]).get('name') == 'tracé' or (x,y-1) == start or (x,y-1) == end):
                tmp+=1
            if tmp >= 3 and (x,y) not in inter:
                inter.append((x,y))
            
    return inter




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
    print("Path Blue v2 :", paths, np.shape(paths))
    wall = transform_wall(map, label, paths)
    print("Wall = ", wall)

    print("=>",find_intercection(map, label, paths))

    ##a* classique
    path1 = [PCCH.a_start(start, end, len(map), len(map[0]), wall)]
    print("Path PCCH :", path1)

    ##a* avec changement de poid
    path2 = [PCCH.a_start(start, end, len(map),len(map[0]), wall, weight)]
    print("Path PCCH safe :", path2)

    res = (path1, path2, paths)
    
    paths = res[1]

    with_game = True


    for path in paths:

        if with_game:
            g = game.Game(file, map, path, label, 2)
            g.on_execute()
        
        print("                 ====                         ",path,len(path))
        dt = descriptionTrajectoire2.DescriptionTrajectoire(map, path, label)
    
        dt.descriptiontTrajectoireSimple(2)


        affichage_console(map, path, label)
        
    
if __name__ == '__main__':
    main()
    map = readfile.read_map_tmx('../ressource/map1.tmx')
    label = readfile.read_desc_xml('../ressource/descripteur.tsx')
    

