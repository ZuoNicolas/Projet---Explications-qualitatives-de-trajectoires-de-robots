import numpy as np

class Etat:
        visite = dict()
        frontiere = []
        x_max = 20
        y_max = 20
        wallStates = []

        def __init__(self,position, g, parent, goal, pos_depart):
            self.parent = parent
            self.pos = position    # la position de la case actuelle
            self.g = g             # pas de l'avancement 
            self.goal = goal
            self.pos_depart = pos_depart

        def setwall(wall):
            Etat.wallStates = wall

        def setx_max(x):
            Etat.x_max = x

        def sety_max(y):
            Etat.y_max = y

        def reset():
            Etat.visite = dict()
            Etat.frontiere = []

        def H(self):               #Distance de Manhattan
            x,y= self.pos
            xG,yG = self.goal
            return abs(xG-x)+abs(y-yG)

        def getPosition(self):
            return self.pos

        def cost(self):
            return self.g+self.H()

        def ajout(self,etat):
            for i in range(len(Etat.frontiere)):
                if Etat.frontiere[i].cost() > etat.cost():
                    Etat.frontiere.insert(i,etat)
                    return
            Etat.frontiere.insert(len(Etat.frontiere),etat)


        def chemin(self,p,chemin):
            chemin.insert(0, p)
            if p == self.pos_depart:
                return chemin
            return self.chemin(Etat.visite[p].pos, chemin)

        def evaluer(self):
            Etat.visite[self.pos]=self.parent
            """if self.pos in goalStates:
                return self.chemin(self.pos, [])"""
            if self.pos == self.goal:
                return self.chemin(self.pos, [])
            x,y = self.pos
            nord = (x,y+1)
            sud = (x,y-1)
            est = (x+1,y)
            ouest = (x-1,y)
            sens = [nord,sud,est,ouest]
            for (a,b) in sens :
                if a>=0 and a<Etat.x_max and b>=0 and b<Etat.y_max and (a,b) not in list(Etat.visite.keys()) and (a,b) not in Etat.wallStates :
                    self.ajout(Etat((a,b),self.g+1,self, self.goal, self.pos_depart))
            while "Etat.frontiere[0] n'est pas dans visite" :
                if len(Etat.frontiere)==0:
                    return []
                e = Etat.frontiere.pop(0)
                if e.pos not in Etat.visite :
                    return e.evaluer()
            return []


def a_start(debut, goal, y_max, x_max, wall):
    Etat.reset()
    Etat.setwall(wall)
    Etat.setx_max(x_max)
    Etat.sety_max(y_max)
    return Etat(debut,0,None, goal, debut).evaluer()

def affichage_console(map,path):
    
    for x in range(len(map)):
        for y in range(len(map[x])):
            if map[x][y] == 1:
                print('|',end='')
            else:
                b=True
                for i,j in path:
                    if i==x and j==y:
                        print('*',end='')
                        b=False
                if b:
                    print(' ',end='')
                
        print()

