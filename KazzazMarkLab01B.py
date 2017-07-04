# Project:      Lab:1
# Name:         Mark Kazzaz
# Date:         2017-07-05
# Description:  Lab 1B: Program that uses loops to print numbers

## Print out the numbers 0 through 9
def mainA():
    print('Printing numbers 0 through 9...')
    for i in range(0,10):
        print(i)
    print('')

## Print out the numbers 1 through 10
def mainB():
    print('Printing numbers 1 through 10...')
    for i in range(0,10):
        print(i+1)

## Print out two columns: [0-9], [0-9]+1
def mainC():
    print('Printing numers 1-9 and 10-19 in separate columns:')
    for i in range(0,10):
        print(i, i+1)

## Execute program
mainA()
mainB()
mainC()
