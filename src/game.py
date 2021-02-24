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
        self.radius = radius
        self.dt = DT.DescriptionTrajectoire(map,path,label)
        
    def on_init(self):
        pygame.init()
        
        root = ET.parse(self.filename).getroot()
        self.size = self.weight, self.height = int(root.get("height")) * 16, int(root.get("width")) * 16 #a changer
        print(self.size)
        #zone d'affichage
        self._display_surf = pygame.display.set_mode(self.size, pygame.HWSURFACE | pygame.DOUBLEBUF)
        self._running = True
        
        tm = pytmx.load_pygame(self.filename, pixelalpha=True)
        self.layer = tm.get_layer_by_name(root.find('layer').get("name"))
        #image de robot
        self.robot = pygame.image.load("../ressource/robot16.png").convert()

        self.image_dict = dict()
        for x, y, image in self.layer.tiles():
	        self.image_dict[(x, y)] = image
 
    def on_event(self, event):
        if event.type == pygame.QUIT:
            self._running = False

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
        pygame.display.flip()

    def draw_circle_alpha(self, surface, color, center, radius):
        target_rect = pygame.Rect(center, (0, 0)).inflate((radius * 2, radius * 2))
        shape_surf = pygame.Surface(target_rect.size, pygame.SRCALPHA)
        shape_surf.set_alpha(50)
        pygame.draw.circle(shape_surf, color, (radius, radius), radius)
        surface.blit(shape_surf, target_rect)
        
    def on_cleanup(self):
        pygame.quit()
    
    def done(self):
        return not self._running or self.iteration + 1 >= len(self.path)

    def on_execute(self):
        if self.on_init() == False:
            self._running = False
 
        while( not self.done() ):
            time.sleep(0.5)
            for event in pygame.event.get():
                self.on_event(event)
            self.on_loop()
            self.on_render()
        self.on_cleanup()

if __name__ == "__main__" :
    map = readfile.read_map_tmx('../ressource/zone_a_danger(rocher).tmx')
    label = readfile.read_desc_xml('../ressource/descripteur.tsx')
    theApp = Game('../ressource/zone_a_danger(rocher).tmx', map, [(11, 17), (12, 17), (12, 16), (12, 15), (12, 14), (13, 14), (13, 13), (13, 12), (14, 12), (14, 11), (15, 11), (15, 10), (16, 10), (17, 10), (18, 10), (19, 10), (20, 10), (21, 10), (22, 10), (23, 10), (24, 10), (25, 10), (26, 10), (27, 10), (28, 10), (28, 11), (29, 11), (29, 12), (30, 12), (30, 13), (31, 13), (31, 14), (31, 15), (31, 16), (31, 17), (30, 17)],label,)
    theApp.on_execute()