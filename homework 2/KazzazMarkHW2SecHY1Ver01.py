# Project:      HW2 (KazzazMarkHW2SecHYVerXX.py)
# Name:         Mark Kazzaz
# Date:         2017-07-19
# Description:  This program will cost out the total order input
##              by a user, inclusive of shipping, handling, and tax.


def main():
    ## Initialize variables & settings
    ### Settings and literals
    intItemPrompt       = 3
    fltTaxRate          = 0.09
    fltShipHandFlat     = 5.00  # flat rate to add to shipping and handling calculation
    fltShipHandPerLBS   = 0.25  # variable rate to calculate shipping and handling per pound

    ### Variables for inputs and calculations
    lstItemDesc         = []
    lstItemPrice        = []
    lstItemQuantity     = []
    lstItemWeightLBS    = []
    fltSubTotal         = 0.0
    fltWeightLBSTotal   = 0.0
    fltShipHandTotal    = 0.0
    fltTaxTotal         = 0.0
    fltGrandTotal       = 0.0
    strSalesSummary     = ''


    ## Greet user
    print('Greetings!  Please prepare to enter'
          ,intItemPrompt
          ,'items to calculate sales total.'
          ,''
          )

    ## Loop for input
    for i in range(intItemPrompt):
        
        ## Prepare a custom prompt for each input comment
        ## Prompt user for input
        ## Repeat four times for description, price, quantity, & weight
        strPrompt = 'Item ' + str(i+1) + ' Description: '
        lstItemDesc.append(str(input(strPrompt)))

        strPrompt = 'Item ' + str(i+1) + ' Price: '
        lstItemPrice.append(float(input(strPrompt)))

        strPrompt = 'Item ' + str(i+1) + ' Quantity: '
        lstItemQuantity.append(int(input(strPrompt)))

        strPrompt = 'Item ' + str(i+1) + ' Weight in Pounds: '
        lstItemWeightLBS.append(float(input(strPrompt)))

        ## Add some white space between items
        print()
        
    ## Loop again to figure out running totals

    for i in range(intItemPrompt):
        fltSubTotal += lstItemPrice[i] * lstItemQuantity[i]
        fltWeightLBSTotal += lstItemWeightLBS[i] * lstItemQuantity[i]

    ## Add running totals together to figure out totals
    fltTaxTotal = fltSubTotal * fltTaxRate
    fltShipHandTotal = (fltWeightLBSTotal * fltShipHandPerLBS) + fltShipHandFlat
    fltGrandTotal = fltSubTotal + fltTaxTotal + fltShipHandTotal

    ## Summarize sale transaction to user
    ### Create a string via loop to summarize items and quantites
    for i in range(intItemPrompt):

        ## Adding some flare so it's easy for the user to understand
        ## a summary of all the items bought.  Will use a comma separator
        ## to separate all the items except for the last one.  Will use an
        ## ampersand to join the last item to the summary.
        strLineEnd = ', '
        strLastItem = ''
        if i == intItemPrompt-1:
            strLineEnd = ''
            strLastItem = '& '

        ## Concatenate all the items together into a single sales summary string
        strSalesSummary = strSalesSummary + strLastItem + str(lstItemQuantity[i]) + ' x ' + lstItemDesc[i] + strLineEnd

    print('You purchased: ', strSalesSummary, sep = '')
    print('Your subtotal charge is: ${:,.2f}'.format(fltSubTotal))
    print('Your shipping and handling charge is: ${:,.2f}'.format(fltShipHandTotal))
    print('Your tax charge is: ${:,.2f}'.format(fltTaxTotal))
    print('Your grand total is: ${:,.2f}'.format(fltGrandTotal))

main()
