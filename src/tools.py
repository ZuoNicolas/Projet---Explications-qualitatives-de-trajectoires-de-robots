import numpy as np
import PCCH

from math import sqrt

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

def get_weight(map,label,alpha=1):
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
                                    res[(x_tmp, y_tmp)] = (radius - sqrt(radius_tmp) + 1)*alpha
                                else:
                                    res[(x_tmp, y_tmp)] +=(radius - sqrt(radius_tmp) + 1)*alpha
    return res

def get_weight_attract(map, label, lobjet, radius = 6, alpha=1):
    res = dict()
    for x in range(len(map)):
        for y in range(len(map[x])):
            name = label.get(map[x][y]).get('name')
            if name in lobjet:
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
                                    res[(x_tmp, y_tmp)] = -(radius - sqrt(radius_tmp) + 1)*alpha
                                else:
                                    res[(x_tmp, y_tmp)] += -(radius - sqrt(radius_tmp) + 1)*alpha
    return res


def get_weight_dist(map, label, alpha=1):
    """
    Attr: 
        alpha : coeff entre 0.01 et 1 donnant l'importance de la distance en %
    Return:
        paths(list(list(tuple))) : la lists des chemins possible avec comme premier chemin le pcch 
        scores(list(tuple(int))) : score optenu pour chaque chemin (dist, danger, danger_max)
    
    """
    res = dict()
    for x in range(len(map)):
        for y in range(len(map[x])):
            res[(x, y)] = alpha
    return res

def fuse_weight(list_dico_weidgh):
    l=list_dico_weidgh[0].copy()
    
    #fusionner avec tout les keys
    for lis in list_dico_weidgh:
        l.update(lis)
    #additionner les valeurs
    for cle in l.keys():
        l[cle]=0
        for lis in list_dico_weidgh:
            if(lis.get(cle) != None):
                l[cle]+=lis[cle]
    return l
    


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

    while not path[-1] == end:
        points= []
        if x+1 < tx and (label.get(map[x+1][y]).get('name') == 'tracé' or (x+1,y) == start or (x+1,y) == end) and (x+1,y) not in path:
            points.append((x+1,y))
        if x-1 >= 0 and (label.get(map[x-1][y]).get('name') == 'tracé' or (x-1,y) == start or (x-1,y) == end) and (x-1,y) not in path:
            points.append((x-1,y))
        if y+1 < ty and (label.get(map[x][y+1]).get('name') == 'tracé' or (x,y+1) == start or (x,y+1) == end) and (x,y+1) not in path:
            points.append((x,y+1))
        if y-1 >= 0 and (label.get(map[x][y-1]).get('name') == 'tracé' or (x,y-1) == start or (x,y-1) == end) and (x,y-1) not in path:
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
    return []

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
            if any((x+1,y) in p for p in paths) or (x+1,y) == start or (x+1,y) == end:
                tmp+=1
            if any((x-1,y) in sublist for sublist in paths) or (x-1,y) == start or (x-1,y) == end:
                tmp+=1
            if any((x,y+1) in sublist for sublist in paths) or (x,y+1) == start or (x,y+1) == end:
                tmp+=1
            if any((x,y-1) in sublist for sublist in paths) or (x,y-1) == start or (x,y-1) == end:
                tmp+=1
            if tmp >= 3 and (x,y) not in inter:
                inter.append((x,y))
            
    return inter


def path_by_retriction(map, label, ltuple_rest, lobjet=[]):
    """
    Attr: 
        map : la carte 
        label : les labels
        tuple_rest(list(tuple)) : list avec les tuples des restriction (dist, danger)
    Return:
        paths(list(list(tuple))) : la lists des chemins possible avec comme premier chemin le pcch 
        scores(list(tuple(int))) : score optenu pour chaque chemin (dist, danger, danger_max)
    """
    start, end = get_start_end(map, label)
    wall = get_wall(map, label)
    weight = get_weight(map, label)
    val_attract = 7

    path, score = PCCH.a_start(start, end, len(map), len(map[0]), wall)
    path2, score2 = PCCH.a_start(start, end, len(map), len(map[0]), wall, weight)
    paths = [path] * len(ltuple_rest) + [path2] * len(ltuple_rest)
    path_weight = [0 if weight.get(pos) == None else weight.get(pos) for pos in path]
    path_weight2 = [0 if weight.get(pos) == None else weight.get(pos) for pos in path2]
    
    

    lsomme_attract = []
    lsomme_attract2 = []
    for restriction in ltuple_rest:
        weight_attract = get_weight_attract(map, label, lobjet, 1, restriction[2] * val_attract)
        path_weight_atrract = [0 if weight_attract.get(pos) == None else weight_attract.get(pos) for pos in path]
        lsomme_attract.append(np.sum(path_weight_atrract))
        path_weight_atrract2 = [0 if weight_attract.get(pos) == None else weight_attract.get(pos) for pos in path2]
        lsomme_attract2.append(np.sum(path_weight_atrract2))


    somme, taille, maxi = np.sum(path_weight),len(path), np.max(path_weight)
    somme2, taille2, maxi2 = np.sum(path_weight2),len(path2), np.max(path_weight2)
    scores = [(score * ltuple_rest[i][0] + somme * ltuple_rest[i][1] + lsomme_attract[i] * ltuple_rest[i][2], somme, taille, lsomme_attract[i]) for i in range(len(ltuple_rest))]
    scores += [(score2 * ltuple_rest[i][0] + somme2 * ltuple_rest[i][1] + lsomme_attract2[i] * ltuple_rest[i][2], somme2, taille2, lsomme_attract2[i]) for i in range(len(ltuple_rest))]
    
    for restriction in ltuple_rest:
        weight_secu = get_weight(map, label, restriction[1])
        weight_dist = get_weight_dist(map, label, restriction[0])
        weight_rest = fuse_weight([weight_dist, weight_secu])
        
        weight_attract = get_weight_attract(map, label, lobjet, 1, restriction[2] * val_attract)
        weight_rest = fuse_weight([weight_rest, weight_attract])
        

        path, score = PCCH.a_start(start, end, len(map), len(map[0]), wall, weight_rest)
        paths.append(path)

        path_weight_attract = [0 if weight_attract.get(pos) == None else weight_attract.get(pos) for pos in path]
        print(path)
        print(weight_attract)
        print(path_weight_attract)

        path_weight = [0 if weight.get(pos) == None else weight.get(pos) for pos in path]
        scores.append((score, np.sum(path_weight), len(path), np.sum(path_weight_attract)))
    return paths, scores

def Bellman_Ford(map, label, weight):
    start, end = get_start_end(map, label)
    c, l = np.shape(map)

    d = np.ones((c,l)) * np.inf
    
    d[start[0]][start[1]] = 0
    
    for x in range(c):
        for y in range(l):
            if x+1 < tx and label.get(map[x+1][y]).get('name') == 'tracé' and (x+1,y) not in path:
                d[x][y] = min(d[x][y], d[x+1][y] + weight.get((x, y)))
            elif x-1 >= 0 and label.get(map[x-1][y]).get('name') == 'tracé' and (x-1,y) not in path:
                d[x][y] = min(d[x][y], d[x-1][y] + weight.get((x, y)))
            elif y+1 < ty and label.get(map[x][y+1]).get('name') == 'tracé' and (x,y+1) not in path:
                d[x][y] = min(d[x][y], d[x][y+1] + weight.get((x, y)))
            elif y-1 >= 0 and label.get(map[x][y-1]).get('name') == 'tracé' and (x,y-1) not in path:
                d[x][y] = min(d[x][y], d[x][y-1] + weight.get((x, y)))
            
    return d