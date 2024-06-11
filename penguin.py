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
        cox = 0
        coy = 0
        gravity = 2
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

        if direction == "jump" and key[pygame.K_SPACE]:
            self.jumping = True
            self.velocity = -30
            self.velocity += gravity
            coy += self.velocity

        if self.rect.left + cox < 0:
            cox = -self.rect.left
        elif self.rect.right + cox > display_width:
            cox = display_width - self.rect.right

        if self.rect.bottom + coy > display_height:
            self.velocity = 0
            self.jumping = False
            coy = (display_width) - self.rect.bottom

        self.rect.x += cox
        self.rect.y += coy







