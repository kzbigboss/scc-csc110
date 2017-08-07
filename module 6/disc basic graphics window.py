# Project:      DISC: basic graphics window
# Name:         Mark Kazzaz
# Goal:         Recreate the graphic show in the header of this dicussion

## load required libraries
from graphics import *

def main():
    win = GraphWin('Shapes', 400, 400)
    win.setCoords(0,500,500,0) # redoing the coordinates since
                               # the sample image is about 500x500

    # draw black rectangle
    rctTallBlack = Rectangle(Point(100, 75), Point(200, 425))
    rctTallBlack.setFill('black')
    rctTallBlack.setOutline('black')
    rctTallBlack.draw(win)
    
    # top title
    txtTop = Text(Point(150, 65), 'Top')
    txtTop.setTextColor('green')
    txtTop.draw(win)

    # bottom title
    txtBottom = Text(Point(150, 435), 'Bottom')
    txtBottom.setTextColor('green')
    txtBottom.draw(win)

    # purple rectangle
    rctPurple = Rectangle(Point(250, 250), Point(330, 290))
    rctPurple.setFill('purple')
    rctPurple.setOutline('black')
    rctPurple.draw(win)

    # orange rectangle
    rctOrange = Rectangle(Point(290, 210), Point(370, 250))
    rctOrange.setFill('orange')
    rctOrange.setOutline('black')
    rctOrange.draw(win)

    # blue rectangle
    rctBlue = Rectangle(Point(330, 170), Point(410, 210))
    rctBlue.setFill('blue')
    rctBlue.setOutline('black')
    rctBlue.draw(win)

    # red circle
    cirRed = Circle(Point(300, 400), 50)
    cirRed.setFill('red')
    cirRed.setOutline('black')
    cirRed.draw(win)

    # yellow circle
    cirRed = Circle(Point(300+50, 400), 50)
    cirRed.setFill('yellow')
    cirRed.setOutline('black')
    cirRed.draw(win)
    
main()
