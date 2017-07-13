# Project:      DISC: Boolean Operators And Or, Blackjack
# Name:         Mark Kazzaz
# Goal:         Collect input as two cards from the user.
##              Calculate Blackjack card game result.

def main():

    # initialize variables
    strCard1, strCard2 = '', ''
    intCard1, intCard2, intCardTotal = 0, 0, 0
    
    # Capture user input of the two cards
    ### Inform user of valid inputs
    print('Enter your two Blackjack cards.  Valid entries include'
          ,'   numerical cards: 2-10'
          ,'   face cards: A, K, Q, J'
          , sep = '\n'
          )

    ### Gather card inputs as string, converting to uppercase
    strCard1 = str(input("What is your first card?: ")).upper()
    strCard2 = str(input("What is your second card?: ")).upper()

    # Check card inputs and convert to integers
    ### Convert card1 face cards to string values
    if strCard1 == 'A':
        strCard1 = '11'
    elif strCard1 == 'K' or strCard1 == 'Q' or strCard1 == 'J':
        strCard1 = '10'

    ### Convert card1 face cards to string values
    if strCard2 == 'A':
        strCard2 = '11'
    elif strCard2 == 'K' or strCard2 == 'Q' or strCard2 == 'J':
        strCard2 = '10'
        
    ### Convert card string values to integer, exit if error
    try:
        intCard1 = int(strCard1)
        intCard2 = int(strCard2)

    except:
        print('invalid input detected, try again')
    
    # Add up the two cards and display to user
    intCardTotal = intCard1 + intCard2

    print(intCardTotal)

main()
