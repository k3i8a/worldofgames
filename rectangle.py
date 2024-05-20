class rectangles:

    def __init__(self, x, y, width, height):
        # self.command = command
        # self.display = display
        # self.colour = colour
        self.x = int(x)
        self.y = int(y)
        self.width = int(width)
        self.height = int(height)

    def rect_draw(self):
        return self(self.x, self.y, self.width, self.height)

