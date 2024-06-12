import time
import random
import pygame
from snowaman import snowman
from clover import Clover
from penguin import penguins

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

p = penguins(500,500)
p_rect = pygame.Rect(370, 250, 200, 100)

c = Clover(100,100)
c_rect = pygame.Rect(370, 200, 200, 100)
STANDING_SURFACE_PENGUIN = pygame.transform.scale(pygame.image.load("penguin.png"), (200,400))
JUMPING_SURFACE_PENGUIN = pygame.transform.scale(pygame.image.load("penguin.png"), (200,400))
penguin_page = False

#snowman
s = snowman(400,200)
s_rect = pygame.Rect(370, 250, 250, 100)



font = pygame.font.SysFont('Arial', 40)
title_font = pygame.font.SysFont('Times New Roman', 60)
title = title_font.render('World of Wonders', True, (255, 255, 255))
start_button = font.render('Start', True, (155, 155, 155))

start_text = "Start"
start_message = font.render(start_text, True, (225, 225, 225))
start_message_rect = pygame.Rect(390, 200, start_message.get_width() + 8, start_message.get_height() - 5)
lose = "You didn't win. Try again!"
loser = font.render(lose, True, (225, 225, 225))
win = "You have won!"
ending = font.render(win, True, (225, 225, 225))



end_text = "End"
ending_message = font.render(end_text, True, (225, 255, 255))
end_message_rect = pygame.Rect(400, 400, ending_message.get_width() + 8, ending_message.get_height() - 5)

stime = time.time()
jumpheights = 20
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
value = 0

score_points = font.render("Score: " + str(value), True, (225, 225, 225))

while run == True and game_over == False:
    current_time = time.time()
    if not game_over:
        keys = pygame.key.get_pressed()  # checking pressed keys
        if keys[pygame.K_d]:
            s.move_direction("right", display_height, display_width)
        if keys[pygame.K_s]:
            s.move_direction("down", display_height, display_width)
        if keys[pygame.K_w]:
            s.move_direction("up", display_height, display_width)
        if keys[pygame.K_a]:
            s.move_direction("left", display_height, display_width)
        if keys[pygame.K_SPACE]:
            s.move_direction("jump", display_height, display_width)
        timer = current_time - stime
    if not game_over:
        times = 10 - timer
    start_time = font.render("Total time: " + str(round(times)) + " s", True, (225,225,225))
    for events in pygame.event.get():
        if events.type == pygame.QUIT:
            pygame.quit()
            quit()
            # Check for the mouse button down event
        if events.type == pygame.MOUSEBUTTONDOWN and start_message_rect.collidepoint(events.pos):
            print("Start button clicked")
            run = True
            # starting_menu = False
        if events.type == pygame.MOUSEBUTTONDOWN and end_message_rect.collidepoint(events.pos):
            print("End button clicked")
            run = False
        if events.type == pygame.MOUSEBUTTONDOWN and (start_message_rect.collidepoint(events.pos) or end_message_rect.collidepoint(events.pos)):
            starting_menu = False
    if starting_menu == True:
        keys = pygame.key.get_pressed()  # checking pressed keys
        if keys[pygame.K_d]:
            s.move_direction("right", display_height, display_width)
        if keys[pygame.K_a]:
            s.move_direction("left", display_height, display_width)

        if events.type == pygame.KEYDOWN:
            if events.key == pygame.K_SPACE:
                jump = True

        if jump:
            s.y -= velocity
            velocity -= gravity
            if velocity < -jumpheights:
                jump = False
                velocity = jumpheights
            s.move(s.x, s.y)
            screen.blit(s.image, s.rect)
        else:
            s.move(s.x, s.y)
            screen.blit(s.image, s.rect)

    # if s.rect.colliderect(p.rect):
    #     if starting_menu == False:
    #         p.move_direction(p.x, p.y)
    #         value -= 10
    #         cloves += 1
    #         x_value = int(random.randint(0, 450))
    #         y_value = int(random.randint(0, 350))
    #         c.set_location(x_value, y_value)
    #         print(value)
    #         print(cloves)
    # if  s.rect.colliderect(c_rect):
    #     if starting_menu == False:
    #         message = "Collision detected"
    #         display_message = font.render(message, True, (255, 255, 255))
    #         x_value = int(random.randint(0, 450))
    #         y_value = int(random.randint(0, 350))
    #         c.set_location(x_value, y_value)
    #         cloves += 1
    #         value += 10
    #     if value >= 100 and times >= 0:
    #         game_over = True
    #         run = False
    #         win = "You have won!"
    #         ending = font.render(win, True, (225, 225, 225))
    #     if value != 100 and times <= 0:
    #         game_over = True
    #         run = False
    #         lose = "You didn't win. Try again!"
    #         loser = font.render(lose, True, (225, 225, 225))
    #     else:
    #         message = "Collision not detected"
    #         display_message = font.render(message, True, (255, 255, 255))
    #     score_points = font.render("Score: " + str(value), True, (225, 225, 225))
    #

    # Shwo the button text
    if starting_menu == True and run == True:
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
        screen.blit(p.image, p.rect)
        screen.blit(second_picture, (0,0))
        screen.blit(s.image, s.rect)
        screen.blit(c.image, c.rect)
        screen.blit(p.image, p.rect)
        screen.blit(score_points, (450, 350))
    if value >= 100 and times >= 0 and game_over == True and starting_menu == False:
        screen.blit(ending,(25,150))
    if value != 100 and times <= 0 and game_over == True and starting_menu == False:
        screen.blit(loser, (25,150))





 # Update the game state
    pygame.display.update()
    clock.tick(60)
