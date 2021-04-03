
def Description_to_Txt(list):
    voyelle = ['A', 'E', 'I', 'O', 'U', 'Y']
    msg = ''
    old_orientation = ''
    old_msg = ''
    espace = ' '
    virgule =', '
    point = '.'
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
        
        for description in ite:
            if description == None:
                continue
            
            if type(description) == str:
                obj_name = description
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
                if direction_obj in ['GAUCHE', 'DROITE']:
                    a = 'à '
                    de = 'de'
                msg_tmp += je + action + espace + a + direction_obj + espace + de + espace + 'l\'' + obj +':' + obj_name
    
        if old_msg != msg_tmp  and msg_tmp != '':
            msg += msg_tmp + point +'\n'
        
        old_msg = msg_tmp
            
    return msg

def txt_to_Description(list):
    
    msg = ''
    

    