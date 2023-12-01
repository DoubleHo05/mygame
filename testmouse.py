import pygame
from sys import exit
pygame.init()

screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()

pygame.mouse.set_visible(False)
cursor_img = pygame.image.load('normal.png')
cursor_img_rect = cursor_img.get_rect()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.fill((255, 255, 255))
    cursor_img_rect.center = pygame.mouse.get_pos()
    screen.blit(cursor_img, cursor_img_rect)


    pygame.display.update()
    clock.tick(60)