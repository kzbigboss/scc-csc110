# Project:      Lab 5 (KazzazLab05SecHYVer01.py)
# Name:         Mark Kazzaz
# Date:         2017-07-31
# Description:  This program leverages functions to calculate the
##              cost per square inch of a circular pizza.

## Primary function for user to interact with
def main():
### Prompt for input
    print('Let\'s figure out how much your circular pizza cost per square inch!')

    ### Loop until we get valid inputs
    isValidInputs = False
    while isValidInputs == False:
        try:
            fltInputDiameter = float(input('Enter the diameter of your pizza: '))
            fltInputPrice = float(input('Enter the cost of your pizza: '))
            isValidInputs = True  ### inputs didn't cause an error, carry on
        except:
            ### inputs caused an error when being set to float, loop back
            print('Looks like one of your input wasn\'t a number.  Try again.')

### calculate measures
    fltPizzaPerInchCost = PizzaCalc(fltInputDiameter, fltInputPrice)
    print('Your circular pizza cost per square inch is ${:,.2f}'.format(fltPizzaPerInchCost))

## function to calculate area and call cost per inch
def PizzaCalc(fltDiameter, fltPrice):
    fltArea = 3.14 * (fltDiameter/2)**2     ##OK to approximate pi with 3.14 instead of loading math library
    fltPizzaPerInchCost = PizzaPerInchCost(fltArea, fltPrice)
    return(fltPizzaPerInchCost)

## function to calculate per inch cost
def PizzaPerInchCost(fltArea, fltPrice):
    fltPizzaPerInchCost = fltPrice / fltArea
    return(fltPizzaPerInchCost)

main()
