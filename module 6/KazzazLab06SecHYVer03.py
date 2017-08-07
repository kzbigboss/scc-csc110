# Project:      Lab 6 (KazzazLab06SecHYVer03.py)
# Name:         Mark Kazzaz
# Date:         2017-08-05
# Description:  This program leverages functions to draw dice within a window


## load required libraries
from graphics import *


## define function to draw dice makers to indicate face value
def drawMark(window, intSize, pntMark):
    ## draw mark location on window within dice rectangle
    cirMark = Circle(pntMark, intSize*0.1)
    cirMark.setFill('green')
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


## define main function to establish window and draw dice
def main():
    ## define window for GUI
    window_width = 400
    window_height = 400
    win = GraphWin('Lab6', window_width, window_height)
    win.setBackground('grey')

    ## leverage the drawDice function to draw dice in the window based
    ## on entering the the top left corner of the die, the size of the die,
    ## and the face value of the dice
    #rctDice01 = drawDice(win, Point(50, 50), 50, 1)
    #rctDice02 = drawDice(win, Point(100, 100), 50, 2)
    #rctDice03 = drawDice(win, Point(150, 150), 50, 3)
    #rctDice04 = drawDice(win, Point(200, 200), 50, 4)
    rctDice05 = drawDice(win, Point(100, 100), 225, 5)
    #rctDice06 = drawDice(win, Point(300, 300), 50, 6)

main()
