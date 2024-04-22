import pyglet


class Button:
    def __init__(self, x, y, text, batch, function, width=200, height=50, color=(0, 255, 0, 255), label_color=(255, 255, 255, 255)):
        label_size = height//3
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        self.text = text
        self.batch = batch
        self.label = pyglet.text.Label(
            text,
            x=x - width//2,
            y=y,
            batch=batch,
            align="center",
            width=width,
            height=label_size * 5,
            anchor_y="center",
            font_size=label_size,
            color=label_color
        )
        self.bg = pyglet.shapes.Rectangle(
            x - width//2,
            y,
            width,
            height,
            color=color,
            batch=batch
        )
        self.function = function

    def check_click(self, x, y):
        if x > self.x and x < self.x + self.width:
            if y > self.y and y < self.y + self.height:
                return True
        return False
    
    def perform_action(self):
        self.function()