# Project:      Lab 3 (KazzazLab03SecHYVer01.py)
# Name:         Mark Kazzaz
# Date:         2017-07-16
# Description:  This program will
##                  A: calculate a user's BMI and respond to the result
##                  B: determine if a user is eligible to run for Congress

# First objective - calculate user's BMI
def mainA():
    # inform user we're going to calculate BMI
    print('Greetings!  Enter the following variables and we can calculate your BMI.')
    
    # get user's weight in pounds
    intUserWeightLBS = int(input('Enter weight in whole pounds: '))

    # get user's heigh in inches
    intUserHeightIN = int(input('Enter height in whole inches: '))

    # calculate user's BMI
    fltUserBMI = float((intUserWeightLBS * 703) / (intUserHeightIN ** 2))

    # determine user's position in regards to the healthy
    # range of 19-25

    if fltUserBMI < 19:
        strBMIRangeResult = 'below'
    elif fltUserBMI > 25:
        strBMIRangeResult = 'above'
    else:
        strBMIRangeResult = 'within'

    # print out the user's BMI and range result

    print('Your BMI is {:.0f}.'.format(fltUserBMI)
          ,'This is considered {} the healthy range of 19-25.'.format(strBMIRangeResult)
          ,sep = '\n'
          )

# Second objective - determine user's eligibilty to run for Congress
def mainB():
    # inform user we're going to determine their eligibilty to run for Congress
    print('Greetings! Answer the following questions and we\'ll determine'
          ,'if you\'re eligible to run for either chamber of the US Congress.'
          ,sep = '\n'
          )

    # get user's age
    intUserAgeYears = int(input('Enter your age: '))

    # get user's length of US citizenship
    intUserCitizenshipYears = int(input('Enter the number of years you\'ve been a US citizen: '))

    # initialize boolean variables, default to FALSE
    isSenateEligible = False
    isHouseEligible = False

    # determine if user is eligble for Senate
    if intUserAgeYears > 30:
        if intUserCitizenshipYears > 9:
            isSenateEligible = True

    # determine if user is eligble for House of Representatives
    if intUserAgeYears > 25:
        if intUserCitizenshipYears > 7:
            isHouseEligible = True

    # determine eligibility for both chambers, set default as neither:
    ## NOTE: order matters.  Since I'm starting with a default result,
    ## I need to evaluate eligiblity from lowest requirements to
    ## highest requirements.

    strChamberResult = 'You are not eligible to run for Congress.'

    if isHouseEligible == True:
        strChamberResult = 'You are eligible to be a Representative.'
    
    if isSenateEligible == True:
        if isHouseEligible == True:
            strChamberResult = 'You are eligible to be a Senator or a Representative.'

    # inform user the result of their eligbility
    print(strChamberResult)


mainA()
print()
mainB()


