import pygame
import pytmx
import xml.etree.ElementTree as ET
import time
import descriptionTrajectoire as DT
import readfile
import Traduction
import slider 
from tools import *
from myEnum import *
black = (0,0,0)
white = (255,255,255)
red = (200,0,0)
green = (0,200,0)
bright_red = (255,0,0)
bright_green = (0,255,0)
block_color = (53,115,255)

YELLOW = (255, 255, 0)
GREEN = (0, 255, 50)
BLUE = (50, 50, 255)
GREY = (200, 200, 200)
ORANGE = (250, 125, 64)
CYAN = (0, 255, 255)
MAGENTA = (255, 0, 255)
RED = (255,0,0)
TRANS = (1, 1, 1)

LIST_COLOR = [MAGENTA, RED, YELLOW, white]

ALPHA = 70

DICO_ACCURACY = {
    'description simple' : 0,
    'comparaison simple' : 1,
    'comparaison détaillée' : 2
}

class Game(object):

    def __init__(self, filename, map, label, radius=5):
        self._running = True
        self._display_surf = None
        self.filename = filename
        self.label=label
        self.path = []
        self.iteration = 0
        self.forward = True
        self.radius = radius
        self.drawingpath = []

        self.restriction=[]
        self.choose_image=False
        self.choose_parametre=False

    def on_init(self):
        pygame.init()

        self.loadimage()
        list_image=["Monde1","Monde2",'Monde3']
        font=pygame.font.SysFont("Verdana", 12)
        self.images=slider.OptionBox(self.width-(self.tool_width),0,150,30,(150, 150, 150), (100, 200, 255),font,list_image,0,False)
        
        self.choix_image()

    def choix_image(self):
        """ permet de dessiner tous les boutons
        Attr: 
        Return:
            None
        """
        while not self.choose_image:
            event_list = pygame.event.get()
            for event in event_list:
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

                elif event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    for s in self.slides:
                        if s.button_rect.collidepoint(pos):
                            s.hit = True
                elif event.type == pygame.MOUSEBUTTONUP:
                    for s in self.slides:
                        s.hit = False
            # Move slides
            for s in self.slides:
                if s.hit:
                    s.move()
            self.option.update(event_list)
            self.option.draw(self._display_surf)
            self.images.set_rect(self.width-(self.tool_width),0,150,30)
            self.images.update(event_list)
            self.images.draw(self._display_surf)
            self.accuracy.update(event_list)
            self.accuracy.draw(self._display_surf)

            for s in self.slides:
                s.draw(self._display_surf)

            self.button('reset', self.width-(self.tool_width*2/3),0, 90, 40, green,bright_green, self.reset)
            self.button('confirm',self.width-(self.tool_width/4)+10,0,90,40,green,bright_green,self.one_step)
            self.button('Draw Path', self.width-(self.tool_width*1/2)+20,0, 90, 40, green,bright_green, self.func_drawpath)

            if(self.option.draw_menu):
                self.option.draw(self._display_surf)
            if(self.images.draw_menu):
                self.images.draw(self._display_surf)
            if(self.accuracy.draw_menu):
                self.accuracy.draw(self._display_surf)
            if(self.filename!='../ressource/'+self.images.option_list[self.images.selected]+'.tmx'):
                self.func_choix_image()

            pygame.display.update()
    def reset(self):
        self.iteration=0
        self.loadimage()
        self.choix_image()
    def func_choix_image(self):
        """ permet de charger la map selectionné
        Attr: 
        Return:
            None
        """
        self.filename='../ressource/'+self.images.option_list[self.images.selected]+'.tmx'
        self.loadimage()
        pygame.display.update()

    def loadimage(self):
        """ permet de charger toute les images necessaire pour le logiciel
        Attr: 
        Return:
            None
        """

        root = ET.parse(self.filename).getroot()
        self.map=readfile.read_map_tmx(self.filename)
        self.dt=DT.DescriptionTrajectoire(self.map,self.path,self.label)
        self.tool_width=30*16 #toolbar a droite de fenetre
        self.discription_height=15*16 #discription en bas de fenetre
        self.size = self.width, self.height = (int(root.get("width"))) * 16+self.tool_width, (int(root.get("height"))) * 16+self.discription_height #a changer
        
        #zone d'affichage
        self._display_surf = pygame.display.set_mode(self.size, pygame.HWSURFACE | pygame.DOUBLEBUF)
        self._display_surf.fill(white)
        self.drawingpath = []




        self._running = True
        pygame.display.set_caption('robot')#ecrire le titre de window
        
        tm = pytmx.load_pygame(self.filename, pixelalpha=True)
        self.layer = tm.get_layer_by_name(root.find('layer').get("name"))
        #image de robot
        self.robot = pygame.image.load("../ressource/robot16.png").convert()
        self.robot_dir = {Description.EST : pygame.image.load("../ressource/robot16Est.png").convert(),
                          Description.NORD : pygame.image.load("../ressource/robot16Nord.png").convert(),
                          Description.OUEST : pygame.image.load("../ressource/robot16West.png").convert(),
                          Description.SUD : pygame.image.load("../ressource/robot16Sud.png").convert()}
        

        self.image_dict = dict()
        self.construction()
        list_obj=self.list_objets()
        font=pygame.font.SysFont("Verdana", 12)
        self.option=slider.OptionBox(self.width-(self.tool_width*2/3),60,90,30,(150, 150, 150), (100, 200, 255),font,list_obj)
        self.accuracy = slider.OptionBox(self.width-(self.tool_width/3)-30,60,170,30,(150, 150, 150), (100, 200, 255),font,list(DICO_ACCURACY.keys()), 1, False)
        self.preference=slider.Slider("point d'interêt",0,150,10,self.width-self.tool_width+10,40)
        self.secu = slider.Slider("sécurité", 0, 150, 10, self.width-self.tool_width+10,100)
        self.rapid=slider.Slider("rapidité",0,150,10,self.width-self.tool_width+10,160)
        
        self.slides=[self.secu,self.rapid,self.preference]


    def drawpath(self):
        """ place le bouton lier au dessin de chemins
        Attr: 
        Return:
            None
        """
        x = self.width-(self.tool_width/2)
        y = 0
        self.button('my path', x, y, 90, 40, green,bright_green, self.func_drawpath)
        

    def func_drawpath(self):
        """ permet de dessiner le chemin a la min sur la carte tant qu'un chemin n'est pas valide
        Attr: 
        Return:
            None
        """
        path = []
        self.drawingpath = []
        push = False
        while self.drawingpath == []:

            event_list = pygame.event.get()
            for event in event_list:
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    push = True
                    pos = pygame.mouse.get_pos()
                    if pos[0] < self.width - self.tool_width and pos[1] < self.height - self.discription_height:
                        x,y = pos
                        x = x//16
                        y = y//16

                        if self.label.get(self.map[y][x]).get('canPass'):
                            if (y,x) not in path:
                                path.append((y,x))
                            else:
                                path.remove((y,x))
                        self.construction()
                        for y, x in path:
                            s = pygame.Surface((16,16))  # the size of your rect
                            s.fill(BLUE)           # this fills the entire surface
                            self._display_surf.blit(s,(x*16,y*16))
                        #pygame.display.update()
                elif event.type == pygame.MOUSEBUTTONUP:
                    push = False
                elif event.type == pygame.MOUSEMOTION and push:
                    pos = pygame.mouse.get_pos()
                    if pos[0] < self.width - self.tool_width and pos[1] < self.height - self.discription_height:
                        x,y = pos
                        x = x//16
                        y = y//16

                        if self.label.get(self.map[y][x]).get('canPass'):
                            if (y,x) not in path:
                                path.append((y,x))
                        self.construction()
                        for y, x in path:
                            s = pygame.Surface((16,16))  # the size of your rect
                            s.fill(BLUE)           # this fills the entire surface
                            self._display_surf.blit(s,(x*16,y*16))
                        #pygame.display.update()
                self.drawingpath = find_path(self.map, self.label, path)
            self.button('reset', self.width-(self.tool_width*2/3),0, 90, 40, green,bright_green, self.reset)
            pygame.display.update()
    def list_objets(self):
        """ renvoi la liste des objets de la map selectionné
        Attr: 
        Return:
            list_obj(list[str]) : liste des objets present sur la carte
        """
        list_obj=[]
        for x in range(len(self.map)):
            for y in range(len(self.map[0])):
                objet = self.label.get(self.map[x][y]).get('name') 
                if(objet not in list_obj):
                    list_obj.append(objet)
        list_obj.remove('terre')
        list_obj.remove('start')
        list_obj.remove('end')
        return list_obj


    def construction(self):
        """ dessine les element pour pour l'intant présent
        Attr: 
        Return:
            None
        """
        #afficher map
        start,end=get_start_end(self.map,self.label)
        self._display_surf.fill(white)
        for x, y, image in self.layer.tiles():
            self._display_surf.blit(image,(x*16,y*16))
        y, x = start
        #afficher path qu'utilisateur a dessiné
        for path in self.drawingpath:
            for y_tmp, x_tmp in path:
                s = pygame.Surface((16,16))  # the size of your rect
                s.set_alpha(ALPHA)           # alpha level
                s.fill(green)                # this fills the entire surface
                self._display_surf.blit(s,(x_tmp*16,y_tmp*16))
        self.draw_circle_alpha( self._display_surf, (255,0,0), ((x+0.5)*16,(y+0.5)*16), self.radius*16)
        
        self._display_surf.blit(self.robot_dir[Description.SUD],(x*16,y*16))
        discp_surf=pygame.Surface((self.width-self.tool_width,self.discription_height))
        discp_surf.fill(GREY)
        self._display_surf.blit(discp_surf,((0,self.height-self.discription_height)))
        
        #afficher guide d'utilisation
        smallText = pygame.font.SysFont("comicsansms",12)
        textSurf2, textRect2 = self.text_objects("Guide d'utilisation : ", smallText)
        textRect2.left,textRect2.top=(self.width-self.tool_width+5,230)
        self._display_surf.blit(textSurf2, textRect2)
        
        textSurf2, textRect2 = self.text_objects("1. Sélectionner les poids", smallText)
        textRect2.left,textRect2.top=(self.width-self.tool_width+4,255)
        self._display_surf.blit(textSurf2, textRect2)
        
        textSurf2, textRect2 = self.text_objects("2. Sélectionner l'intérêt", smallText)
        textRect2.left,textRect2.top=(self.width-self.tool_width+4,267)
        self._display_surf.blit(textSurf2, textRect2)
        
        textSurf2, textRect2 = self.text_objects("3. Le degrée de description", smallText)
        textRect2.left,textRect2.top=(self.width-self.tool_width+4,279)
        self._display_surf.blit(textSurf2, textRect2)
        
        textSurf2, textRect2 = self.text_objects("4. Confirm", smallText)
        textRect2.left,textRect2.top=(self.width-self.tool_width+4,291)
        self._display_surf.blit(textSurf2, textRect2)
        
        textSurf2, textRect2 = self.text_objects("5. Cliquer pour avancer", smallText)
        textRect2.left,textRect2.top=(self.width-self.tool_width+4,303)
        self._display_surf.blit(textSurf2, textRect2)
        
    def update_score(self):
        """ affiche le tableau de score
        Attr: 
        Return:
            None
        """
        #scores(list(tuple(int))) : score optenu pour chaque chemin (general, dist, danger, préférence)
        #score: total,rapitite,securite,preference
        scores=self.dt.list_score_tout_les_chemins_affichage
        
        names_score = self.dt.list_name_tout_les_chemins_affichage
        names=self.dt.list_name_tout_les_chemins
        score_surf=pygame.Surface((self.tool_width-10,self.height-300))
        score_surf.fill(GREY)
        smallText = pygame.font.SysFont("comicsansms",12)
        
        param=[" rapidité "," securité "," intérêt "," total "]
        x,y=105,0
        #titre
        textSurf, textRect = self.text_objects("tableau de score de différents cheimins : ", smallText)
        textRect.left,textRect.top=(0,0)
        w,h=textRect.size
        y=h
        score_surf.blit(textSurf, textRect)
        #affiche la ligne param
        for i in range(len(param)):
            textSurf, textRect = self.text_objects(param[i], smallText)
            textRect.left,textRect.top=(x,y)
            w,h=textRect.size
            x+=w
            score_surf.blit(textSurf, textRect)
        y=2*h
        #affiche chaque score ligne par ligne
        for i in range(len(scores)):
            
            score=scores[i]
            textSurf, textRect = self.text_objects(names_score[i], smallText)
            textRect.left,textRect.top=(0,y)
            score_surf.blit(textSurf,textRect)
            x=120
            for j in [1,2,3,0]:
                textSurf, textRect = self.text_objects(str("%.2f"%score[j]), smallText)
                textRect.left,textRect.top=(x,y)
                x+=50
                score_surf.blit(textSurf,textRect) 

            y=y+textRect.height

        #note
        textSurf, textRect = self.text_objects("(Note 1 : on cherche une minimisation des scores)", smallText)
        textRect.left,textRect.top=(0,y+2)
        score_surf.blit(textSurf, textRect)
        textSurf2, textRect2 = self.text_objects("(Note 2 : les chemins générés ne sont pas forcément les plus optimaux)", smallText)
        textRect2.left,textRect2.top=(0,y+17)
        score_surf.blit(textSurf2, textRect2)
        self._display_surf.blit(score_surf,((self.width-self.tool_width+10,self.height-self.discription_height)))  

    def one_step(self):
        """ function execute quand on click confirm
        mets a jour les paramettres (restriction,choix de discription,path)
        laisser utilisateur avancer le robot pour voir les descriptions etape par etape.
        """
        self.iteration=0
        self.restriction=[(self.rapid.value,self.secu.value,self.preference.value)]
        # print("lvl secu =>",DICO_ACCURACY[self.accuracy.option_list[self.accuracy.selected]])
        self.discription=self.dt.descriptiontTrajectoirePlusExplication(agent_rayon=self.radius, ltuple_rest=self.restriction,lobjet=self.option.list_sel, path_donners=self.drawingpath, precision = DICO_ACCURACY[self.accuracy.option_list[self.accuracy.selected]])
        self.list_msg = Traduction.Description_to_Txt2(self.discription, self.label)
        for path in self.dt.list_tout_les_chemins:
            for y, x in path:
                if (y,x) not in self.dt.path:
                    s = pygame.Surface((16,16))  # the size of your rect
                    s.set_alpha(ALPHA)                # alpha level
                    s.fill(BLUE)           # this fills the entire surface
                    self._display_surf.blit(s,(x*16,y*16))
        
        for y, x in self.dt.path:
            s = pygame.Surface((16,16))  # the size of your rect
            s.set_alpha(ALPHA)                # alpha level
            s.fill(green)           # this fills the entire surface
            self._display_surf.blit(s,(x*16,y*16))
        for path in self.drawingpath:
            for y, x in path:
                s = pygame.Surface((16,16))  # the size of your rect
                s.set_alpha(ALPHA)                # alpha level
                s.fill(green)           # this fills the entire surface
                self._display_surf.blit(s,(x*16,y*16))

        self.on_render()
        self.chemin()
        self.construction()
        
    def chemin(self):
        """
        laisser utilisateur avancer le robot pour voir les descriptions etape par etape.
        """

        self.iteration=0
        while( not self.done() ):
            self.forward = False
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                self.on_event(event)
            if self.forward:
                self.on_loop()
                self.on_render()
            self.button('reset', self.width-(self.tool_width*2/3),0, 90, 40, green,bright_green, self.reset)

        
        

    def on_loop(self):
        self.iteration +=1
        
    def on_render(self, inter = False):
        """
        afficher tableau de score 
        mettre a jour la postion de robot et la description correspondante.
        """ 
        #afficher map
        for x, y, image in self.layer.tiles():
            self._display_surf.blit(image,(x*16,y*16))
        y, x = self.dt.path[self.iteration]
        #afficher robot et rayon
        self.draw_circle_alpha( self._display_surf, (255,0,0), ((x+0.5)*16,(y+0.5)*16), self.radius*16)
        self.update_score()
        
        #discription correspondante
        msg=self.list_msg[self.iteration]

        self._display_surf.blit(self.robot_dir[self.discription[self.iteration][0]],(x*16,y*16))
        #afficher path
        if not inter:
            for path in self.dt.list_tout_les_chemins:
                for y, x in path:
                    if (y, x) not in self.dt.path:
                        s = pygame.Surface((16,16))  # the size of your rect
                        s.set_alpha(ALPHA)                # alpha level
                        s.fill(BLUE)           # this fills the entire surface
                        self._display_surf.blit(s,(x*16,y*16))
        
        for y, x in self.dt.path:
            s = pygame.Surface((16,16))  # the size of your rect
            s.set_alpha(ALPHA)                # alpha level
            s.fill(green)           # this fills the entire surface
            self._display_surf.blit(s,(x*16,y*16))
        if not inter:
            for path in self.drawingpath:
                for y, x in path:
                    s = pygame.Surface((16,16))  # the size of your rect
                    s.set_alpha(ALPHA)                # alpha level
                    s.fill(green)           # this fills the entire surface
                    self._display_surf.blit(s,(x*16,y*16))
        
        #affiche la discription
        if not inter:
            self.set_discription(self._display_surf,msg)
        
        pygame.display.update()

    def draw_circle_alpha(self, surface, color, center, radius):
        """ dessine un cercle avec la couleur et le rayon souaité
        Attr: 
            surface : la surface où faire le dessin
            color : la couleur du cercle au format (R,G,B)
            center : le centre du cercle
            radius : le rayon
        Return:
            None
        """
        target_rect = pygame.Rect(center, (0, 0)).inflate((radius * 2, radius * 2))
        shape_surf = pygame.Surface(target_rect.size, pygame.SRCALPHA)
        shape_surf.set_alpha(ALPHA)
        pygame.draw.circle(shape_surf, color, (radius, radius), radius)
        surface.blit(shape_surf, target_rect)

    def text_objects(self,text, font):
        textSurface = font.render(text, True, black)
        return textSurface, textSurface.get_rect()
 
    def button(self,msg,x,y,w,h,ic,ac,action=None):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        if x+w > mouse[0] > x and y+h > mouse[1] > y:
            pygame.draw.rect(self._display_surf, ac,(x,y,w,h))

            if click[0] == 1 and action != None:
                action()         
        else:
            pygame.draw.rect(self._display_surf, ic,(x,y,w,h))

        smallText = pygame.font.SysFont("comicsansms",12)
        textSurf, textRect = self.text_objects(msg, smallText)
        textRect.center = ( (x+(w/2)), (y+(h/2)) )
        self._display_surf.blit(textSurf, textRect)

    def set_discription(self,surface,discription):
        """ dessine la zone de description et affiche le text l'intant présent
        Attr: 
            surface : la surface où faire le dessin
            discription : la classe description qui permet de recuperer les description celon le chemin
        Return:
            None
        """
        discp_surf=pygame.Surface((self.width-self.tool_width,self.discription_height))
        discp_surf.fill(GREY)
        
        font=pygame.font.SysFont('Times', 18)
        discrip1=discription.split("[NewLine]")


        text_click = font.render("clicker pour voir la suite de la description.", True, (0,0,0), GREY)
        text_click_w, text_click_h = text_click.get_size()

        y=16
        x=0
        text_w, text_h = 0,0
        i = 0
        remove_blue = False
        for discription_tmp in discrip1:

            discrip=discription_tmp.split(" ")
            # print(discrip)
            for word in discrip:
                if len(word) > 0 and word[0] == '[':
                    
                    if not remove_blue:
                        self.on_render(True)
                        remove_blue = True
                    color = LIST_COLOR[i%len(LIST_COLOR)]
                    for y_tmp, x_tmp in self.dt.dict_des_chemins[word[1:-1]]:
                        if (y_tmp, x_tmp) not in self.dt.path:
                            s = pygame.Surface((16,16))    # the size of your rect
                            s.set_alpha(ALPHA)                # alpha level
                            s.fill(color)# this fills the entire surface
                            self._display_surf.blit(s,(x_tmp*16,y_tmp*16))
                    text = font.render("=>", True, color, GREY)
                    text_w, text_h = text.get_size()
                    if(y>=self.discription_height - 4 * text_click_h):
                        x=0
                        y=y+text_click_h
                        discp_surf.blit(text_click, (x, y))
                        self._display_surf.blit(discp_surf,((0,self.height-self.discription_height)))
                        pygame.display.update()
                        push = False
                        while (not push):
                            event_list = pygame.event.get()
                            for event in event_list:
                                if event.type == pygame.QUIT:
                                    pygame.quit()
                                    quit()
                                elif event.type == pygame.MOUSEBUTTONDOWN:
                                    push = True
                                    x=0
                                    y=16
                                    discp_surf.fill(GREY)
                    discp_surf.blit(text, (x, y))
                    x=x+text_w
                    if(x>(self.width-self.tool_width-90)):
                        x=0
                        y=y+text_h
                    i = i+1
                text = font.render(word+" ", True, (0,0,0), GREY)
                text_w, text_h = text.get_size()
                if(y>=self.discription_height - 2 * text_click_h):
                        x=0
                        y=y+text_click_h
                        discp_surf.blit(text_click, (x, y))
                        self._display_surf.blit(discp_surf,((0,self.height-self.discription_height)))
                        pygame.display.update()
                        push = False
                        while (not push):
                            event_list = pygame.event.get()
                            for event in event_list:
                                if event.type == pygame.QUIT:
                                    pygame.quit()
                                    quit()
                                elif event.type == pygame.MOUSEBUTTONDOWN:
                                    push = True
                                    x=0
                                    y=16
                                    discp_surf.fill(GREY)
                discp_surf.blit(text, (x, y))
                x=x+text_w
                if(x>(self.width-self.tool_width-90)):
                    x=0
                    y=y+text_h
            x=0
            y=y+text_h
        self._display_surf.blit(discp_surf,((0,self.height-self.discription_height)))


        #action lier au event
    def on_lbutton_up(self, event):
        self.forward = False
    def on_mbutton_up(self, event):
        pass
    def on_rbutton_up(self, event):
        pass
    def on_lbutton_down(self, event):
        pos = pygame.mouse.get_pos()
        if pos[0] < self.width - self.tool_width and pos[1] < self.height - self.discription_height:
            self.forward = True
    def on_mbutton_down(self, event):
        pass
    def on_rbutton_down(self, event):
        pass
        
    def on_event(self, event):
        if event.type == pygame.QUIT:
            self._running = False
        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                self.on_lbutton_up(event)
            elif event.button == 2:
                self.on_mbutton_up(event)
            elif event.button == 3:
                self.on_rbutton_up(event)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                self.on_lbutton_down(event)
            elif event.button == 2:
                self.on_mbutton_down(event)
            elif event.button == 3:
                self.on_rbutton_down(event)
    
    def on_cleanup(self):
        pygame.quit()
    
    def done(self):
        return not self._running or self.iteration + 1 >= len(self.dt.path)

    def on_execute(self):
        if self.on_init() == False:
            self._running = False

        self.on_cleanup()