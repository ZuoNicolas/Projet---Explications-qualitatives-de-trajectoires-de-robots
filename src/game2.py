import pygame
import pytmx
import xml.etree.ElementTree as ET
import time
import descriptionTrajectoire as DT
import readfile
clock = pygame.time.Clock()
black = (0,0,0)
white = (255,255,255)

red = (200,0,0)
green = (0,200,0)

bright_red = (255,0,0)
bright_green = (0,255,0)
 
block_color = (53,115,255)

class Game(object):

    def __init__(self, filename, map, path, label, radius=5):
        self._running = True
        self._display_surf = None
        self.filename = filename

        self.path = path
        self.iteration = 0
        self.forward = True
        self.radius = radius
        self.dt =DT.DescriptionTrajectoire(map, path, label)
        self.map=map
        self.label=label

    def on_init(self):
        pygame.init()
        
        root = ET.parse(self.filename).getroot()
        self.size = self.weight, self.height = (int(root.get("width"))+10) * 16, (int(root.get("height"))+2) * 16  #a changer
        print(self.size)
        #zone d'affichage
        self._display_surf = pygame.display.set_mode(self.size, pygame.HWSURFACE | pygame.DOUBLEBUF)
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
    def add_buttons(self):
        self.construction()
        list_obj=self.list_objets()
        while True:
            for event in pygame.event.get():
            #print(event)
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
            pos_x=self.weight-10*16
            pos_y=0
            print("obj",list_obj)
            for obj in list_obj:
                if(pos_y+40 >=(self.height-2*16)):
                    pos_x=pos_x+90
                    pos_y=0
                self.button(obj,pos_x,pos_y,90,40,green,bright_green,self.one_step)
                
                pos_y=pos_y+40
                
            pygame.display.update()
            clock.tick(15)

    def list_objets(self):
        list_obj=[]
        for x in range(len(self.map)):
            for y in range(len(self.map[0])):
                objet = self.label.get(self.map[x][y]).get('name') 
                if(objet not in list_obj):
                    list_obj.append(objet)
        return list_obj

    def click_avance(self):
        self.construction()
        while True:
            for event in pygame.event.get():
            #print(event)
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
            self.button("avancer",0,self.height-10*16,50,self.height-10*16+50,green,bright_green,self.click_jusqu_a)
            pygame.display.update()
            clock.tick(15)

    def construction(self):
        self._display_surf.fill(white)
        for x, y, image in self.layer.tiles():
            self._display_surf.blit(image,(x*16,y*16))
        y, x = self.path[self.iteration]
        self.draw_circle_alpha( self._display_surf, (255,0,0), ((x+0.5)*16,(y+0.5)*16), self.radius*16)
        
        self._display_surf.blit(self.robot,(x*16,y*16))
        for y, x in self.path:
            s = pygame.Surface((16,16))  # the size of your rect
            s.set_alpha(50)                # alpha level
            s.fill((0,0,255))           # this fills the entire surface
            self._display_surf.blit(s,(x*16,y*16))
        discp_surf=pygame.Surface((self.weight,2*16))
        discp_surf.fill(block_color)
        self._display_surf.blit(discp_surf,((0,self.height-2*16)))
    
    def click_jusqu_a(self):

        while True:
            for event in pygame.event.get():
            #print(event)
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
            self.construction()
            self.button("jusqu_a",50,self.height-10*16,50,self.height-10*16+50,green,bright_green,self.one_step)

            pygame.display.update()
            clock.tick(15)
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
    def one_step(self):
        if not self.done():
            self.on_render()
        while( not self.done() ):
            self.forward = False
            for event in pygame.event.get():
                self.on_event(event)
            if self.forward:
                self.on_loop()
                self.on_render()

    def on_loop(self):
        self.iteration +=1
        
    def on_render(self):

        for x, y, image in self.layer.tiles():
            self._display_surf.blit(image,(x*16,y*16))
        y, x = self.path[self.iteration]
        self.draw_circle_alpha( self._display_surf, (255,0,0), ((x+0.5)*16,(y+0.5)*16), self.radius*16)
        msg = self.dt.descriptiontTrajectoireActif(self.radius, saw=False, iterator=self.iteration)
        print(self.iteration,':',msg)
        self._display_surf.blit(self.robot,(x*16,y*16))
        for y, x in self.path:
            s = pygame.Surface((16,16))  # the size of your rect
            s.set_alpha(50)                # alpha level
            s.fill((0,0,255))           # this fills the entire surface
            self._display_surf.blit(s,(x*16,y*16))
        #affiche la discription
        self.set_discription(self._display_surf,msg)

        pygame.display.update()
        clock.tick(15)


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
        print(click)
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
        discp_surf=pygame.Surface((self.weight,2*16))
        discp_surf.fill(block_color)
        font=pygame.font.SysFont('Times', 12)
        discrip=discription.split("/")
        y=0
        for d in discrip[1:]:

            text = font.render(d, True, (0,0,0), (255,255,255))
            text_w, text_h = text.get_size()
            discp_surf.blit(text, (0, y))
            y=y+text_h
        self._display_surf.blit(discp_surf,((0,self.height-2*16)))
    def on_cleanup(self):
        pygame.quit()
    
    def done(self):
        return not self._running or self.iteration + 1 >= len(self.path)

    def on_execute(self):
        if self.on_init() == False:
            self._running = False
        self.add_buttons()
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