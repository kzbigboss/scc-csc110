from graphics import *

def drawDice(PointZero, intSize, intFaceValue):
    window_width = intSize
    window_height = window_width
    win = GraphWin('Dice', window_width, window_height)
    
    ## evaluate if we received a valid dice face value
    ## proceed if we did, exit if we didn't
    if 1 <= intFaceValue <= 6:
        ## setup basic drawing offsets and partitions
        fltXOffset = PointZero.getX()
        fltYOffset = PointZero.getY()
        fltNearPartition    = 0.2
        fltMidPartition     = 0.5
        fltFarPartition     = 0.8

        ## define the areas where dice markers belong
        ## relative to offsets and partitions
        lstMarkerLocations = [     # list of a list containing marker locations
             ## first row
              [fltNearPartition*intSize+fltXOffset, fltNearPartition*intSize+fltYOffset]  #p0
             ,[fltMidPartition*intSize+fltXOffset, fltNearPartition*intSize+fltYOffset]   #p1
             ,[fltFarPartition*intSize+fltXOffset, fltNearPartition*intSize+fltYOffset]   #p2
             ## second row
             ,[fltNearPartition*intSize+fltXOffset, fltMidPartition*intSize+fltYOffset]   #p3
             ,[fltMidPartition*intSize+fltXOffset, fltMidPartition*intSize+fltYOffset]    #p4
             ,[fltFarPartition*intSize+fltXOffset, fltMidPartition*intSize+fltYOffset]    #p5
             ## third row
             ,[fltNearPartition*intSize+fltXOffset, fltFarPartition*intSize+fltYOffset]   #p6
             ,[fltMidPartition*intSize+fltXOffset, fltFarPartition*intSize+fltYOffset]    #p7
             ,[fltFarPartition*intSize+fltXOffset, fltFarPartition*intSize+fltYOffset]    #p8
              ]

        ## evaluate the face value requested and determine
        ## allowable markers to draw
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
        
        ## loop through the list of marker locations only drawing
        ## if the mark has been identified via the face value input
        for i in range(len(lstMarkerLocations)):
            if i in lstMarkIndex:
                cir = Circle(Point(lstMarkerLocations[i][0], lstMarkerLocations[i][1]), intSize*0.1)
                cir.setFill('green')
                cir.draw(win)
    else:
        return('Dice value must be between 1 and 6.')

drawDice(Point(0,0), 400, 1)
drawDice(Point(0,0), 400, 2)
drawDice(Point(0,0), 400, 3)
drawDice(Point(0,0), 400, 4)
drawDice(Point(0,0), 400, 5)
drawDice(Point(0,0), 400, 6)
