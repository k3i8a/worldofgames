import pygame

class penguins:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.image = pygame.image.load("penguin.png")
        self.image_size = self.image.get_size()
        self.rect = pygame.Rect(self.x, self.y, self.image_size[0], self.image_size[1])
        self.data = .1
        self.current_direction = "right"


    def move_direction(self, direction):
        if self.current_direction == "right" and direction == "left":
            self.image = pygame.transform.flip(self.image, True, False)
        if self.current_direction == "left" and direction == "right":
            if self.image == "right":
                self.current_direction == "right"
                self.x = self.x + self.delta
            self.rect = pygame.Rect(self.x, self.y, self.image_size[0], self.image_size[1])