# Name:		Mark Kazzaz
# Section:	CSC110.1180
# Assignment:	DISC - Loop Accumulator

def main():
    # initialize variables

    intNumberPrompts = 4
    fltRunningTotal = 0

    # prompt user for numbers

    print('Enter ', intNumberPrompts, 'numbers...')

    for i in range(4):
        fltNumberInput = float(input('Enter a number: '))
        fltRunningTotal = fltRunningTotal + fltNumberInput

    # summarize and print results
    fltAverageInputs = fltRunningTotal / intNumberPrompts
    print('Your inputs totaled', fltRunningTotal, 'and averaged', fltAverageInputs)

main()
