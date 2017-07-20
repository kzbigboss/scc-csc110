# Project:      Lab 4 (KazzazLab04SecHYVer01.py)
# Name:         Mark Kazzaz
# Date:         2017-07-20
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
          ,sep = ' '
          )
