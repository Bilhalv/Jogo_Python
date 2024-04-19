import pyglet

class Screen:
    def __init__(self, title):
        self.title = title
        self.window = pyglet.window.Window(caption=self.title)
        self.window.set_fullscreen(True)

    def start(self):
        pyglet.app.run()
    
    def draw(self, batch):
        batch.draw()

    def clear(self):
        self.window.clear()
    
    def add_listener(self, listener):
        self.window.push_handlers(listener)
    
    def remove_listener(self, listener):
        self.window.remove_handlers(listener)
    
    def clear_listeners(self):
        self.window.remove_handlers()