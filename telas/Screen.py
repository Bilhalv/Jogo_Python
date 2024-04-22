import pyglet

class Screen:
    def __init__(self, title):
        self.title = title
        self.window = pyglet.window.Window(caption=self.title)
        # self.window.set_fullscreen(True)

    def start(self):
        self.clear()
        self.clear_listeners()
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
    
    def change_caption(self, caption):
        self.window.set_caption(caption)
    
    def change(self, new):
        try:
            self.window.close()
            pyglet.app.exit()
        except BaseException as error:
            print(error)
        finally:
            new.start()

