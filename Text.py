import pygame

from constants import WIDTH
from constants import HEIGHT

class Text:

    font = 'Orbitron-VariableFont_wght.ttf'
    fontsize = 30

    def __init__(self, screen, pos, bg_active=False, bgcolor=(0,0,0), fontsize=fontsize):

        self.screen = screen
        self.bg_active = bg_active

        pygame.font.init()
        self.loaded_font = pygame.font.Font(self.font, fontsize)
        self.textsurface = self.loaded_font.render("", False, (255, 255, 255))
        self.initial_pos = pos
        self.pos = (pos[0] - self.textsurface.get_width()/2, pos[1] - self.textsurface.get_height()/2)

        if(self.bg_active):
            self.bg = pygame.Surface((self.textsurface.get_width(),self.textsurface.get_height()))
            self.bg.fill(bgcolor) 


    def draw(self):

        if(self.bg_active):
            self.screen.blit(self.bg,self.pos)

        self.screen.blit(self.textsurface,self.pos)


    def update_text(self, text):
        self.text = text
        self.textsurface = self.loaded_font.render(text, False, (255, 255, 255))
        self.pos = (self.initial_pos[0] / 2 - self.textsurface.get_width()/2, self.initial_pos[1] / 2 - self.textsurface.get_height()/2)