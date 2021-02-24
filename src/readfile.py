import xml.etree.ElementTree as ET
import pandas as pd
import sys

if sys.version_info[0] < 3: 
    from StringIO import StringIO
else:
    from io import StringIO

def read_map_csv(filename):
    """ Str -> ndarray(int, int)
    Prend un fichier le lis puis renvoie notre carte sous une liste de matrice avec un dictionnaire de chaque id = terrain ou mur"""
    return pd.read_csv(filename, sep=',', header=None).values

def read_map_tmx(filename):
    """ Str -> ndarray(int, int)
    Prend un fichier le lis puis renvoie notre carte sous une liste de matrice avec un dictionnaire de chaque id = terrain ou mur"""
    root = ET.parse(filename).getroot()
    res = pd.read_csv(StringIO(root.find('layer/data').text), sep=',', header=None).values
    return res[:,:-1].astype(int) -1


def read_desc_xml(filename):
    """ Str -> dict
    Prend un fichier le lis puis renvoie notre carte sous une liste de matrice avec un dictionnaire de chaque id = terrain ou mur"""
    dict_res = dict()
    root = ET.parse(filename).getroot()
    lterrain = root.findall('terraintypes/terrain')
    for terrain in lterrain:
        tile = int(terrain.get('tile'))
        tmpdict = dict()
        tmpdict["name"]  = terrain.get('name')
        for property in terrain.findall("properties/property"):
            if property.get('value') == 'true':
                tmpdict[property.get('name')]  = True
            elif property.get('value') == 'false':
                tmpdict[property.get('name')]  = False
            else:
                tmpdict[property.get('name')]  = property.get('value')
        dict_res[tile] = tmpdict  
   
    tiles=root.findall('tile')
    for tile in tiles:
        i=int(tile.get('terrain').split(',')[0])
        tmpdict = dict()
        tmpdict["name"]  = lterrain[i].get('name')
        for property in lterrain[i].findall("properties/property"):
            if property.get('value') == 'true':
                tmpdict[property.get('name')]  = True
            elif property.get('value') == 'false':
                tmpdict[property.get('name')]  = False
            else:
                tmpdict[property.get('name')]  = property.get('value')
            
        dict_res[int(tile.get('id'))]=tmpdict
    return dict_res

