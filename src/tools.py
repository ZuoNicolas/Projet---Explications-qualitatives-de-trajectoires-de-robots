

def fuse_weidgh(list_dico_weidgh):
    l=list_dico_weidgh[0].copy()
    
    #fusionner avec tout les keys
    for lis in list_dico_weidgh:
        l.update(lis)
    #additionner les valeurs
    for cle in l.keys():
        l[cle]=0
        for lis in list_dico_weidgh:
            if(lis.has_key(cle)):
                l[cle]+=lis[cle]
    return l