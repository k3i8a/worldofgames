import time
import random
import pygame
from snowaman import snowman
from clover import Clover
from penguin import penguins
from snowflake import Snowflake


display_width = 900
display_height = 700
screen = pygame.display.set_mode((display_width, display_height))




pygame.init()
pygame.font.init()
clock = pygame.time.Clock()


background = pygame.image.load("village.jpg")
picture = pygame.transform.scale(background, (900, 700))


second_background = pygame.image.load("village_2.jpg")
second_picture = pygame.transform.scale(second_background, (900,700))


button_rect = pygame.Rect(370, 250, 250, 100)
button_surface = pygame.Surface((150, 50))


button_rect_two = pygame.Rect(370, 250, 250, 100)
button_surface_two = pygame.Surface((300, 100))


platform = pygame.image.load("clover.png")
clover = pygame.transform.scale(platform, (900,700))


p = penguins(500,400)


c = Clover(100,130)

sf = Snowflake(180, 150)
#snowman
s = snowman(400,450)


font = pygame.font.SysFont('Arial', 40)
title_font = pygame.font.SysFont('Times New Roman', 60)
title = title_font.render('World of Wonders', True, (255, 255, 255))
start_button = font.render('Start', True, (155, 155, 155))


start_text = "Start"
start_message = font.render(start_text, True, (225, 225, 225))
start_message_rect = pygame.Rect(390, 200, start_message.get_width() + 8, start_message.get_height() - 5)

win = "You have won!"
ending = font.render(win, True, (225, 225, 225))


end_text = "End"
ending_message = font.render(end_text, True, (225, 255, 255))
end_message_rect = pygame.Rect(400, 400, ending_message.get_width() + 8, ending_message.get_height() - 5)


stime = time.time()
jumpheights = 26
gravity = 1
velocity = jumpheights
jumping = False
jump = False
run = True
starting_menu = True
starting_button = False
next_page = False
game_over = False
icecream_page = False
cloves = 0
score = 0
end = True

score_points = font.render("Score: " + str(score), True, (225, 225, 225))


while run == True:
    for events in pygame.event.get():
        if events.type == pygame.QUIT:
            pygame.quit()
            quit()
            # Check for the mouse button down event
        if events.type == pygame.MOUSEBUTTONDOWN and start_message_rect.collidepoint(events.pos):
            print("Start button clicked")
            score = 0
            run = True
            # starting_menu = False
        if events.type == pygame.MOUSEBUTTONDOWN and end_message_rect.collidepoint(events.pos):
            print("End button clicked")
            run = False
        if events.type == pygame.MOUSEBUTTONDOWN and (start_message_rect.collidepoint(events.pos) or end_message_rect.collidepoint(events.pos)):
            starting_menu = False

        if events.type == pygame.KEYDOWN:
            if events.key == pygame.K_SPACE:
                jump = True


        if jump and starting_menu == False:
            s.y -= velocity
            velocity -= gravity
            if velocity < -jumpheights:
                jump = False
                velocity = jumpheights
            s.move(s.x, s.y)
            screen.blit(s.image, s.rect)
        elif not(jump) and starting_menu == False:
            s.move(s.x, s.y)
            screen.blit(s.image, s.rect)


    if starting_menu == False:
        keys = pygame.key.get_pressed()  # checking pressed keys
        if keys[pygame.K_d]:
            s.move_direction("right", display_height, display_width)
        if keys[pygame.K_a]:
            s.move_direction("left", display_height, display_width)

    if s.rect.colliderect(sf.rect) and starting_menu == False:
        x_value = int(random.randint(0, display_width - p.image_size[0]))
        sf.move(x_value, sf.y)
        score += 3




    if s.rect.colliderect(p.rect) and starting_menu == False:
        x_value = int(random.randint(0, display_width - p.image_size[0]))
        p.move(x_value, p.y)
        score -= 25


    if s.rect.colliderect(c.rect) and starting_menu == False:
        message = "Collision detected"
        display_message = font.render(message, True, (255, 255, 255))
        x_value = int(random.randint(0, display_width - c.image_size[0]))
        c.move(x_value, c.y)
        cloves += 1
        score += 10

    else:
        message = "Collision not detected"
        display_message = font.render(message, True, (255, 255, 255))
    score_points = font.render("Score: " + str(score), True, (225, 225, 225))

    if score >= 100:
        end = True
        starting_menu = True
        run = False


    # Shwo the button text
    if starting_menu == True and run == True:
        screen.blit(title, (200,100))
        screen.blit(start_message, (390,200))
        start_message.get_rect().move(390, 200)
        pygame.draw.rect(screen, (255,255,255), start_message_rect, 2)


        screen.blit(ending_message, (400, 400))
        ending_message.get_rect().move(400, 400)
        pygame.draw.rect(screen, (255, 255, 255), end_message_rect, 2)


    if starting_menu == False and not(score >= 100):
        screen.blit(picture, (0,0))
        screen.blit(s.image, s.rect)
        screen.blit(p.image, p.rect)
        screen.blit(second_picture, (0,0))
        screen.blit(s.image, s.rect)
        screen.blit(c.image, c.rect)
        screen.blit(p.image, p.rect)
        screen.blit(sf.image, sf.rect)
        screen.blit(score_points, (650, 550))

    if score >= 100 and end == True:
        screen.blit(ending, (400,300))



    # Update the game state
    pygame.display.update()
