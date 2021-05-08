import numpy as np
import PCCH

from math import sqrt

def get_start_end(map,label):
    """ trouve le départ et la fin
    Attr: 
        map : la carte 
        label : les labels
    Return:
        start(str) : la case de départ
        end(str) : la case de fin
    """
    for key in label.keys():
        if label.get(key).get('name')=='start':
            start = ( np.where(map==key)[0][0] ,
                      np.where(map==key)[1][0] )
        if label.get(key).get('name')=='end' :
            end = ( np.where(map==key)[0][0] ,
                      np.where(map==key)[1][0] )
    return start, end

def get_wall(map,label):
    """ trouve tous les murs
    Attr: 
        map : la carte 
        label : les labels
    Return:
        res (dict(str, int)) : les case qui sont des mur
    """
    wall=[]
    
    for x in range(len(map)):
        for y in range(len(map[x])):
            if not( label.get(map[x][y]).get('canPass') or \
                   label.get(map[x][y]).get('name') == 'start' or \
                   label.get(map[x][y]).get('name') == 'end' ):
                
                wall.append((x,y))
                
    return wall

def get_weight(map,label,alpha=1):
    """ met un poid de dangerosité pour toutes les cases
    Attr: 
        map : la carte 
        label : les labels
    Return:
        res (dict(str, int)) : les poid des cases.
    """
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
                                    res[(x_tmp, y_tmp)] = max(res[(x_tmp, y_tmp)], (radius - sqrt(radius_tmp) + 1)*alpha)
    return res

