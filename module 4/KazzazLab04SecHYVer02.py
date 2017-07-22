# Project:      Lab 4 (KazzazLab04SecHYVer02.py)
# Name:         Mark Kazzaz
# Date:         2017-07-22
# Description:  This program will
##                  A: calculate user's numeric value of their name
##                  B: calculate lines, words, and characters within a file

## Calculate a user's numeric value of their name
def mainA():
    ### Prompt for user name
    print('Let\'s figure out the numerical value of your first name.')
    strUserFirstName = str(input('Enter your first name: '))

    ### Initialize a running total variable to capture numerical results
    intNameValueRunningTotal = 0

    ### Loop through the length of the user name
    for i in range(len(strUserFirstName)):

        ### For each iteration, find the Unicode value of the lower case
        ### letter and subtract 96 so that 'a' = 1 and 'z' = 26.  Add
        ### the result into the running total variable.
        intNameValueRunningTotal += ord(strUserFirstName[i].lower()) - 96

    ### Display the numerical result to the user
    print('The numerical value of your name is:'
          ,str(intNameValueRunningTotal)
          ,'\n' # adding an extra line to help with white space between lab functions
          ,sep = ' '
          )

mainA()

## Count the numbers of lines, words, and non-space characters
## in the target text file.

def mainB():
    ### initialize variables
    intLines                = 0
    intWords                = 0
    intNonSpaceCharacters   = 0

    ### prompt user for file name
    dataFileName = str(input('Enter file name to count: '))

    ### open the file in read-only mode
    dataFile = open(dataFileName, 'r')

    ### loop through each line of the file.
    for line in dataFile:

        ### count this iteration as a line
        intLines += 1

        ### leverage the split method to count the number of words
        intWords += len(line.split())

        ### loop through line split and count non-space characters
        for i in range(len(line.split())):
            intNonSpaceCharacters += len(line.split()[i])

    ### inform user of count results
    print('Results of counting', dataFileName, 'are:')
    print('Lines: \t \t \t', str(intLines))
    print('Words: \t \t \t', str(intWords))
    print('Non-space characters: \t', str(intNonSpaceCharacters))

mainB()
        
