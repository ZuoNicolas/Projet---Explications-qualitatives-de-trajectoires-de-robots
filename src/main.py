# -*- coding: utf-8 -*-
"""
Created on Sat Feb 13 17:18:22 2021

@author: Nico
"""
import numpy as np
import PCCH
import readfile

def get_start_end(map,label):
    for key in label.keys():
        if label.get(key).get('name')=='point depart':
            start = ( np.where(map==key)[0][0] ,
                      np.where(map==key)[1][0] )
        if label.get(key).get('name')=='point arriver' :
            end = ( np.where(map==key)[0][0] ,
                      np.where(map==key)[1][0] )
    return start, end

def get_wall(map,label):
    wall=[]
    
    for x in range(len(map)):
        for y in range(len(map[x])):
            if not( label.get(map[x][y]).get('canPass') or \
                   label.get(map[x][y]).get('name') == 'point depart' or \
                   label.get(map[x][y]).get('name') == 'point arriver' ):
                
                wall.append((x,y))
                
    return wall

def affichage_console(map,path,label):
    
    print('S = start    E = End     mur = |     chemin = *')
    for x in range(len(map)):
        print('[',end='')
        for y in range(len(map[x])):
            if not( label.get(map[x][y]).get('canPass') or 
                   label.get(map[x][y]).get('name') == 'point depart' or 
                   label.get(map[x][y]).get('name') == 'point arriver' ):
                print('|',end='')
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
        
def main():
    
    map = readfile.read_map_csv('../ressource/map.csv')
    label = readfile.read_desc_xml('../ressource/propriete.tsx')
    
    start, end = get_start_end(map, label)
    wall = get_wall(map, label)


    path = PCCH.a_start(start, end, len(map),len(map[0]),wall)
    #print("Path PCCH :", path)
    affichage_console(map, path, label)
    
if __name__ == '__main__':
    main()