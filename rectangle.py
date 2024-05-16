class rectangles:

    def __init__(self, x, y, width, height):
        # self.command = command
        # self.display = display
        # self.colour = colour
        self.x = int(x)
        self.y = int(y)
        self.width = int(width)
        self.height = int(height)

    def rectdraw(self):
        return self(self.x, self.y, self.width, self.height)


button_rect_one = rectangles(100, 100, 200, 200)
button_rect_two = rectangles(370, 350, 350, 2000)

