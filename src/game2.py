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
ORANGE = (200, 100, 50)
CYAN = (0, 255, 255)
MAGENTA = (255, 0, 255)
TRANS = (1, 1, 1)

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
        list_image=["zone_non_carre2",'map1','zone_a_danger(rocher)']
        font=pygame.font.SysFont("Verdana", 12)
        self.images=slider.OptionBox(self.weight-(self.tool_width),0,120,30,(150, 150, 150), (100, 200, 255),font,list_image,0,False)
        while(not self.choose_image):
            self.choix_image()
    def choix_image(self):
        if(self.choose_parametre==True):
            self._display_surf.fill(white)
            self.loadimage()

        while not self.choose_image:
            event_list = pygame.event.get()
            for event in event_list:
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
            self.images.set_rect(self.weight-(self.tool_width),0,120,30)
            self.images.update(event_list)
            
            self.images.draw(self._display_surf)
            self.button('loadimage', self.weight-(self.tool_width/2),60, 90, 40, green,bright_green, self.func_choix_image)
            self.button('confirm', self.weight-(self.tool_width/2), 120, 90, 40, green,bright_green, self.set_choose)
            pygame.display.update()
        self.choose_parametre=False
        self.choix_parametre()
    def set_choose(self):
        self.choose_image=True
        self.loadimage()
    def func_choix_image(self):
        self.filename='../ressource/'+self.images.option_list[self.images.selected]+'.tmx'
        self.loadimage()
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

    def choix_parametre(self):
        self.secu = slider.Slider("sécurité", 0, 150, 10, self.weight-self.tool_width,0)
        self.rapid=slider.Slider("rapidité",0,150,10,self.weight-self.tool_width,60)
        self.preference=slider.Slider("préférence",0,150,10,self.weight-self.tool_width,120)
        self.slides=[self.secu,self.rapid,self.preference]

        list_obj=self.list_objets()
        font=pygame.font.SysFont("Verdana", 12)
        self.option=slider.OptionBox(self.weight-self.tool_width,180,90,30,(150, 150, 150), (100, 200, 255),font,list_obj)
        while (self.choose_parametre==False):
            self._display_surf.fill(white)
            self.construction()
            event_list = pygame.event.get()
            for event in event_list:
                if event.type == pygame.QUIT:
                    self.choose_image=False
                    self.choose_parametre=True
                    
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    for s in self.slides:
                        if s.button_rect.collidepoint(pos):
                            s.hit = True
                elif event.type == pygame.MOUSEBUTTONUP:
                    for s in self.slides:
                        s.hit = False
            # Move slides
            if(self.choose_parametre==True):
                break

            for s in self.slides:
                if s.hit:
                    s.move()
            
            for s in self.slides:
                s.draw(self._display_surf)
            self.button('confirm',self.weight-(self.tool_width/2),240,90,40,green,bright_green,self.one_step)
            self.drawpath()
            self.option.update(event_list)
            self.option.draw(self._display_surf)
            pygame.display.update()
        #clock.tick(speed.val)

    def drawpath(self):
        x = self.weight-(self.tool_width/2)
        y = 0
        self.button('my path', x, y, 90, 40, green,bright_green, self.func_drawpath)
        

    def func_drawpath(self):
        path = []
        self.drawingpath = []
        while self.drawingpath == []:
            event_list = pygame.event.get()
            for event in event_list:
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    if pos[0] < self.weight and pos[1] < self.height:
                        x,y = pos
                        x = x//16
                        y = y//16
                        print(self.drawingpath, path)
                        if (y,x) not in path:
                            path.append((y,x))
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
                s.set_alpha(50)                # alpha level
                s.fill(green)           # this fills the entire surface
                self._display_surf.blit(s,(x_tmp*16,y_tmp*16))
        self.draw_circle_alpha( self._display_surf, (255,0,0), ((x+0.5)*16,(y+0.5)*16), self.radius*16)
        
        self._display_surf.blit(self.robot,(x*16,y*16))
        discp_surf=pygame.Surface((self.weight,self.discription_height))
        discp_surf.fill(block_color)
        self._display_surf.blit(discp_surf,((0,self.height-self.discription_height)))
    
    def one_step(self):
        self.restriction=[(self.rapid.value,self.secu.value,self.preference.value)]
        print("Liste de restriction :\n",self.restriction)
        print(self.option.selections)
        self.discription=self.dt.descriptiontTrajectoirePlusExplication(agent_rayon=self.radius, ltuple_rest=self.restriction,lobjet=self.option.list_sel)
        self.list_msg = Traduction.Description_to_Txt2(self.discription, self.label)
        for path in self.dt.list_tout_les_chemins:
            for y, x in path:
                s = pygame.Surface((16,16))  # the size of your rect
                s.set_alpha(50)                # alpha level
                s.fill(BLUE)           # this fills the entire surface
                self._display_surf.blit(s,(x*16,y*16))

        for y, x in self.dt.path:
            s = pygame.Surface((16,16))  # the size of your rect
            s.set_alpha(50)                # alpha level
            s.fill(bright_red)           # this fills the entire surface
            self._display_surf.blit(s,(x*16,y*16))

        for path in self.drawingpath:
            for y, x in path:
                s = pygame.Surface((16,16))  # the size of your rect
                s.set_alpha(50)                # alpha level
                s.fill(green)           # this fills the entire surface
                self._display_surf.blit(s,(x*16,y*16))
        #print('list chemin',self.dt.list_tout_les_chemins)
        #print('my path',self.dt.path)
        pygame.display.update()
        self.chemin()
        self.construction()

    def chemin(self):
        if self.on_init() == False:
            self._running = False
 
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
        
    def on_render(self):

        for x, y, image in self.layer.tiles():
            self._display_surf.blit(image,(x*16,y*16))
        y, x = self.dt.path[self.iteration]
        self.draw_circle_alpha( self._display_surf, (255,0,0), ((x+0.5)*16,(y+0.5)*16), self.radius*16)
        
        
        #description_list =dt.descriptiontTrajectoireSimple(2)

        msg=self.list_msg[self.iteration]

        #msg = dt.descriptiontTrajectoireActif(self.radius, saw=False, iterator=self.iteration)
        #print(self.iteration,':',msg)
        self._display_surf.blit(self.robot,(x*16,y*16))

        for path in self.dt.list_tout_les_chemins:
            for y, x in path:
                s = pygame.Surface((16,16))  # the size of your rect
                s.set_alpha(50)                # alpha level
                s.fill(BLUE)           # this fills the entire surface
                self._display_surf.blit(s,(x*16,y*16))

        for y, x in self.dt.path:
            s = pygame.Surface((16,16))  # the size of your rect
            s.set_alpha(50)                # alpha level
            s.fill(bright_red)           # this fills the entire surface
            self._display_surf.blit(s,(x*16,y*16))

        for path in self.drawingpath:
            for y, x in path:
                s = pygame.Surface((16,16))  # the size of your rect
                s.set_alpha(50)                # alpha level
                s.fill(green)           # this fills the entire surface
                self._display_surf.blit(s,(x*16,y*16))
        
        #affiche la discription
        self.set_discription(self._display_surf,msg)

        pygame.display.update()
        #clock.tick(15)

    def draw_circle_alpha(self, surface, color, center, radius):
        target_rect = pygame.Rect(center, (0, 0)).inflate((radius * 2, radius * 2))
        shape_surf = pygame.Surface(target_rect.size, pygame.SRCALPHA)
        shape_surf.set_alpha(50)
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
        discp_surf=pygame.Surface((self.weight,self.discription_height))
        discp_surf.fill(block_color)
        font=pygame.font.SysFont('Times', 12)
        discrip=discription.split(" ")
        y=0
        x=0
        for word in discrip:

            text = font.render(word+" ", True, (0,0,0), (255,255,255))
            text_w, text_h = text.get_size()
            discp_surf.blit(text, (x, y))
            x=x+text_w
            if(x>=self.weight):
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