import pygame
import time
import random

pygame.init()

display_width = 800
display_height = 600
screen = pygame.display.set_mode((display_width, display_height))

def start_menu():
    screen.fill((0,0,0))
    font = pygame.font.SysFont('arial', 40)
    title = font.render('World of Wonders', True, (255, 255, 255))
    start_button = font.render('Start', True, (255, 255, 255))
    screen.blit(title, (display_width/2 - title.get_width()/2), (display_height/2 - title.get_height()/2))
    screen.blit(start_button, (display_width/2 - start_button.get_width()/2), (display_height/2 + start_button.get_height()/2))
    pygame.display.update()

game_start = "start_menu"
while True:
    for events in pygame.event.get():
        if events.type == pygame.QUIT:
            pygame.quit()
            quit()
    if game_start == "start_menu":
        start_menu()




