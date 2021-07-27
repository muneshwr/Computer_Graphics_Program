from graphics import *
import time

def bramhasn(x1, y1, x2, y2):
    

    # creating the window
    winX = 600
    winY = 600
    win = GraphWin('Brasenham Line', winX, winY)

    # measure the distance
    dx = abs(x2 - x1)
    dy = abs(y2 - y1)

    # prepare the p attrib
    p = 2 * dy - dx
    duady = 2 * dy
    duadydx = 2 * (dy - dx)

    # check the start & end point
    if(x1 > x2):
        x, y = x2, y2
        xend = x1
    else:
        x, y = x1, y1
        xend = x2

    # loop for making the line based on point
    PutPixle(win, x, y)
    while(x < xend):
        x = x + 1
        if(p < 0):
            p = p + duady
        else:
            y = y - 1 if y1 > y2 else y + 1
            p = p + duadydx

        time.sleep(0.01)
        print(x,y)
        PutPixle(win, x, y)

    win.getMouse()

    win.close()
def PutPixle(win, x, y):
    """ Plot A Pixle In The Windows At Point (x, y) """
    pt = Point(x, y)
    pt.draw(win)


def main():
    x1 = int(input("Enter Start X: "))
    y1 = int(input("Enter Start Y: "))
    x2 = int(input("Enter End X: "))
    y2 = int(input("Enter End Y: "))

    bramhasn(x1, y1, x2, y2)


if __name__ == "__main__":
    main()
