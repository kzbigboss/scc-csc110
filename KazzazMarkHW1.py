# Project:      HW:1
# Name:         Mark Kazzaz
# Date:         2017-07-05
# Description:  (a) program that calculates MPH
#               (b) program that takes two numbers and multiplies them by six

## Collect miles and minute from user, calculate MPH
def mainA():
    print('Bicycle MPH Calculator...')
    flt_miles = float(input('Input the number of miles you traveled: '))
    flt_minutes = float(input('Input number of minutes you road for: '))

    flt_hours = flt_minutes / 60 # converting minute input into hours
    flt_mph = flt_miles / flt_hours
    print('You averaged',flt_mph, 'MPH')

## Collect two numbers, print both numbers multipled by six

def mainB():
    flt_firstnumber = float(input('Enter first number: '))
    flt_secondnumber = float(input('Enter second number: '))
    print('Your numbers multipled by six are...')
    print(flt_firstnumber*6, flt_secondnumber*6)

# Execute program
mainA()
mainB()
