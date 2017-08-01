# Date:         08/04/14
# Description:  This program uses "if" statements to convert
#               cards into values and add them.

def blackjack():
    
    #Get user input, set to two cards
    lstCards = []    
    for i in range(2):
        lstCards.append(str(input("What is card " + str(i+1) +": ")))

    #leverage cardcalc() to figure out card values
    for card in lstCards:
        lstCards[lstCards.index(card)] = cardcalc(card)

    #Add together and display
    intTotal = sum(lstCards)
    print("Your total is: ", intTotal)
        
def cardcalc(strCard):
    #set card string to upper case
    strCard = strCard.upper()
    #evaluate face cards, else use inputted value
    if strCard == "J" or strCard == "Q" or strCard == "K":
        intCard = 10
    elif strCard == "A":
        intCard = 11
    else:
        intCard = int(strCard)
    #return an integer
    return(intCard)

blackjack()
