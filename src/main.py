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
        
def main():
    
    file = '../ressource/exemple1.tmx'
    map = readfile.read_map_tmx(file)
    label = readfile.read_desc_xml('../ressource/descripteur.tsx')
    path = blue_path(map, label)
    #print("Path Blue :", path)
    dt = descriptionTrajectoire2.DescriptionTrajectoire(map, path, label)
    
    description_list = dt.descriptiontTrajectoireSimple(2)
    
    #print(description_list)
    #print(Traduction.Description_to_Txt(description_list,label))
    #print(Traduction.Description_to_path(description_list,path[0]))
    
    
    g = game2.Game(file, map, path, label, 2)
    g.on_execute()
    """

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
    

