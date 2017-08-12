# Project:      HW4 (KazzazMarkHW4SecHYVer01.py)
# Name:         Mark Kazzaz
# Date:         2017-08-12
# Description:  This program will interept clicks in a GUI from a user to
##              draw a collection of dice, present the total face value,
##              then create a button that will quit the application.

## load required libraries
from graphics import *      ## GUI/drawing
from random import randint  ## Random integer function

## define function to roll a dice and aggregate results
def rollDice(window, rctDice, intSize):    

    ## randomy determine dice face
    intFaceValue = randint(1,6)
    
    ## draw dice
    drawDice(window, rctDice.getP1(), intSize, intFaceValue)

    ## return face value
    return(intFaceValue)
    
## define function to draw dice makers to indicate face value
def drawMark(window, intSize, pntMark):
    ## draw mark location on window within dice rectangle
    cirMark = Circle(pntMark, intSize*0.1)
    cirMark.setFill('green')
    cirMark.setOutline('green')
    cirMark.draw(window)

## define function to draw dice within a window
def drawDice(window, pntTopLeft, intSize, intFaceValue):
    ## figure out corresponding bottom right corner based on
    ## top left corner input
    pntBottomRight = Point(pntTopLeft.getX()+intSize
                           ,pntTopLeft.getY()+intSize
                           )

    ## define and draw rectangle shape based on top corner & bottom corner
    ## into window input
    rctDice = Rectangle(pntTopLeft, pntBottomRight)
    rctDice.setFill('white')
    rctDice.setOutline('black')
    rctDice.draw(window)

    ## define offsets and partitions for dice face marker locations
    fltXOffset          = pntTopLeft.getX()
    fltYOffset          = pntTopLeft.getY()
    fltNearPartition    = 0.2
    fltMidPartition     = 0.5
    fltFarPartition     = 1.0 - fltNearPartition ## make it an inverse of the near partition

    ## calculate the relative location of the dice marker locations
    ## based on the window placement and width of the dice

    lstMarkerLocations = [  # list of a list containing dice marker locations
        ### map of all maker points on a dice face:
            ### |NP | MP | FP|  = Near Partition, Middle Partition, Far Partition
            ### --------------
            ### | p0  p1  p2 |
            ### |            |
            ### | p3  p4  p5 |
            ### |            |
            ### | p6  p7  p8 |
            ### --------------
        
        ## first row
         [fltNearPartition*intSize+fltXOffset, fltNearPartition*intSize+fltYOffset] #p0
        ,[fltMidPartition*intSize+fltXOffset, fltNearPartition*intSize+fltYOffset]  #p1
        ,[fltFarPartition*intSize+fltXOffset, fltNearPartition*intSize+fltYOffset]  #p2
        ## second row
        ,[fltNearPartition*intSize+fltXOffset, fltMidPartition*intSize+fltYOffset]  #p3
        ,[fltMidPartition*intSize+fltXOffset, fltMidPartition*intSize+fltYOffset]   #p4
        ,[fltFarPartition*intSize+fltXOffset, fltMidPartition*intSize+fltYOffset]   #p5
        ## third row
        ,[fltNearPartition*intSize+fltXOffset, fltFarPartition*intSize+fltYOffset]  #p6
        ,[fltMidPartition*intSize+fltXOffset, fltFarPartition*intSize+fltYOffset]   #p7
        ,[fltFarPartition*intSize+fltXOffset, fltFarPartition*intSize+fltYOffset]   #p8
         ]

    ## evaluate the face value requested and determine
    ## the allowable markers to draw
    if intFaceValue == 1:
        lstMarkIndex = [4]
    elif intFaceValue == 2:
        lstMarkIndex = [0,8]
    elif intFaceValue == 3:
        lstMarkIndex = [0,4,8]
    elif intFaceValue == 4:
        lstMarkIndex = [0,2,6,8]
    elif intFaceValue == 5:
        lstMarkIndex = [0,2,4,6,8]
    elif intFaceValue == 6:
        lstMarkIndex = [0,2,3,5,6,8]

    ## subset the marker location listing to just those necesssary to
    ## create the requested face value
    lstMarkerLocations = [lstMarkerLocations[i] for i in lstMarkIndex]

    ## leverage the diceMark function to draw dice markers based
    ## on the requested face value
    for i in range(len(lstMarkerLocations)):
        drawMark(window, intSize, Point(lstMarkerLocations[i][0],lstMarkerLocations[i][1]))

    ## return the rectangle constructor that was created
    return(rctDice)

## define function to draw empty dice shapes for the user to interact with
def drawBlankDice(window, pntTopLeft, intSize):
    ## figure out corresponding bottom right corner based on
    ## top left corner input
    pntBottomRight = Point(pntTopLeft.getX()+intSize
                           ,pntTopLeft.getY()+intSize
                           )

    ## define and draw rectangle shape based on top corner & bottom corner
    ## into window input
    rctDice = Rectangle(pntTopLeft, pntBottomRight)
    rctDice.setFill('black')
    rctDice.setOutline('white')
    rctDice.draw(window)
    return(rctDice)

