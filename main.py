import pygame
from snowaman import snowman
from icecream import ice_cream
from penguin import penguins

display_width = 900
display_height = 700
screen = pygame.display.set_mode((display_width, display_height))

jump_height_sm = 20
gravity = 1
snowman_velocity = jump_height_sm
jump_height_p = 20
p_velocity = jump_height_p
jumping = False
jump = False

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

p = penguins(500,500)
p_x, p_y = 200, 400
p_rect = pygame.Rect(370, 250, 200, 100)
# snowman_rect = pygame.Rect(370, 250, 250, 100)
STANDING_SURFACE_PENGUIN = pygame.transform.scale(pygame.image.load("Penguin.png"), (200,400))
JUMPING_SURFACE_PENGUIN = pygame.transform.scale(pygame.image.load("Penguin.png"), (200, 400))
penguin_page = False

#snowman
s = snowman(400,500)
sm_x, sm_y = 200, 600
snowman_rect = pygame.Rect(370, 250, 200, 100)
STANDING_SURFACE_SNOWMAN = pygame.transform.scale(pygame.image.load("snowman.png"), (200,400))
JUMPING_SURFACE_SNOWMAN = pygame.transform.scale(pygame.image.load("snowman.png"), (200, 400))

#icecream
cream = ice_cream(100,100)
c_x, c_y = 200, 400
STANDING_SURFACE_ICECREAM = pygame.transform.scale(pygame.image.load("icecream.png"), (20, 400))
JUMPING_SURFACE_ICECREAM = pygame.transform.scale(pygame.image.load("icecream.png"), (20,400))


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
count = 0
counts = 0
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
            if (next_page == True):
                    if count == 0:
                        jumping = True
                        count += 1
                    # jumping = True
                        print(jumping)
    if jumping:
        print("I can jump")
        sm_y -= snowman_velocity
        snowman_velocity -= gravity
    if sm_y <= jump_height_sm:
        print("hell")
        jumping = False
        sm_y = jump_height_sm
        s.rect = JUMPING_SURFACE_SNOWMAN.get_rect(center=(sm_x, sm_y))
                        # screen.blit(JUMPING_SURFACE_SNOWMAN, s.rect)
    else:
        s.rect = STANDING_SURFACE_SNOWMAN.get_rect(center=(sm_x, sm_y))
            # screen.blit(STANDING_SURFACE_SNOWMAN, s.rect)

        if (events.type == pygame.MOUSEBUTTONDOWN and p.rect.collidepoint(events.pos) and starting_menu == False):
            print("User clicked something!")
            penguin_page = True
            if (penguin_page == True):
                if counts == 0:
                    jump = True
                    counts += 1
                    print(jump)
    if jump:
        print("I can jump")
        p_x -= p_velocity
        p_velocity -= gravity
    if p_x <= jump_height_p:
        print("ok")
        jump = False
        p_y = jump_height_p
        cream.rect = JUMPING_SURFACE_PENGUIN.get_rect(center=(c_x, c_y))

    else:
        cream.rect = STANDING_SURFACE_PENGUIN.get_rect(center=(c_x, c_y))



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
        # screen.blit(cream.image, cream.rect)
        screen.blit(p.image, p.rect)
        # screen.blit(second_picture, (0,0))

    if next_page == True or penguin_page == True:
        screen.blit(second_picture, (0,0))
        # screen.blit(s.image, s.rect)


    if jumping == True and next_page == True:
        screen.blit(JUMPING_SURFACE_SNOWMAN, s.rect)

    if jump == True and penguin_page == True:
        screen.blit(JUMPING_SURFACE_PENGUIN, p.rect)

    # if jump == True and icecream_page == True:
    #     screen.blit(JUMPING_SURFACE_ICECREAM, cream.rect)


 # Update the game state
    pygame.display.update()






