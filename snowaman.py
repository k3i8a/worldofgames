import pygame
import pygame.draw

class snowman:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.image = pygame.image.load("snowman.png")
        self.image_size = self.image.get_size()
        self.delta = 5
        self.velocity = 0
        self.rect = pygame.Rect((x, y, 200, 100))
        self.jumping = False

    def move_direction(self, direction, display_height, display_width):
        key = pygame.key.get_pressed()
        if direction == "left" and key[pygame.K_a]:
            self.x = self.x - self.delta
        self.rect = pygame.Rect(self.x, self.y, self.image_size[0], self.image_size[1])
        if direction == "right" and key[pygame.K_d]:
            self.x = self.x + self.delta
        self.rect = pygame.Rect(self.x, self.y, self.image_size[0], self.image_size[1])

    def move(self, new_x, new_y):
        self.x = new_x
        self.y = new_y
        self.rect = pygame.Rect(self.x, self.y, self.image_size[0], self.image_size[1])