## define function to help determine if a a mouse click occured within a rectangle shape
def checkWithinRectangle(point, rectangle):
    pntTopLeft = rectangle.getP1()
    pntBottomRight = rectangle.getP2()
    isWithinX = pntTopLeft.getX() < point.getX() < pntBottomRight.getX()
    isWithinY = pntTopLeft.getY() < point.getY() < pntBottomRight.getY()
    isWithin = isWithinX and isWithinY
    return(isWithin)

def main():
    ## define variables
    intDiceRollsRemaining = 5
    intDiceRollTotal = 0
    strUserPrompt = 'Please click on the {} blank dice.'
    #### establish False values for all/any dice roll
    isAllDiceRolled = False
    isDice01Rolled = False
    isDice02Rolled = False
    isDice03Rolled = False
    isDice04Rolled = False
    isDice05Rolled = False
    #### dice attributes
    intDiceSize = 140
    #### exit button control variable
    isExitPressed = False
    
    ## define window for GUI
    window_width = 800
    window_height = 400
    win = GraphWin('Homework 4 - Dice Game', window_width, window_height)
    win.setBackground('light grey')

    txtPrompt = Text(Point(window_width*.5, window_height*.05), strUserPrompt.format(str(intDiceRollsRemaining)))
    txtPrompt.draw(win)

    ## draw unrolled dice
    # blank dice 1
    rctDice01 = drawBlankDice(win, Point(35,125), intDiceSize)

    # blank dice 2
    rctDice02 = rctDice01.clone()
    rctDice02.move(150,0)
    rctDice02.draw(win)

    # blank dice 3
    rctDice03 = rctDice02.clone()
    rctDice03.move(150,0)
    rctDice03.draw(win)

    # blank dice 4
    rctDice04 = rctDice03.clone()
    rctDice04.move(150,0)
    rctDice04.draw(win)

    # blank dice 5
    rctDice05 = rctDice04.clone()
    rctDice05.move(150,0)
    rctDice05.draw(win)

    while isAllDiceRolled == False:
        # get user's click
        clkUser = win.getMouse()

        # did user click within dice 1?
        if checkWithinRectangle(clkUser, rctDice01):
            ## has this dice already been rolled?
            if isDice01Rolled == False:
                isDice01Rolled = True
                intDiceRollsRemaining -= 1
                txtPrompt.setText(strUserPrompt.format(str(intDiceRollsRemaining)))
                intDiceRollTotal += rollDice(win, rctDice01, intDiceSize)
                
                if intDiceRollsRemaining == 0:
                    isAllDiceRolled = True
            
        # did user click within dice 2?
        elif checkWithinRectangle(clkUser, rctDice02):
            if isDice02Rolled == False:
                isDice02Rolled = True
                intDiceRollsRemaining -= 1
                txtPrompt.setText(strUserPrompt.format(str(intDiceRollsRemaining)))
                intDiceRollTotal += rollDice(win, rctDice02, intDiceSize)
                
                if intDiceRollsRemaining == 0:
                    isAllDiceRolled = True

        # did user click within dice 3?
        elif checkWithinRectangle(clkUser, rctDice03):
            if isDice03Rolled == False:
                isDice03Rolled = True
                intDiceRollsRemaining -= 1
                txtPrompt.setText(strUserPrompt.format(str(intDiceRollsRemaining)))
                intDiceRollTotal += rollDice(win, rctDice03, intDiceSize)
                
                if intDiceRollsRemaining == 0:
                    isAllDiceRolled = True

        # did user click within dice 4?
        elif checkWithinRectangle(clkUser, rctDice04):
            if isDice04Rolled == False:
                isDice04Rolled = True
                intDiceRollsRemaining -= 1
                txtPrompt.setText(strUserPrompt.format(str(intDiceRollsRemaining)))
                intDiceRollTotal += rollDice(win, rctDice04, intDiceSize)
                
                if intDiceRollsRemaining == 0:
                    isAllDiceRolled = True

        # did user click within dice 5?
        elif checkWithinRectangle(clkUser, rctDice05):
            if isDice05Rolled == False:
                isDice05Rolled = True
                intDiceRollsRemaining -= 1
                txtPrompt.setText(strUserPrompt.format(str(intDiceRollsRemaining)))
                intDiceRollTotal += rollDice(win, rctDice05, intDiceSize)
                
                if intDiceRollsRemaining == 0:
                    isAllDiceRolled = True

        # did the user click outside of a dice? set default prompt
        else:
            txtPrompt.setText(strUserPrompt.format(str(intDiceRollsRemaining)))

    # exited the isAllDiceRolled loop, update prompt 
    txtPrompt.setText('All dice have been rolled. Congrats! You rolled {}. \n Press Exit to close.'.format(str(intDiceRollTotal)))

    # draw exit button
    btnExitShape = Rectangle(Point(window_width-100,window_height-50), Point(window_width-10, window_height-10))
    btnExitShape.setFill('black')
    btnExitShape.draw(win)

    btnExitText = Text(btnExitShape.getCenter(), 'Exit')
    btnExitText.setStyle('bold')
    btnExitText.setTextColor('white')
    btnExitText.draw(win)

    # exit application via exit button

    while isExitPressed == False:
        # get user's click
        clkUser = win.getMouse()

        # did user click the exit button?
        if checkWithinRectangle(clkUser, btnExitShape):
            win.close()
            isExitPressed = True
    
main()
