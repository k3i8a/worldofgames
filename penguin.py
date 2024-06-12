import pygame
import pygame.draw

class penguins:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.image = pygame.image.load("penguin.png")
        # self.rescale_image(self.image)
        self.image_size = self.image.get_size()
        self.rect = pygame.Rect(self.x, self.y, self.image_size[0], self.image_size[1])
        self.delta = .1
        self.velocity = 20
        self.jumping = False


    def move_direction(self, direction, display_height, display_width):
        key = pygame.key.get_pressed()
        if direction == "left" and key[pygame.K_a]:
            self.x = self.x - self.delta
        self.rect = pygame.Rect(self.x, self.y, self.image_size[0], self.image_size[1])
        if direction == "right" and key[pygame.K_d]:
            self.x = self.x + self.delta
        self.rect = pygame.Rect(self.x, self.y, self.image_size[0], self.image_size[1])
        if direction == "down" and key[pygame.K_s]:
            self.y = self.y - self.delta
        self.rect = pygame.Rect(self.x, self.y, self.image_size[0], self.image_size[1])
        if direction == "up" and key[pygame.K_w]:
            self.y = self.y + self.delta
        self.rect = pygame.Rect(self.x, self.y, self.image_size[0], self.image_size[1])