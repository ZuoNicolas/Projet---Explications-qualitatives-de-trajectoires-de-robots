import myEnum
import re
import numpy as np
def Description_to_Txt2(list_desc, label):
    """
    Fait la traduction de la liste des Descriptions en Texte
    """

    list_msg = []

    for descriptions in list_desc:
        msg = ''
        list_obj = []
        for description in descriptions:
            msg_tmp = ''
            
            if description == None:
                continue
            
            if type(description) == tuple: #Quand c'est un objet description = tuple(ID,name)
                obj_id, obj_name = description
                continue
            
            if description in [myEnum.Description.NORD, myEnum.Description.SUD, myEnum.Description.EST, myEnum.Description.OUEST]:
                continue
                
            if type(description) == list: #Quand il y a une explication d'un choix de chemin
                msg_tmp += str(myEnum.Description.EXPLICATION.value)+' '
                secu_bonne = ''
                secu_mauvaise = ''
                rapi_bonne = ''
                rapi_mauvaise = ''
                for desc in description:
                    value = desc.value
                    if desc in [myEnum.Description.BEAUCOUP_MOINS_SECURITE, myEnum.Description.MOINS_SECURITE]:
                        secu_mauvaise = value
                    elif desc in [myEnum.Description.PLUS_SECURITE, myEnum.Description.BEAUCOUP_PLUS_SECURITE,myEnum.Description.SECURITE]:
                        secu_bonne = value
                    elif desc in  [myEnum.Description.BEAUCOUP_MOINS_RAPIDE, myEnum.Description.MOINS_RAPIDE]:
                        rapi_mauvaise = value
                    elif desc in [myEnum.Description.PLUS_RAPIDE, myEnum.Description.BEAUCOUP_PLUS_RAPIDE, myEnum.Description.RAPIDE]:
                        rapi_bonne = value
                    else:  
                        msg_tmp += ' '+str(value)
                
                if secu_bonne != '':
                    if rapi_mauvaise != '':
                        msg_tmp += secu_bonne+', mais '+rapi_mauvaise
                    else:
                        msg_tmp += 'bug1'
                elif secu_mauvaise != '':
                    if rapi_bonne != '':
                        msg_tmp += rapi_bonne+' en terme de distance, mais en terme de sécurité on est '+secu_mauvaise
                    else:
                        msg_tmp +='bug2'  
            else:
                
                value = description.value  
                
                if description == myEnum.Description.OBJECT: 
                    value = obj_name
                    if obj_name not in list_obj:
                        list_obj.append((obj_id, obj_name))
                    obj_name = ''
                
                msg_tmp += str(value)
                
            msg += msg_tmp+' '

        for id, valeur in list_obj:

            if myEnum.Description.GAUCHE.value+' '+valeur in msg:
                msg = re.sub(' '+myEnum.Description.PASSE.value+' '+myEnum.Description.GAUCHE.value+' '+valeur,'', msg)
                if myEnum.Description.DROITE.value+' '+valeur in msg:
                    msg = re.sub(' '+myEnum.Description.PASSE.value+' '+myEnum.Description.DROITE.value+' '+valeur,'', msg)
                    msg += ' '+myEnum.Description.PASSE.value+' '+myEnum.Description.ENTRE.value+' les '+valeur+'(s)'
                else:
                    msg += ' '+myEnum.Description.PASSE.value+' '+myEnum.Description.GAUCHE.value+' '+de(id, valeur, label)+valeur
                    
            elif myEnum.Description.DROITE.value+' '+valeur in msg:
                msg = re.sub(' '+myEnum.Description.PASSE.value+' '+myEnum.Description.DROITE.value+' '+valeur,'', msg)
                
                if myEnum.Description.GAUCHE.value+' '+valeur in msg:
                    msg = re.sub(' '+myEnum.Description.PASSE.value+' '+myEnum.Description.GAUCHE.value+' '+valeur,'', msg)
                    msg += ' '+myEnum.Description.PASSE.value+' '+myEnum.Description.ENTRE.value+' les '+valeur+'(s)'
                else:
                    msg += ' '+myEnum.Description.PASSE.value+' '+myEnum.Description.DROITE.value+' '+de(id, valeur, label)+valeur
    
        list_msg.append(msg)

    return list_msg

