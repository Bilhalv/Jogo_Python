import pyglet

matriz = []

window = pyglet.window.Window(
    width=410,
    height=410,
)
for line in range(4):
        matriz.append([])
        for row in range(4):
            variacaox = line*100
            variacaoy = row*100
            matriz[line].append([10+variacaox, 10+variacaoy, 0, 0, 255])

@window.event
def on_draw():
    window.clear()
    for line in range(4):
        for row in range(4):
            pyglet.shapes.Rectangle(x=10+line*100, y=10+row*100, width=90, height=90, color=(matriz[line][row][2], matriz[line][row][3], matriz[line][row][4])).draw()
@window.event
def on_mouse_press(x, y, button, modifiers):
    for i in range(4):
        for j in range(4):
            if matriz[i][j][0] <= x and x <= matriz[i][j][0]+90 and matriz[i][j][1] <= y and y <= matriz[i][j][1]+90:
                update_matriz(i, j)

def update_matriz(i, j):
    if matriz[i][j][2] == 255:
        matriz[i][j][4] = 0
        matriz[i][j][3] = 255
        matriz[i][j][2] = 0
    else:
        matriz[i][j][4] = 0
        matriz[i][j][3] = 0
        matriz[i][j][2] = 255
        
pyglet.app.run()