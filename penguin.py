import pygame

class penguins:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.image = pygame.image.load("penguin.png")
        self.image_size = self.image.get_size()
        self.rect = pygame.Rect(self.x, self.y, self.image_size[0], self.image_size[1])
        self.delta = 3
        self.velocity = 0
        # self.gravity = 1
        # self.current_direction = "right"
        self.jumping = False

    def move_direction(self, direction, display_height, display_width):
        # speed = 3
        # cox = 0
        coy = 0
        gravity = 2
        key = pygame.key.get_pressed()
        if direction == "right" and key[pygame.K_a]:
            self.x = self.x + self.delta
        self.rect = pygame.Rect(self.x, self.y, self.image_size[0], self.image_size[1])
        if direction == "left" and key[pygame.K_d]:
            self.x = self.x - self.delta
        self.rect = pygame.Rect(self.x, self.y, self.image_size[0], self.image_size[1])
        if direction == "down" and key[pygame.s]:
            self.y = self.y + self.delta
        self.rect = pygame.Rect(self.x, self.y, self.image_size[0], self.image_size[1])
        if direction == "up" and key[pygame.K_w]:
            self.y = self.y - self.delta
        self.rect = pygame.Rect(self.x, self.y, self.image_size[0], self.image_size[1])
        self.velocity += gravity
        if direction == "jump" and key[pygame.K_SPACE]:
            self.jump = True
            self.velocity =- 30
        self.velocity += gravity
        coy += self.velocity

        if self.rect.bottom + coy > display_height:
            self.velocity = 0
            self.jumping = False
            coy = (display_width) - self.rect.bottom



