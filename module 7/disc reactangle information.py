# Program:  DISC: Rectangle Information
# Name:     Mark Kazzaz
# Goal:     This program prompts the user to draw a rectangle
##          then calculates the rectangles area and perimeter.

from graphics import *

def main():

    # Create the window
    win = GraphWin("Rectangle Information", 500, 500)

    # Draw message
    txtMessage = Text(Point(250,10), "Click on two opposite points to draw a rectangle")
    txtMessage.draw(win)

    # Capture user mouse clicks
    pntClick1 = win.getMouse()
    pntClick1.draw(win)
    pntClick2 = win.getMouse()
    pntClick2.draw(win)

    # Draw rectangle via user inputs
    shpRectangle = Rectangle(pntClick1, pntClick2)
    shpRectangle.draw(win)
    shpRectangle.setFill('blue')
    shpRectangle.setOutline('blue')

    # Clear unnecessary drawings
    pntClick1.undraw()
    pntClick2.undraw()
    txtMessage.undraw()

    # Calculate area and perimeter
    intLength = abs(pntClick2.getY() - pntClick1.getY())
    intWidth = abs(pntClick2.getX() - pntClick1.getX())

    intArea = (intLength * intWidth)
    intPerimeter = (2 * intLength) + (2 * intWidth)

    txtResult = Text(Point(250, 450), 'Your rectangle has an area of {} and a permeter of {}.'.format(
        str(intArea)
        ,str(intPerimeter)))
    txtResult.draw(win)
    
    # Wait for another click to exit
    txtExit = Text(Point(250, 475), 'Click anywhere to quit.')
    txtExit.draw(win)
    win.getMouse()
    win.close()
        
main()





