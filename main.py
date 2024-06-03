import pygame
from snowaman import snowman
from icecream import ice_cream

display_width = 900
display_height = 700
screen = pygame.display.set_mode((display_width, display_height))



pygame.init()
pygame.font.init()

background = pygame.image.load("village.jpg")
picture = pygame.transform.scale(background, (900, 700))

second_background = pygame.image.load("village_2.jpg")
second_picture = pygame.transform.scale(second_background, (900,700))

button_rect = pygame.Rect(370, 250, 250, 100)
button_surface = pygame.Surface((150, 50))

button_rect_two = pygame.Rect(370, 250, 250, 100)
button_surface_two = pygame.Surface((300, 100))


s = snowman(200,400)
snowman_rect = pygame.Rect(370, 250, 250, 100)
cream = ice_cream(400,400)

font = pygame.font.SysFont('Arial', 40)
title_font = pygame.font.SysFont('Times New Roman', 60)
title = title_font.render('World of Wonders', True, (255, 255, 255))
start_button = font.render('Start', True, (155, 155, 155))

start_text = "Start"
start_message = font.render(start_text, True, (225, 225, 225))
start_message_rect = pygame.Rect(390, 200, start_message.get_width() + 8, start_message.get_height() - 5)


end_text = "End"
ending_message = font.render(end_text, True, (225, 255, 255))
end_message_rect = pygame.Rect(400, 400, ending_message.get_width() + 8, ending_message.get_height() - 5)

stop = True
starting_menu = True
starting_button = False
next_page = False
icecream_page = False
while stop == True:
    for events in pygame.event.get():
        if events.type == pygame.QUIT:
            pygame.quit()
            quit()
            # Check for the mouse button down event
        if events.type == pygame.MOUSEBUTTONDOWN and start_message_rect.collidepoint(events.pos):
            print("Start button clicked")
            stop = True
            # starting_menu = False
        if events.type == pygame.MOUSEBUTTONDOWN and end_message_rect.collidepoint(events.pos):
            print("End button clicked")
            stop = False
        if events.type == pygame.MOUSEBUTTONDOWN and (start_message_rect.collidepoint(events.pos) or end_message_rect.collidepoint(events.pos)):
            starting_menu = False
        if (events.type == pygame.MOUSEBUTTONDOWN and s.rect.collidepoint(events.pos) and starting_menu == False):
            print("User clicked something!")
            next_page = True
        if (events.type == pygame.MOUSEBUTTONDOWN and cream.rect.collidepoint(events.pos) and starting_menu == False):
            icecream_page = True
            # if next_page == True:
            #









 # Shwo the button text
    if starting_menu == True and stop == True:
        screen.blit(title, (200,100))
        screen.blit(start_message, (390,200))
        start_message.get_rect().move(390, 200)
        pygame.draw.rect(screen, (255,255,255), start_message_rect, 2)

        screen.blit(ending_message, (400, 400))
        ending_message.get_rect().move(400, 400)
        pygame.draw.rect(screen, (255, 255, 255), end_message_rect, 2)

    if starting_menu == False:
        screen.blit(picture, (0,0))
        screen.blit(s.image, s.rect)
        screen.blit(cream.image, cream.rect)
        # screen.blit(second_picture, (0,0))

    if next_page == True:
        screen.blit(second_picture, (0,0))
        screen.blit(s.image, s.rect)
    if icecream_page == True:
        screen.blit(second_picture, (0, 0))
        screen.blit(cream.image, cream.rect)


 # Update the game state
    pygame.display.update()






