import pygame
import pytmx
import xml.etree.ElementTree as ET
import time
import descriptionTrajectoire as DT
import readfile


class Game(object):

    def __init__(self, filename, map, path, label, radius=5):
        self._running = True
        self._display_surf = None
        self.filename = filename

        self.path = path
        self.iteration = 0
        self.forward = True
        self.radius = radius
        self.dt = DT.DescriptionTrajectoire(map,path,label)
        
    def on_init(self):
        pygame.init()
        
        root = ET.parse(self.filename).getroot()
        self.size = self.weight, self.height = int(root.get("width")) * 16, (int(root.get("height"))+10) * 16  #a changer
        print(self.size)
        #zone d'affichage
        self._display_surf = pygame.display.set_mode(self.size, pygame.HWSURFACE | pygame.DOUBLEBUF)
        
        self._running = True
        pygame.display.set_caption('robot')#ecrire le titre de window
        
        tm = pytmx.load_pygame(self.filename, pixelalpha=True)
        self.layer = tm.get_layer_by_name(root.find('layer').get("name"))
        #image de robot
        self.robot = pygame.image.load("../ressource/robot16.png").convert()

        self.image_dict = dict()
        for x, y, image in self.layer.tiles():
	        self.image_dict[(x, y)] = image
 
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
        pygame.display.flip()
    def draw_circle_alpha(self, surface, color, center, radius):
        target_rect = pygame.Rect(center, (0, 0)).inflate((radius * 2, radius * 2))
        shape_surf = pygame.Surface(target_rect.size, pygame.SRCALPHA)
        shape_surf.set_alpha(50)
        pygame.draw.circle(shape_surf, color, (radius, radius), radius)
        surface.blit(shape_surf, target_rect)


    def set_discription(self,surface,discription):
        discp_surf=pygame.Surface((self.weight,10*16))
        discp_surf.fill((255,255,255))
        font=pygame.font.SysFont('Times', 12)
        discrip=discription.split("/")
        y=0
        for d in discrip:
            text = font.render(d, True, (0, 0, 255), (0, 255, 0))
            text_w, text_h = text.get_size()
            discp_surf.blit(text, (0, y))
            y=y+text_h
        self._display_surf.blit(discp_surf,((0,self.height-10*16)))
    def on_cleanup(self):
        pygame.quit()
    
    def done(self):
        return not self._running or self.iteration + 1 >= len(self.path)

    def on_execute(self):
        if self.on_init() == False:
            self._running = False
 
        if not self.done():
            self.on_render()
        while( not self.done() ):
            self.forward = False
            for event in pygame.event.get():
                self.on_event(event)
            if self.forward:
                self.on_loop()
                self.on_render()
        self.on_cleanup()
