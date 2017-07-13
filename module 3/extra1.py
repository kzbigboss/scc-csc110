def main():

    print('Welcome to the trianger printer!'
          ,'Please enter in whole numbers the base of your triangle.')

    strTriangleBaseInput = input('Triangle base: ')

    ## check if user entered a number
    try:
        intTriangleBase = int(strTriangleBaseInput)
    except:
        print('Invalid input detected.  Try again')

    intLoopCount = 1
    strTriangleCharacter = 'X'

    for i in range(intTriangleBase):
        print(strTriangleCharacter * intLoopCount)
        intLoopCount += 1

main()
