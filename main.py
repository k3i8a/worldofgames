import pygame
from tkinter import *
import threading
import time
import random

pygame.init()

display_width = 800
display_height = 600
screen = pygame.display.set_mode((display_width, display_height))

window = Tk()
window.geometry("800x600")


stop = False

def ending_button():
    global stop
    stop = True

def starting_button():
    global stop
    stop = False

def button_starting():
    t = threading.Thread(target = starting_button)
    t.start()
def start_menu():
    screen.fill((0,0,0))
    # font = pygame.font.SysFont('arial', 40)
    title_font = pygame.font.SysFont('Times New Roman', 60)
    title = title_font.render('World of Wonders', True, (255, 255, 255))
    start_button = font.render('Start', True, (255, 255, 255))
    the_start = Button(window, text="START", padx=30, pady=20, command=button_starting)
    the_start.grid(columnspan=1, row=1, column=0)
    # quit_button = font.render('Quit', True, (255, 255, 255))
    screen.blit(title, ((display_width/2) - (title.get_width()/2), ((display_height/2) - (title.get_height()/2)) - 50))
    # screen.blit(start_button, ((display_width/2) - (start_button.get_width()/2), (display_height/2) + (start_button.get_height()/2)))
    # screen.blit(quit_button,  ((display_width/2) - (quit_button.get_width()/2), ((display_height/2) - (quit_button.get_height()/2)) + 90))
    # the_start = Button(window, text="START", padx=30, pady=20, command=button_starting)
    # the_start.grid(columnspan=1, row=1, column=0)
    the_end = Button(window, text="EXIT", padx=33, pady=22, command=ending_button)
    the_end.grid(row=2, column=0)
    window.mainloop()
    pygame.display.update()

game_start = "start_menu"
while True:
    for events in pygame.event.get():
        if events.type == pygame.QUIT:
            pygame.quit()
            quit()
    if game_start == "start_menu":
        start_menu()
        # the_start = Button(window, text = "START", padx = 30, pady = 20, command = button_starting)
        # the_start.grid(columnspan = 1, row = 1, column = 0)
        # the_end = Button(window, text = "EXIT", padx = 33, pady = 22, command = ending_button)
        # the_end.grid(row = 2, column = 0)
        # window.mainloop()

    # if game_start == "game":
    #     keys = pygame.key.get_pressed()
    # if game_start == "start_menu":
    #     keys = pygame.key.get_pressed()
    #     if keys[pygame.K_SPACE]:
    #
    #         game_start = "game "
    #         game_over = False







