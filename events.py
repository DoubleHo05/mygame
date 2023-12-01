from newsettings import *

class Events():
    def __init__(self):
        self.surface = pygame.Surface((EVENTS_WIDTH, EVENTS_HEIGHT))
        self.rect = self.surface.get_rect()
        self.display_surface = pygame.display.get_surface()

    def run(self):
        self.display_surface.blit(self.surface, (EVENTS_X, EVENTS_Y))
        