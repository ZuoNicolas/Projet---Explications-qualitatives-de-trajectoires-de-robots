import xml.etree.ElementTree as ET


def read_desc_xml(filename):
    """ Str -> dict
    Prend un fichier le lis puis renvoie notre carte sous une liste de matrice avec un dictionnaire de chaque id = terrain ou mur"""
    dict_res = dict()
    root = ET.parse(filename).getroot()
    lterrain = root.findall('terraintypes/terrain')
    for terrain in lterrain:
        tile = terrain.get('tile')
        tmpdict = dict()
        tmpdict["name"]  = terrain.get('name')
        for property in terrain.findall("properties/property"):
            tmpdict[property.get('name')]  = property.get('value')
        dict_res[tile] = tmpdict  
   
    tiles=root.findall('tile')
    for tile in tiles:
        i=int(tile.get('terrain')[0])
        tmpdict = dict()
        tmpdict["name"]  = lterrain[i].get('name')
        for property in lterrain[i].findall("properties/property"):
            tmpdict[property.get('name')]  = property.get('value')
        dict_res[tile.get('id')]=tmpdict
    return dict_res
print(read_desc_xml("exemple.tsx"))