def Description_to_Txt(list, label):
    """
    Fait la traduction de la liste des Descriptions en Texte
    """
    voyelle = ['A', 'E', 'I', 'O', 'U', 'Y','a', 'e', 'i', 'o', 'u', 'y']
    msg = ''
    old_orientation = ''
    old_msg = ''
    espace = ' '
    virgule =', '
    point = '.'
    description = []
    
    for ite in list:
        orientation = ''
        list_action = []
        precition_avancer = ''
        descrip_avancer = ''
        precision_distance = ''
        distance = ''
        direction_obj = ''
        direction_sens = ''
        obj = ''
        old_action = ''
        obj_id = None
        
        for description in ite:
            if description == None:
                continue
            
            if type(description) == tuple: #Quand c'est un objet description = tuple(ID,name)
                obj_id, obj_name = description
                continue

                
            value = description.value
            name = description.name

            if value <= -1 and value >= -4:
                orientation = name
                
            elif value >= -7:
                list_action.append(name)
            
            elif value >= -9:
                precition_avancer = name
                
            elif value >= -11:
                descrip_avancer = name
                
            elif value >= -13:
                precision_distance = name
            
            elif value >= -16:
                distance = name
                
            elif value >= -26:
                direction_obj = name
                
            elif value >= -32:
                direction_sens = name

            elif value >= -60:
                obj = name
            

        msg_tmp = ''
        for action in list_action:
            
            if msg_tmp != '' :
                msg_tmp += virgule
                
            je = 'Je '
            if action[0] in voyelle:
                je = 'J\''
                
            if action == 'AVANCE' and descrip_avancer != '':
                msg_tmp += je + action + espace + precition_avancer + ' l\'' + descrip_avancer
            
            elif action == 'TOURNE' : 
                msg_tmp += je + action + espace + direction_sens
                
            elif action == 'PASSE' : 
                a = ''
                de = ''
                le = ''
                if direction_obj in ['GAUCHE', 'DROITE']:
                    a = 'à '
                    if obj_name[0] in voyelle:
                        de = 'de' + espace
                        le = 'l\''
                    elif label.get(obj_id).get('genre') == 'M':
                        de = 'du' + espace
                    else:
                        de = 'de' + espace
                        le = 'la' + espace
                else : #Derriere
                    if obj_name[0] in voyelle:
                        le = 'l\''
                    elif label.get(obj_id).get('genre') == 'M':
                        le = 'le' + espace
                    else:
                        le = 'la' + espace

                if obj_name in msg_tmp:
                    msg_tmp = re.sub(de + le + obj_name, 'des' + espace + obj_name + 's', msg_tmp) #modifie pour avoir en pluriel
                    msg_tmp = msg_tmp[:-2] #pour enlever les virgules de fin, comme on rajoute pas de contenu mais qu'on a modifié
                else : 
                    msg_construit = je + action + espace + a + direction_obj + espace + de + le + obj_name
                    msg_tmp += msg_construit
    
        if old_msg != msg_tmp  and msg_tmp != '':
            msg += msg_tmp + point +'\n'
        
        old_msg = msg_tmp
            
    return msg

def txt_to_Description(text, case_départ, orientation_départ, map):
    """
    L'utilisateur donne des descriptions sur la carte, sur des mots prédefinie, exemple :
        J'avance jusqu'au fleur, ou j'avance très près des fleurs, et s'il y a plusieur fleur sur la carte,
        soit on laisse l'utilisateur choisir lequelles soit on choisis les fleurs les plus proche du robot
        
    On pourra faire cette traduction en faisant plusieur A* du point actuelle jusqu'au point demandé avec de certaine option,
    par exemple si dans la phrase l'utilisateur dit, 'par un chemin sécurisé', alors on mettra une option dans notre A*, pour qu'il
    trouve un chemin sûr d'un point A à un point B, et quand on a construit notre path, il nous reste plus qu'a le faire passer 
    dans notre descriptionTrajectoire2
    """
    # Version Incomplète a refaire en ->
    # description = []
    # list_description = list(myEnum.Description.name)
    # list_description_name = [ desc.name for desc in list_description]
    
    # text = re.sub("'", " ", text)
    # text = re.sub(",", " ", text)
    # text = re.sub(".", " ", text)
    
    # orientation = orientation_départ
    
    # for txt in text.split('\n'):
    #     tmp = []
    #     text_list = txt.split()
        
    #     tmp.append(myEnum.orientation)
    #     for elem in text_list:
            
    #         if elem in list_description_name:
    #             tmp.append(myEnum.elem)
    
    
def Description_to_path(description,case_present):
    path=[case_present]
    for d in description:
    #direction
        case_suivante=get_next_pos(case_present,d[0])
        path.append(case_suivante)
        case_present=case_suivante
    return path[:-1]

def get_next_pos(case_present,d):
    if(d.value==myEnum.Description.SUD.value):#sud
        return (case_present[0]+1,case_present[1])
    if(d.value==myEnum.Description.NORD.value):#nord
        return (case_present[0]-1,case_present[1])
    if(d.value==myEnum.Description.EST.value):#est
        return (case_present[0],case_present[1]+1)
    if(d.value==myEnum.Description.OUEST.value):#ouest
        return (case_present[0],case_present[1]-1)
    
def de(obj_id, obj_name, label):
    voyelle = ['A', 'E', 'I', 'O', 'U', 'Y','a', 'e', 'i', 'o', 'u', 'y']
    de = ''
    le = ''
    if obj_name[0] in voyelle:
        de = 'de l\''
    elif label.get(obj_id).get('genre') == 'M':
        de = 'du '
    else:
        de = 'de la '

    return de


    