def get_weight_attract(map, label, lobjet, radius = 6, alpha=1):
    """ met un poid des points d'interet pour toutes les cases
    Attr: 
        map : la carte 
        label : les labels
        alpha : coeff entre 0 et 1 donnant l'importance de la distance en %
    Return:
        res (dict(str, int)) : les poid des cases.
    """
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
    """ met un poid de distance pour toutes les cases
    Attr: 
        map : la carte 
        label : les labels
        alpha : coeff entre 0 et 1 donnant l'importance de la distance en %
    Return:
        res (dict(str, int)) : les poid des cases.
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
    """ affiche sur la console la carte avec le chemin.
    Attr: 
        map : la carte 
        path(list(str)) : le tracé.
        label : les labels
    Return:
        NoneType
    """
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
    """ affiche sur la console les zone mur(0) et non mur(1)
    Attr: 
        map : la carte 
        x(int) = longueur
        y(int) = hauteur
    Return:
        NoneType
    """
    for i in range(x):
        for j in range(y):
            if (i,j) in wall:
                print(0,end='')
            else:
                print(1,end='')
        print()
        
def blue_path(map,label):
    """ trouve toules chemin posible pour un tracé dessiner à l'avance sur la carte
    Attr: 
        map : la carte 
        label : les labels
    Return:
        path(list(list(str))) : les chemins.
    """
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
    """ trouve toules chemin posible pour un tracé dessiner à l'avance sur la carte
    Attr: 
        map : la carte 
        label : les labels
        path(list(list(str))) : les chemins retenu.
    Return:
        path(list(list(str))) : les chemins.
    """
    start, end = get_start_end(map,label)
    if len(path)== 0: 
        path=[start]
    x, y = path[-1]
    tx = len(map)
    ty = len(map[0])
    

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


def find_path(map, label, path = [], path2 = []):
    """ trouve toules chemin posible pour un tracé
    Attr: 
        map : la carte 
        label : les labels
        path(list(str)) : le tracé.
        path2(list(list(str))) : les chemins retenu.
    Return:
        path2(list(list(str))) : les chemins.
    """
    start, end = get_start_end(map,label)
    if len(path2)== 0: 
        path2=[start]
    x, y = path2[-1]
    tx = len(map)
    ty = len(map[0])
    

    while not path2[-1] == end:
        points= []
        if x+1 < tx and ((x+1,y) in path or (x+1,y) == start or (x+1,y) == end) and (x+1,y) not in path2:
            points.append((x+1,y))
        if x-1 >= 0 and ((x-1,y) in path or (x-1,y) == start or (x-1,y) == end) and (x-1,y) not in path2:
            points.append((x-1,y))
        if y+1 < ty and ((x,y+1) in path or (x,y+1) == start or (x,y+1) == end) and (x,y+1) not in path2:
            points.append((x,y+1))
        if y-1 >= 0 and ((x,y-1) in path or (x,y-1) == start or (x,y-1) == end) and (x,y-1) not in path2:
            points.append((x,y-1))
        if len(points) > 1:
            path_tmp = path2.copy()
            path2 = []
            for point in points:
                path_tmp = path_tmp.copy()
                res_tmp = find_path(map, label, path, path_tmp + [point])
                for res in res_tmp:
                    path2.append(res)
            return path2
        elif len(points) == 1:
            x, y = points[0]
            path2.append(points[0])
        else:
            break
    if path2[-1] == end:
        return [path2]
    return []


def transform_wall(map,label, path):
    """ transforme un chemin en mur
    Attr: 
        map : la carte 
        label : les labels
        path(list(str)) : le chemin.
    Return:
        wall(list(str)) : liste des murs 
    """
    wall=[]
    path = [elem for e in path for elem in e]
    for x in range(len(map)):
        for y in range(len(map[x])):
            if (x,y) not in path:
                wall.append((x,y))
                
    return wall


def find_intercection(map, label, paths):
    """ trouve les intercections des chemins
    Attr: 
        map : la carte 
        label : les labels
        paths(list(list(str))) : les chemins.
    Return:
        inter(list(str)) : liste des intercection des chemins 
    """
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
            if (tmp >= 3 or ((x,y) == start and tmp >= 2)) and (x,y) not in inter:
                inter.append((x,y))
            
    return inter


def get_score(map, label, lobjet, path, weight, ltuple_rest, val_attract = 7):
    """ calcul le score pour un pour chaque tuple de restriction
    Attr: 
        map : la carte 
        label : les labels
        lobjet(list(str)) : la liste des point d'interêt
        path(list(str)))) : chemins sur lequel on fait les calcul.
        weight (dict(str,int)) : les poid des case sur la carte
        tuple_rest(list(tuple)) : list avec les tuples des restriction (dist, danger, point d'interêt)
        val_attract (int) : valeur a donner au case autour des point d'interêt
    Return:
        scores(list(tuple(int))) : score optenu pour le chemin pour chache tuple de restriction (general, dist, danger, danger_max)
    """
    path_weight = [0 if weight.get(pos) == None else weight.get(pos) for pos in path]
    lsomme_attract = []
    for restriction in ltuple_rest:
        weight_attract = get_weight_attract(map, label, lobjet, 1, restriction[2] * val_attract)
        path_weight_atrract = [0 if weight_attract.get(pos) == None else weight_attract.get(pos) for pos in path]
        lsomme_attract.append(np.sum(path_weight_atrract))


    somme, taille = np.sum(path_weight), len(path)
    return [(taille * ltuple_rest[i][0] + somme * ltuple_rest[i][1] + lsomme_attract[i] * ltuple_rest[i][2], somme, taille, lsomme_attract[i]) for i in range(len(ltuple_rest))]

def path_by_retriction(map, label, ltuple_rest, lobjet=[], lpath = []):
    """
    Attr: 
        map : la carte 
        label : les labels
        tuple_rest(list(tuple)) : list avec les tuples des restriction (dist, danger, point d'interêt)
        lobjet(list(str)) : la liste des point d'interêt
        lpath(list(list(str)))) : la liste des chemins dessiner à l'avance.
    Return:
        paths(list(list(tuple))) : la lists des chemins possible avec comme premier chemin le pcch 
        scores(list(tuple(int))) : score optenu pour chaque chemin (general, dist, danger, danger_max)
    """
    start, end = get_start_end(map, label)
    wall = get_wall(map, label)
    weight = get_weight(map, label)
    val_attract = 7

    path, score = PCCH.a_start(start, end, len(map), len(map[0]), wall)
    path2, score2 = PCCH.a_start(start, end, len(map), len(map[0]), wall, weight)
    paths = [path] * len(ltuple_rest) + [path2] * len(ltuple_rest)

    scores = get_score(map, label, lobjet, path, weight, ltuple_rest)
    scores += get_score(map, label, lobjet, path2, weight, ltuple_rest)

    score_lpath = []
    if len(lpath) == 0:
        score_lpath = None
    else:
        for p in lpath:
            score_lpath += get_score(map, label, lobjet, p, weight, ltuple_rest)

    for restriction in ltuple_rest:
        weight_secu = get_weight(map, label, restriction[1])
        weight_dist = get_weight_dist(map, label, restriction[0])
        weight_attract = get_weight_attract(map, label, lobjet, 1, restriction[2] * val_attract)
        weight_rest = fuse_weight([weight_dist, weight_secu, weight_attract])

        path, score = PCCH.a_start(start, end, len(map), len(map[0]), wall, weight_rest)
        paths.append(path)
        scores += get_score(map, label, lobjet, path, weight, [restriction])
    return paths, scores, score_lpath

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