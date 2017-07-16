# Project:      DISC: While Loop - $100!
# Name:         Mark Kazzaz
# Goal:         Collect monetary inputs from user until total
##              amount exceeds $100.00.

def main():
    # initialize variables as float data type
    fltTotalMonetaryInput = float(0)
    fltTotalMonetaryMinimum = float(100)

    # default to a true loop
    # break the loop once the inputs exceed the minimum
    while True:
        
        # accept input from user
        fltTotalMonetaryInput = fltTotalMonetaryInput + float(input('Enter monetary input: '))

        # determine if total amount exceeeds the minimum amount
        if fltTotalMonetaryInput > fltTotalMonetaryMinimum:
            # if inputs exceed minimum, inform user and quit program
            print(''
                  ,'Monetary threshold of $100.00 met. Congrats!'
                  ,'Exiting program.'
                  ,sep = '\n'
                  )
            break

        # if inputs are less than minimum, inform user and loop program
        print(''
              ,'Total monetary inputs must exceed $100.00.'
              ,'Current total monetary input is: '
              ,fltTotalMonetaryInput
              ,'Please continue to input monetary deposits.'
              , sep = '\n'
              )

main()
