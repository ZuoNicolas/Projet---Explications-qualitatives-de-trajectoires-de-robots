import pygame, math, sys

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 50, 50)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 50)
BLUE = (50, 50, 255)
GREY = (200, 200, 200)
ORANGE = (200, 100, 50)
CYAN = (0, 255, 255)
MAGENTA = (255, 0, 255)
TRANS = (1, 1, 1)

class OptionBox():

    def __init__(self, x, y, w, h, color, highlight_color, font, option_list, selected = 0,multiselection=True):
        self.color = color
        self.highlight_color = highlight_color
        self.rect = pygame.Rect(x, y, w, h)
        self.font = font
        self.option_list = option_list
        self.selected = selected
        self.draw_menu = False
        self.menu_active = False
        self.active_option = -1
        self.selections=[]
        self.list_sel=[]
        self.multiselection=multiselection
    def set_rect(self,x,y,w,h):
        self.rect = pygame.Rect(x, y, w, h)
    def draw(self, surf):
        pygame.draw.rect(surf, self.highlight_color if self.menu_active else self.color, self.rect)
        pygame.draw.rect(surf, (0, 0, 0), self.rect, 2)
        m=""
        self.list_sel=[]
        if(self.multiselection):
            for i in self.selections:
                m=m+self.option_list[i]+' '
                self.list_sel.append(self.option_list[i])
        else:
            m=self.option_list[self.selected]
        msg = self.font.render(m, 1, (0, 0, 0))
        surf.blit(msg, msg.get_rect(center = self.rect.center))

        if self.draw_menu:
            for i, text in enumerate(self.option_list):
                rect = self.rect.copy()
                rect.y += (i+1) * self.rect.height
                if(self.multiselection):
                    pygame.draw.rect(surf, self.highlight_color if i in self.selections else self.color, rect)
                else:
                    pygame.draw.rect(surf, self.highlight_color if i==self.selected else self.color, rect)
                msg = self.font.render(text, 1, (0, 0, 0))
                surf.blit(msg, msg.get_rect(center = rect.center))
            outer_rect = (self.rect.x, self.rect.y + self.rect.height, self.rect.width, self.rect.height * len(self.option_list))
            pygame.draw.rect(surf, (0, 0, 0), outer_rect, 2)
    def update(self, event_list):
        mpos = pygame.mouse.get_pos()
        self.menu_active = self.rect.collidepoint(mpos)
        
        self.active_option = -1
        for i in range(len(self.option_list)):
            rect = self.rect.copy()
            rect.y += (i+1) * self.rect.height
            if rect.collidepoint(mpos):
                self.active_option = i
                break
        if not self.menu_active and self.active_option == -1:
            self.draw_menu = False

        for event in event_list:
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if self.menu_active:
                    self.draw_menu = not self.draw_menu
                elif self.draw_menu and self.active_option >= 0:
                    if(self.active_option in self.selections):
                        self.selections.remove(self.active_option)
                    else:
                        self.selections.append(self.active_option)
                    self.selected = self.active_option

                    self.draw_menu = False
                    return self.active_option
        return -1




class Slider():
    def __init__(self, name, value, maxi, mini, pos,y_pos):
        self.value = value  # start value
        self.maxi = maxi  # maximum at slider position right
        self.mini = mini  # minimum at slider position left
        self.xpos = pos  # x-location on screen
        self.ypos = y_pos
        self.val=(self.maxi-self.mini)*self.value+self.mini
        self.name=name


        self.surf = pygame.surface.Surface((100, 50))
        #font = pygame.font.SysFont("Verdana", 12)
        self.hit = False  # the hit attribute indicates slider movement due to mouse interaction
        font = pygame.font.SysFont("Verdana", 12)
        self.txt_surf = font.render(name+':'+str(self.value), 1, BLACK)
        self.txt_rect = self.txt_surf.get_rect(center=(50, 15))

        # Static graphics - slider background #
        self.surf.fill((100, 100, 100))
        pygame.draw.rect(self.surf, GREY, [0, 0, 100, 50], 3)
        pygame.draw.rect(self.surf, ORANGE, [10, 10, 80, 10], 0)
        pygame.draw.rect(self.surf, WHITE, [10, 30, 80, 5], 0)

        self.surf.blit(self.txt_surf, self.txt_rect)  # this surface never changes

        # dynamic graphics - button surface #
        self.button_surf = pygame.surface.Surface((20, 20))
        self.button_surf.fill(TRANS)
        self.button_surf.set_colorkey(TRANS)
        pygame.draw.circle(self.button_surf, BLACK, (10, 10), 6, 0)
        pygame.draw.circle(self.button_surf, ORANGE, (10, 10), 4, 0)
        
    def draw(self,screen):
        """ Combination of static and dynamic graphics in a copy of
    the basic slide surface
    """
        # static
        surf = self.surf.copy()
        self.txt_surf.fill((255,255,255))
        surf.blit(self.txt_surf,self.txt_rect)
        font = pygame.font.SysFont("Verdana", 12)
        self.txt_surf = font.render(self.name+':'+"%.2f"%self.value, 1, BLACK)
        self.txt_rect = self.txt_surf.get_rect(center=(50, 15))
        surf.blit(self.txt_surf, self.txt_rect) 
        # dynamic
        pos = (10+int((self.val-self.mini)/(self.maxi-self.mini)*80), 33)
        self.button_rect = self.button_surf.get_rect(center=pos)
        surf.blit(self.button_surf, self.button_rect)
        self.button_rect.move_ip(self.xpos, self.ypos)  # move of button box to correct screen position
        # screen
        screen.blit(surf, (self.xpos, self.ypos))
        
    def move(self):
        """
    The dynamic part; reacts to movement of the slider button.
    """
        self.val = (pygame.mouse.get_pos()[0] - self.xpos - 10) / 80 * (self.maxi - self.mini) + self.mini
        if self.val < self.mini:
            self.val = self.mini
        if self.val > self.maxi:
            self.val = self.maxi
        self.value=(self.val-self.mini)/(self.maxi-self.mini ) 