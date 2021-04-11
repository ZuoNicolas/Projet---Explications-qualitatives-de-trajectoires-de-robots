import numpy as np
import time
import myEnum
import tools
class DescriptionTrajectoire():

    def __init__(self,map,path,label):
            self.map = map
            self.path = path
            self.label = label
            self.description = []
            self.myDescription = myEnum.Description
            self.list_tout_les_chemins = []
            self.list_tout_les_inter = []
            self.list_score_tout_les_chemins = []
            
    def descriptiontTrajectoireSimple(self, agent_rayon=None):
        """ list(list(int)) * list(int) * dict{int:dict{str:str}}
        Parcours le chemin path en regardant les objets au alentours,
        pour retourner la description contruite"""

        if len(self.path) == 0:
            print("Erreur path vide dans descriptiontrajectoireSimple")
            return -1
        #créer une liste qui décris chaque case du path où les objets sont a porter d'intéraction de la case en question
        map_local = self.local_map(agent_rayon)
        #print(map_local)
        
        old = None #Sauvegarde de l'ancienne orientation
        n_case = -1 #Compteur du nombre de case parcourus avant un événement
        old_res='' #Sauverade du dernier objet de passage pour évité le spam
        anti_spam=0 #Compteur du nombre d'itération du même événement de passage
        nb_de_case_anti_spam=2 #Nombre de case avant de pouvoir redécrire le même événement de passage
        
        #Parcours le chemin et contruit la description
        for i in range(len(self.path)):
            
            # n_case+=1 #incrémentation
            
            #Pour évité l'erreur de Out Of Bound, car on regarde notre case actuel et la case suivante,
            #pour savoir l'évolution du sens d'orientation actuel.
            if i == len(self.path)-1 :
                break
            

            description_temp = []
            orientation = self.direction(self.path[i],self.path[i+1]) #Calcul de l'orientation de notre agent en regardant sa case actuel et la case suivante
            
            description_temp.append(orientation)
            
            #Pour la première itération
            if old == None:
                old=orientation
                
            description_temp = description_temp + [self.myDescription.AVANCE, self.myDescription.JUSQU_A]
            sauvegarde = description_temp.copy()
    
            #Si l'orientation du case suivante est différente, alors on rajoute l'événement tourner
            if  old != orientation:
                description_temp.append(self.myDescription.INTERSECTION)
                description_temp += [self.myDescription.TOURNE, self.message_orientation(old, orientation) ]#Ajout du bon message en fonction des orientations
                
            #Si il y a un événement sur la case
            if map_local[i] != [] :
                
                #Calcul du message de passage à coté de ...
                for ind in range(len(map_local[i])):
                    res = [self.calcul_position_objet(orientation, map_local[i][ind][1],map_local[i][ind][2]), map_local[i][ind][0]]
                    
                    #Pour évité le spam quand on passe a coté d'un objet qui a un rayon d'interraction sur plusieur case
                    if res != old_res:
                        description_temp.append(self.myDescription.PASSE)
                        description_temp += res
                        description_temp.append(self.myDescription.OBJECT)
                        
                        #Mise à jour des variables
                        old_res = res
                        anti_spam=0
                        
            old = orientation
            
            if description_temp == sauvegarde: #Si il n'y a aucun changement on incrémente l'anti-spam
                description_temp = description_temp[:-1]
                anti_spam+=1
                if anti_spam > nb_de_case_anti_spam:
                    old_res=''
            
            self.description.append(description_temp)
        
        #Ajout du dernier événement
        description_temp = []
        description_temp.append(orientation)
        description_temp += self.avancer_jusqu_a() + [self.myDescription.ARRIVER]
        
        self.description.append(description_temp)
        
        return self.description
    
    def descriptiontTrajectoirePlusExplication(self, agent_rayon=None, ltuple_rest=[(0.1,0.9)]):
        """ list(list(int)) * list(int) * dict{int:dict{str:str}}
        Parcours le chemin path en regardant les objets au alentours,
        pour retourner la description contruite"""

        # fonction.getScore
        paths, score = tools.path_by_retriction(self.map, self.label,  ltuple_rest)
        argmin = np.argmin(np.array(score)[:,0])
        self.path = paths[argmin] #Le meilleu path
        _, path_securiter, path_rapide, path_secu_max = score[argmin] 
        self.list_tout_les_inter = tools.find_intercection(self.map, self.label, paths)
        print("meilleur path\n", self.path)
        print("les chemins\n",paths)
        print("==\n",paths[0]==paths[1])
        print("score\n",score)     
        print("Intersection\n",self.list_tout_les_inter)
        print(argmin)
        del paths[argmin]
        del score[argmin]
        self.list_tout_les_chemins = paths
        
        self.list_score_tout_les_chemins = score
        
        
        if len(self.path) == 0:
            print("Erreur path vide dans descriptiontrajectoireSimple")
            return -1
        #créer une liste qui décris chaque case du path où les objets sont a porter d'intéraction de la case en question
        map_local = self.local_map(agent_rayon)
        #print(map_local)

        old = None #Sauvegarde de l'ancienne orientation
        n_case = -1 #Compteur du nombre de case parcourus avant un événement
        old_res='' #Sauverade du dernier objet de passage pour évité le spam
        anti_spam=0 #Compteur du nombre d'itération du même événement de passage
        nb_de_case_anti_spam=2 #Nombre de case avant de pouvoir redécrire le même événement de passage
        
        #Parcours le chemin et contruit la description
        for i in range(len(self.path)):
            
            # n_case+=1 #incrémentation
            
            #Pour évité l'erreur de Out Of Bound, car on regarde notre case actuel et la case suivante,
            #pour savoir l'évolution du sens d'orientation actuel.
            if i == len(self.path)-1 :
                break
            
            orienter = False
            description_temp = []
            orientation = self.direction(self.path[i],self.path[i+1]) #Calcul de l'orientation de notre agent en regardant sa case actuel et la case suivante
            
            description_temp.append(orientation)
            
            #Pour la première itération
            if old == None:
                old=orientation
                
            description_temp += [self.myDescription.AVANCE]
            sauvegarde = description_temp.copy()
    
            #Si l'orientation du case suivante est différente, alors on rajoute l'événement tourner
            if  old != orientation:
                description_temp += [self.myDescription.TOURNE, self.message_orientation(old, orientation) ]#Ajout du bon message en fonction des orientations
                orienter = True
            if self.path[i] in self.list_tout_les_inter:
                if orienter:
                    description_temp += [self.myDescription.AVANCE]
                description_temp += [self.myDescription.JUSQU_A,self.myDescription.INTERSECTION]
                description_temp += self.explication_intersection(self.path[i], i+1, self.path, path_rapide, path_securiter)
            #Si il y a un événement sur la case
            if map_local[i] != [] :
                
                #Calcul du message de passage à coté de ...
                for ind in range(len(map_local[i])):
                    res = [self.calcul_position_objet(orientation, map_local[i][ind][1],map_local[i][ind][2]), map_local[i][ind][0]]
                    
                    #Pour évité le spam quand on passe a coté d'un objet qui a un rayon d'interraction sur plusieur case
                    if res != old_res:
                        description_temp.append(self.myDescription.PASSE)
                        description_temp += res
                        description_temp.append(self.myDescription.OBJECT)
                        
                        #Mise à jour des variables
                        old_res = res
                        anti_spam=0
                        
            old = orientation
            
            if description_temp == sauvegarde: #Si il n'y a aucun changement on incrémente l'anti-spam
                anti_spam+=1
                if anti_spam > nb_de_case_anti_spam:
                    old_res=''
            
            self.description.append(description_temp)
        
        #Ajout du dernier événement
        description_temp = []
        description_temp.append(orientation)
        description_temp += [self.myDescription.AVANCE, self.myDescription.JUSQU_A, self.myDescription.ARRIVER]
        
        self.description.append(description_temp)

        return self.description
            
    def local_map(self, agent_rayon=None):
        """Retourne une liste de liste ou chaque indice correspond au case,*
        Chaque sous liste contient toute les événements entre les objets"""
        
        path_area = [ [] for x in range(len(self.path)) ]
        
        #Parcours de toute la map et on regarde le rayon d'action de chaque objet
        #Si l'objet est à porter d'une de nos case du path alors on le rajoute dans notre liste
        for x in range(len(self.map)):
            for y in range(len(self.map[0])):
                rayon_action = self.label.get(self.map[x][y]).get('vision_area') #Récupération du rayon d'action  
                
                if  rayon_action != None and int(rayon_action) > 0 : #Vérification de la présence d'un rayon
                    if  agent_rayon != None : #Vérification de la présence d'un rayon
                        #Parcours du path pour savoir si une de nos case est dans le rayon d'action de l'objet en question ou non
                        for i in range(len(self.path)): 
                            a,b = self.path[i]
                            rayon = (a - x)**2 + (b - y)**2 #Formule de rayon au carré
                            if rayon <= int(agent_rayon)**2 :
                                path_area[i].append(((self.map[x][y],self.label.get(self.map[x][y]).get('name')), (a,b), (x,y)))
                                
                    else :
                        #Parcours du path pour savoir si une de nos case est dans le rayon d'action de l'objet en question ou non
                        for i in range(len(self.path)): 
                            a,b = self.path[i]
                            rayon = (a - x)**2 + (b - y)**2 #Formule de rayon au carré
                            if rayon <= int(rayon_action)**2 :
                                path_area[i].append(((self.map[x][y], self.label.get(self.map[x][y]).get('name')), (a,b), (x,y)))
        
    
        return path_area
    
    def direction(self, case_present, case_suivante):
        """Calcul le sens de la direction et renvoie 0,1,2 ou 3, 
        mais ne marche, ici que pour deux case cote à cote"""
        vect_x = case_suivante[0] - case_present[0]
        vect_y = case_suivante[1] - case_present[1]
        
        if vect_x > 0 :
            return self.myDescription.SUD
        elif vect_x < 0 :
            return self.myDescription.NORD
        elif vect_x == 0:
            if vect_y > 0:
                return self.myDescription.EST
            elif vect_y < 0:
                return self.myDescription.OUEST
            
    def calcul_position_objet(self, d , point,point_objet):
        """         0 : Nord
        3 : Ouest               1 : Est
                    2 : Sud
        Prend la direction d : {0,1,2,3}
        et renvoie une phrase pour dire si depuis sont point actuel, 
        le point de l'objet est plutôt a droite, a gauche, devant ou derrire 
        (fonctionne meme sur deux points non cote a cote)
        """
        x, y = point
        xo, yo = point_objet
        
        if d == self.myDescription.NORD:
            if y < yo :
                return self.myDescription.GAUCHE
            elif y > yo  :
                return self.myDescription.DROITE
            elif x > xo :
                return self.myDescription.DEVANT
            else :
                return self.myDescription.DERRIERE
        if d == self.myDescription.EST:
            if x < xo :
                return self.myDescription.GAUCHE
            elif x > xo :
                return self.myDescription.DROITE
            elif y < yo :
                return self.myDescription.DEVANT
            else :
                return self.myDescription.DERRIERE
            
        if d == self.myDescription.SUD:
            if y > yo :
                return self.myDescription.GAUCHE
            elif y < yo :
                return self.myDescription.DROITE
            elif x < xo :
                return self.myDescription.DEVANT
            else :
                return self.myDescription.DERRIERE
        if d == self.myDescription.OUEST:
            if x > xo :
                return self.myDescription.GAUCHE
            elif x < xo :
                return self.myDescription.DROITE
            elif y > yo:
                return self.myDescription.DEVANT
            else :
                return self.myDescription.DERRIERE
        
    def message_orientation(self, old, now):
        """         0 : Nord
        3 : Ouest               1 : Est
                    2 : Sud
        Prend deux direction : {0,1,2,3}  et renvoie un String pour dire dans quel sens on a tourné depuis la dernière orientation
        """
        if old == self.myDescription.NORD:
            
            if now == self.myDescription.EST:
                return self.myDescription.A_DROITE
            
            if now == self.myDescription.SUD:
                return self.myDescription._DERRIERE
            
            if now == self.myDescription.OUEST:
                return self.myDescription.A_GAUCHE
            
        if old == self.myDescription.EST:
            
            if now == self.myDescription.SUD:
                return self.myDescription.A_DROITE
            
            if now == self.myDescription.OUEST:
                return self.myDescription._DERRIERE
            
            if now == self.myDescription.NORD:
                return self.myDescription.A_GAUCHE
            
        if old == self.myDescription.SUD:
            
            if now == self.myDescription.OUEST:
                return self.myDescription.A_DROITE
            
            if now == self.myDescription.NORD:
                return self.myDescription._DERRIERE
            
            if now == self.myDescription.EST:
                return self.myDescription.A_GAUCHE
            
        if old == self.myDescription.OUEST:
            
            if now == self.myDescription.NORD:
                return self.myDescription.A_DROITE
            
            if now == self.myDescription.EST:
                return self.myDescription._DERRIERE
            
            if now == self.myDescription.SUD:
                return self.myDescription.A_GAUCHE
    
    
    def explication_intersection(self, case_actuelle, id_case_suivante, path_choisi, path_rapide, path_securiter):
        
        x, y = case_actuelle; #(ligne, colonne)
        
        msg = []
        i = 0
        for chemin in self.list_tout_les_chemins :
            #Pour enlever les chemin qui vont dans la meme direction
            if id_case_suivante < len(chemin)  and chemin[id_case_suivante] != path_choisi[id_case_suivante]:
                if (x+1, y) == chemin[id_case_suivante] or (x-1, y) == chemin[id_case_suivante] or \
                    (x, y+1) == chemin[id_case_suivante] or (x, y-1) == chemin[id_case_suivante] :
                    #case_actuelle = une intersection
                    if case_actuelle in chemin:
                        _, securiter, rapide, _ = self.list_score_tout_les_chemins[i]
                        
                        msg.append(('CHEMIN', i))
                        tmp_msg = []
                        
                        ratio_rapide = rapide/path_rapide
                        ratio_securiter = securiter/path_securiter
                        
                        if path_rapide == 0 :
                            ratio_rapide = rapide-path_rapide
                            if rapide == 0 :
                                ratio_rapide = 1
                        
                        if path_securiter == 0 :
                            ratio_securiter = securiter-path_securiter
                            if securiter == 0 :
                                ratio_securiter = 1
                                
                        
                        
                        if ratio_rapide >= 1.7:
                            tmp_msg.append(self.myDescription.BEAUCOUP_MOINS_RAPIDE)
                            
                        elif ratio_rapide > 1 :
                            tmp_msg.append(self.myDescription.MOINS_RAPIDE)
                            
                        elif ratio_rapide == 1 :
                            tmp_msg.append(self.myDescription.RAPIDE)
                            
                        elif ratio_rapide >= 0.5 :
                            tmp_msg.append(self.myDescription.PLUS_RAPIDE)
                            
                        else:
                            tmp_msg.append(self.myDescription.BEAUCOUP_PLUS_RAPIDE)
                            
                            
                        if ratio_securiter >= 1.7 :
                            tmp_msg.append(self.myDescription.BEAUCOUP_MOINS_SECURITE)
                            
                        elif ratio_securiter > 1 :
                            tmp_msg.append(self.myDescription.MOINS_SECURITE)
                            
                        elif ratio_securiter == 1 :
                            tmp_msg.append(self.myDescription.SECURITE)
                            
                        elif ratio_securiter > 0.5 :
                            tmp_msg.append(self.myDescription.PLUS_SECURITE)
                            
                        else:
                            tmp_msg.append(self.myDescription.BEAUCOUP_PLUS_SECURITE)
                        
                        msg.append(tmp_msg)
                        print(path_securiter, '-', securiter,'=',securiter-path_securiter,'\n',path_rapide, '-', rapide,'=',rapide-path_rapide)
            i+=1
        
        return msg
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        

