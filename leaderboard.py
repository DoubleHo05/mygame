from newsettings import *

class Leaderboard:
    def __init__(self):
        self.surface = pygame.Surface((LEADERBOARD_WIDTH, LEADERBOARD_HEIGHT))
        self.rect = self.surface.get_rect(topright = (1280, 0))
        self.display_surface = pygame.display.get_surface()
        self.image = pygame.transform.scale(pygame.image.load('leaderboard.png').convert_alpha(), (320, 150))

    def run(self):
        self.display_surface.blit(self.image, self.rect)

    