from graphics import *
import random as r

win = GraphWin('random 4 pan eyeshadow palette', 400, 400)
win.setBackground('black')

def make_palette():

    colors = []
    circles = []

    for i in range(0,4):
        colors.append(color_rgb(random_rgb(), random_rgb(), random_rgb()))
        print(colors[i])

    high = 300 # higher offset on the coordinates
    low = 100 # lower offset on the coordinates

    make_pans(circles, high, high)
    make_pans(circles, high, low)
    make_pans(circles, low, high)
    make_pans(circles, low, low)

    for j in range(0,4):
        fill_pan(circles[j], colors[j])

    win.getKey()

def make_pans(circles, x_coor, y_coor):
    circles.append(Circle(Point(x_coor, y_coor), 80).draw(win))

def fill_pan(pan, color):
    pan.setFill(color)

def random_rgb():
    return r.randint(0,255)

make_palette()
