# Project:      DISC: If Statements
# Name:         Mark Kazzaz
# Goal:         Post the Decision Structure (If Statement) that
##              will accomplish the following:
##
##              A certain CS professor gives 100-point exams that are
##              graded on the scale 90-100:A, 80-89:B, 70-79:C, 60-69:D.
##              A user puts in their numeric score and their letter grade
##              is displayed.

def main():
    #Obtain numerical score from user, round to integer if they enter a float
    intNumericGrade = int(round(float(input('Enter your numeric score: ')),0))

    #Initialize empty string for letter grade
    strLetterGrade = ''

    #Evaluate if the grade is an A, B, C, or D.  Else, provide an F.
    if intNumericGrade >= 90:
        strLetterGrade = 'A'
    elif intNumericGrade >= 80:
        strLetterGrade = 'B'
    elif intNumericGrade >= 70:
        strLetterGrade = 'C'
    elif intNumericGrade >= 60:
        strLetterGrade = 'D'
    else:
        strLetterGrade = 'F'

    #inform user of resulting letter grade
    print('Your letter grade is: ', strLetterGrade)

main()
