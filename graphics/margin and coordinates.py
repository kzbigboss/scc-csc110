from graphics import *

window_width = 400
window_height = 400
margin = 0.05

win = GraphWin('Kewl', window_width, window_height)
win.setCoords(0-margin, 0-margin, 2+margin, 2+margin)

margin = Rectangle(Point(0,0), Point(2, 2))
margin.draw(win)

Point(0.5,1.5).draw(win)
Point(1.5,1.5).draw(win)

Point(0.5,1.0).draw(win)
Point(1,1).draw(win)
Point(1.5, 1).draw(win)

Point(0.5,0.5).draw(win)
Point(1.5,0.5).draw(win)

##cir = Circle(Point(1,1),0.05)
##cir.setFill('red')
##cir.draw(win)

lstMarkerLocations = [
    [0.5,1.5]
    ,[1.5,1.5]
    ,[0.5,1.0]
    ,[1.0,1.0]
    ,[0.5,0.5]
    ,[1.5,0.5]
    ,[1.5,1.0]
    ]

for i in range(len(lstMarkerLocations)):
    print(type(i), i)
    cir = Circle(Point(lstMarkerLocations[i][0], lstMarkerLocations[i][1]), 0.15)
    cir.setFill('green')
    cir.draw(win)
