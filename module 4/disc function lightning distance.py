# Project:      DISC: Function - Lightning Distance
# Name:         Mark Kazzaz
# Goal:         User inputs number seconds of between seeing lightning strike and hearing thunder.
##              Program responses with how many miles away the lightning strike was.

def lightning(intSecondsPassed):

    # Input agrument to code is seconds passed

    # Calculate how many feet were traveled by thunder
    
    intFeetTraveled = intSecondsPassed * 1120  #1120 ft/sec = speed of sound

    # Convert feet traveled into miles

    fltMilesTraveled = intFeetTraveled / 5280 #5280 ft = 1 mile

    # print results
    print('You heard thunder'
          ,intSecondsPassed
          , 'seconds after you saw lightning.')
    print()
    print('This means the lightning strike was'
          ,'{:0.1f}'.format(fltMilesTraveled)
          ,'miles away.')
    print()
