import pygame
import pytmx
import xml.etree.ElementTree as ET
import time
import descriptionTrajectoire2 as DT
import readfile
import Traduction
import slider 
from tools import *

#clock = pygame.time.Clock()
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
    'description' : 0,
    'description + comparaison' : 1,
    'tout' : 2
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
        list_image=["zone_non_carre2",'zone_a_danger(rocher)']
        font=pygame.font.SysFont("Verdana", 12)
        self.images=slider.OptionBox(self.weight-(self.tool_width),0,150,30,(150, 150, 150), (100, 200, 255),font,list_image,0,False)
        self.choix_image()
    def choix_image(self):
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
            self.images.set_rect(self.weight-(self.tool_width),0,150,30)
            self.images.update(event_list)
            self.images.draw(self._display_surf)
            self.accuracy.update(event_list)
            self.accuracy.draw(self._display_surf)

            for s in self.slides:
                s.draw(self._display_surf)

            self.button('loadimage', self.weight-(self.tool_width/2),0, 90, 40, green,bright_green, self.func_choix_image)
            self.button('confirm',self.weight-(self.tool_width),self.height-self.discription_height+90,90,40,green,bright_green,self.one_step)
            self.button('my path', self.weight-(self.tool_width),self.height-self.discription_height, 90, 40, green,bright_green, self.func_drawpath)

            if(self.option.draw_menu):
                self.option.draw(self._display_surf)
            if(self.images.draw_menu):
                self.images.draw(self._display_surf)
            if(self.accuracy.draw_menu):
                self.accuracy.draw(self._display_surf)
            

            pygame.display.update()
    def func_choix_image(self):
        self.filename='../ressource/'+self.images.option_list[self.images.selected]+'.tmx'
        self.loadimage()
        pygame.display.update()
    def loadimage(self):

        root = ET.parse(self.filename).getroot()
        self.map=readfile.read_map_tmx(self.filename)
        self.dt=DT.DescriptionTrajectoire(self.map,self.path,self.label)

        self.tool_width=20*16 #toolbar a droite de fenetre
        self.discription_height=10*16 #discription en bas de fenetre
        self.size = self.weight, self.height = (int(root.get("width"))) * 16+self.tool_width, (int(root.get("height"))) * 16+self.discription_height #a changer
        #print(self.size)
        #zone d'affichage
        self._display_surf = pygame.display.set_mode(self.size, pygame.RESIZABLE)
        self._display_surf.fill(white)
        self.drawingpath = []
        #self.zone_button=pygame.Surface((10*16,self.height))
        #self.zone_button.fill(block_color)



        self._running = True
        pygame.display.set_caption('robot')#ecrire le titre de window
        
        tm = pytmx.load_pygame(self.filename, pixelalpha=True)
        self.layer = tm.get_layer_by_name(root.find('layer').get("name"))
        #image de robot
        self.robot = pygame.image.load("../ressource/robot16.png").convert()

        self.image_dict = dict()
        self.construction()
        list_obj=self.list_objets()
        font=pygame.font.SysFont("Verdana", 12)
        self.option=slider.OptionBox(self.weight-self.tool_width/2,60,90,30,(150, 150, 150), (100, 200, 255),font,list_obj)
        self.accuracy = slider.OptionBox(self.weight-self.tool_width/2,self.height-self.discription_height,140,30,(150, 150, 150), (100, 200, 255),font,list(DICO_ACCURACY.keys()), 0, False)
        self.secu = slider.Slider("sécurité", 0, 150, 10, self.weight-self.tool_width,60)
        self.rapid=slider.Slider("rapidité",0,150,10,self.weight-self.tool_width,120)
        self.preference=slider.Slider("point d'interêt",0,150,10,self.weight-self.tool_width,180)
        self.slides=[self.secu,self.rapid,self.preference]

    def drawpath(self):
        x = self.weight-(self.tool_width/2)
        y = 0
        self.button('my path', x, y, 90, 40, green,bright_green, self.func_drawpath)
        

    def func_drawpath(self):
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
                    if pos[0] < self.weight - self.tool_width and pos[1] < self.height - self.discription_height:
                        x,y = pos
                        x = x//16
                        y = y//16
                        #print(self.drawingpath, path)
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
                        pygame.display.update()
                elif event.type == pygame.MOUSEBUTTONUP:
                    push = False
                elif event.type == pygame.MOUSEMOTION and push:
                    pos = pygame.mouse.get_pos()
                    if pos[0] < self.weight - self.tool_width and pos[1] < self.height - self.discription_height:
                        x,y = pos
                        x = x//16
                        y = y//16
                        #print(self.drawingpath, path)
                        if self.label.get(self.map[y][x]).get('canPass'):
                            if (y,x) not in path:
                                path.append((y,x))
                        self.construction()
                        for y, x in path:
                            s = pygame.Surface((16,16))  # the size of your rect
                            s.fill(BLUE)           # this fills the entire surface
                            self._display_surf.blit(s,(x*16,y*16))
                        pygame.display.update()
                self.drawingpath = find_path(self.map, self.label, path)
        
                        

    def list_objets(self):
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
        start,end=get_start_end(self.map,self.label)
        self._display_surf.fill(white)
        for x, y, image in self.layer.tiles():
            self._display_surf.blit(image,(x*16,y*16))
        y, x = start
        for path in self.drawingpath:
            for y_tmp, x_tmp in path:
                s = pygame.Surface((16,16))  # the size of your rect
                s.set_alpha(ALPHA)                # alpha level
                s.fill(green)           # this fills the entire surface
                self._display_surf.blit(s,(x_tmp*16,y_tmp*16))
        self.draw_circle_alpha( self._display_surf, (255,0,0), ((x+0.5)*16,(y+0.5)*16), self.radius*16)
        
        self._display_surf.blit(self.robot,(x*16,y*16))
        discp_surf=pygame.Surface((self.weight-self.tool_width,self.discription_height))
        discp_surf.fill(GREY)

        self._display_surf.blit(discp_surf,((0,self.height-self.discription_height)))
    
    def one_step(self):
        self.restriction=[(self.rapid.value,self.secu.value,self.preference.value)]
        print("Liste de restriction :\n",self.restriction)
        #print(self.option.selections)
        print("lvl secu =>",DICO_ACCURACY[self.accuracy.option_list[self.accuracy.selected]])
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
        #print('list chemin',self.dt.list_tout_les_chemins)
        #print('my path',self.dt.path)
        self.on_render()
        pygame.display.update()
        self.chemin()
        self.construction()

    def chemin(self):
 
        while( not self.done() ):
            self.forward = False
            for event in pygame.event.get():
                self.on_event(event)
            if self.forward:
                self.on_loop()
                self.on_render()
        self.iteration=0
        

    def on_loop(self):
        self.iteration +=1
        
    def on_render(self, inter = False):

        for x, y, image in self.layer.tiles():
            self._display_surf.blit(image,(x*16,y*16))
        y, x = self.dt.path[self.iteration]
        self.draw_circle_alpha( self._display_surf, (255,0,0), ((x+0.5)*16,(y+0.5)*16), self.radius*16)
        
        
        #description_list =dt.descriptiontTrajectoireSimple(2)

        msg=self.list_msg[self.iteration]

        #msg = dt.descriptiontTrajectoireActif(self.radius, saw=False, iterator=self.iteration)
        #print(self.iteration,':',msg)
        self._display_surf.blit(self.robot,(x*16,y*16))
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
        #clock.tick(15)

    def draw_circle_alpha(self, surface, color, center, radius):
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
        #print(click)
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
        discp_surf=pygame.Surface((self.weight-self.tool_width,self.discription_height))
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
                    if(x>(self.weight-self.tool_width-90)):
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
                if(x>(self.weight-self.tool_width-90)):
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
        if pos[0] < self.weight - self.tool_width and pos[1] < self.height - self.discription_height:
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
        #self.one_step()
        #if not self.done():
            #self.on_render()
        #while( not self.done() ):
            #self.forward = False
            #for event in pygame.event.get():
                #self.on_event(event)
            #if self.forward:
                #self.on_loop()
                #self.on_render()

        self.on_cleanup()