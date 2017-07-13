# Project:      EXTR: 1 - Triangle (KazzazMarkEXTR01SecHYVer01.py)
# Name:         Mark Kazzaz
# Date:         2017-07-12
# Description:  This program will draw a triangle based on user input of height

def main():

    # greet user, share input requirement
    print('Welcome to the trianger printer!'
          ,'Please enter in whole numbers the height of your desired triangle.'
          ,sep = '\n'
          )

    # if invalid input is detected, loop until valid input is accepted
    isValidInput = False
    while isValidInput == False:
        try:
            ### obtain input from user
            strTriangleHeightInput = str(input('Triangle height: '))
            ### convert input to integer
            intTriangleHeight = int(strTriangleHeightInput)
            ### record valid input and move on
            isValidInput = True
        except:
            ### an invalid input was found.  ask user to try again.
            print('Invalid input detected.  Try again.')

    # prepare variable to help with printing triangle
    strTriangleCharacter = 'X'
    intLoopCount = 0

    # loop through printing until loop interation exceeds user input
    while (intLoopCount < intTriangleHeight):
        intLoopCount = intLoopCount + 1
        print(strTriangleCharacter * intLoopCount)

main()
