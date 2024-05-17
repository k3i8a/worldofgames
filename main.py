import pygame
import random

# from rectangle import rectangles


display_width = 900
display_height = 700
screen = pygame.display.set_mode((display_width, display_height))


pygame.init()
pygame.font.init()


stop = False
button_rect = pygame.Rect(370, 250, 250, 100)
button_surface = pygame.Surface((150, 50))

button_rect_two = pygame.Rect(370, 250, 240, 100)
button_surface_two = pygame.Surface((300, 100))


font = pygame.font.SysFont('Arial', 40)
title_font = pygame.font.SysFont('Times New Roman', 60)
title = title_font.render('World of Wonders', True, (255, 255, 255))
start_button = font.render('Start', True, (155, 155, 155))

start_text = "Start"
start_message = font.render(start_text, True, (225, 225, 225))
# start_text_rect = start_text.get_rect(center=(button_surface.get_width()/2, button_surface.get_height()/2))

end_text = "End"
ending_message = font.render(end_text, True, (225, 255, 255))
# end_text_rect = end_text.get_rect(center=((button_surface.get_width()/2 - 100), (button_surface.get_height()/2) - 100))


game_start = "start_menu"
while True:
    for events in pygame.event.get():
        if events.type == pygame.QUIT:
            pygame.quit()
            quit()
            # Check for the mouse button down event
            if events.type == pygame.MOUSEBUTTONDOWN and events.button == 1:
                # Call the on_mouse_button_down() function
                if button_rect.collidepoint(events.pos):
                    print("Button clicked!")

        # Check if the mouse is over the button. This will create the button hover effect
        if button_rect.collidepoint(pygame.mouse.get_pos()):
            pygame.draw.rect(button_surface, (127, 255, 212), (1, 1, 148, 48))
            pygame.draw.rect(button_surface_two, (127, 255, 212), (3, 3, 248, 148))
        else:
            pygame.draw.rect(button_surface, (0, 0, 0), (0, 0, 150, 50))
            pygame.draw.rect(button_surface, (255, 255, 255), (1, 1, 148, 48))
            pygame.draw.rect(button_surface, (0, 0, 0), (1, 1, 148, 1), 2)
            pygame.draw.rect(button_surface, (0, 100, 0), (1, 48, 148, 10), 2)
            pygame.draw.rect(button_surface_two, (0, 0, 0), (0, 0, 350, 200))
            pygame.draw.rect(button_surface_two, (255, 255, 255), (3, 3, 248, 148))
            pygame.draw.rect(button_surface_two, (0, 0, 0), (3, 3, 248, 3), 3)
            pygame.draw.rect(button_surface_two, (0, 100, 0), (3, 148, 248, 30), 4)




 # Shwo the button text
    screen.blit(start_message, (button_surface.get_width()/2, button_surface.get_height()/2))
    # screen.blit(ending_message, (button_surface_two.get_width()/2), (button_surface_two.get_height()/2))

 # Draw the button on the screen
 #    screen.blit(button_surface, (button_rect.x, button_rect.y))
 #    screen.blit(button_surface_two, (button_rect_two.x, button_rect.y))

 # Update the game state
    pygame.display.update()






