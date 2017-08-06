# Project:      DISC: Function Scholarship
# Name:         Mark Kazzaz
# Goal:         Evaluate a user's eligibilty for a scholarship based on
##              grades, credits, and letters of recommendation

def LetterGrade(strLetterGrade):
    ## convert the uppercase of the string input into a numerical grade value
    if strLetterGrade.upper() == 'A':
        fltNumericGrade = 4.0
    elif strLetterGrade.upper() == 'B':
        fltNumericGrade = 3.5
    elif strLetterGrade.upper() == 'C':
        fltNumericGrade = 3.0
    elif strLetterGrade.upper() == 'D':
        fltNumericGrade = 2.5
    elif strLetterGrade.upper() == 'F':
        fltNumericGrade = 0.0
    else:
    ## if we can't determine the numerical value, set the value -1.0 and handle outside this function
        fltNumericGrade = -1.0
    return(fltNumericGrade)

def CalculateGPA(fltNumericalGradeTotal, intGradeCreditsTotal):
    ## calculate GPA and round the results
    fltGPA = fltNumericalGradeTotal / intGradeCreditsTotal
    return(round(fltGPA,2))

def Eligible(intRecommendationLetters, intGradeCreditsTotal, fltGPA):
    ## consider the values of recommendation latters, grade credit total, and GPA
    ## to determine if the person is eligible for a scholarship
    strEligibleStatus = 'not eligible'
    if intRecommendationLetters >= 2:
        if fltGPA >= 3.7:
            if intGradeCreditsTotal > 20:
                strEligibleStatus = 'eligible'
    return(strEligibleStatus)

def PrintScholarship(intRecommendationLetters, fltNumericalGradeTotal, intGradeCreditsTotal):
    ## caluate the GPA then leverage the Eligible() function to determine eligibilty
    fltGPA = CalculateGPA(fltNumericalGradeTotal, intGradeCreditsTotal)
    strEligibleStatus = Eligible(intRecommendationLetters, intGradeCreditsTotal, fltGPA)
    return(strEligibleStatus)

def main():
    intRecommendationLetters = 0
    fltNumericalGradeTotal = 0.0
    intGradeCreditsTotal = 0
    
    ## Greet user
    print('Let\'s figure out if you\'re eligible for a scholarship.'
          ,'Answer the following questions.'
          ,''
          ,sep = '\n'
          )

    ## Ask and record how many letters of recommedation the student has 
    isValidRecommendationInput = False
    while isValidRecommendationInput == False:
        try:
            intRecommendationLetters = int(input('How many leters of recommendation do you have? '))
            isValidRecommendationInput = True
            print('') ## adding some white space
        except:
            print('Please enter a whole number.')

    ## Figure out how many classes we need to get data for
    isValidClassNumber = False
    while isValidClassNumber == False:
        try:
            intClassNumber = int(input('How many classes did you take? '))
            isValidClassNumber = True
            print('') ## adding some white space
        except:
            print('Please enter a while number.')

    ## Loop for all classes to capture grade and credits
    for i in range(intClassNumber):
        ## loop until we receive a valid grade credits entry
        isValidGradeCredits = False
        while isValidGradeCredits == False:
            try:
                intGradeCredits = int(input('How many credits is class {}? '.format(i+1)))
                intGradeCreditsTotal += intGradeCredits
                if intGradeCredits > 0:
                    isValidGradeCredits = True
                else:
                    print('Input error.  Enter a number greater than zero.')
            except:
                print('Input error.  Enter a number greater than zero.')
                
        ## loop until we receive a valid letter grade
        isValidLetterGrade = False
        while isValidLetterGrade == False:
            ## leverage a function to convert the letter grade
            fltNumericalGrade = LetterGrade(str(input('What is the letter grade for class {}? '.format(i+1))))
            if fltNumericalGrade != -1.0:
                fltNumericalGradeTotal += fltNumericalGrade * intGradeCredits
                isValidLetterGrade = True
            else:
                print('Input error.  Enter a letter grade between A-F.')

        print('') ## adding some white space

    print('You are {} for a scholarship.'.format(PrintScholarship(intRecommendationLetters, fltNumericalGradeTotal, intGradeCreditsTotal)))

main()
