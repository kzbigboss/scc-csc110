# Project:      Lab 2
# Name:         Zeke Lorens, Mark Kazzaz
# Date:         2017-07-06
# Description:  In class partner lab

## Calculate cost of coffee
def mainA():
    ## Define literal costs
    fltCofferPerPound = 10.5
    fltShippingPerPound = .86
    fltOverhead = 1.50
    
    ## Get input from user
    fltPoundsOrdered = float(input('Input how many pounds of coffee: '))
    
    ## Calculate costs
    fltCoffeeCost = fltCofferPerPound * fltPoundsOrdered
    fltShippingCost = fltShippingPerPound * fltPoundsOrdered
    fltTotalCost = fltCoffeeCost + fltShippingCost + fltOverhead

    ## Respond to the user with total cost
    print('The cost of your order is: ', '${:,.2f}'.format(fltTotalCost))


## Convert Celsius to Fahrenheit, 0-100 in 10s
def mainB():
    print('\t','Celsius', '\t', 'Fahrenheit')
    for i in range(0, 101, 10):
        intCelsius = i
        fltFahrenheit = 9/5 * intCelsius + 32

        ### Since we're always multiplying by a multiple of 10, our
        ### fahrenheit result will not have any fractional values that
        ### need a decimal point.  I'm going to format the float output
        ### of the fahrenheit result to not print the decimal on-screen.
        print('\t', intCelsius,'\t \t', '{0:g}'.format(fltFahrenheit)) 
    
mainA()
print('') # blank space
mainB()
