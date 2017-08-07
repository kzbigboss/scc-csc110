# Project:      DISC: Lists and Master list
# Name:         Mark Kazzaz
# Goal:         Combine three related book inventory lists into a single list
##              and print out summary information

def main():
    ## define lists via random books from Amazon.com recommendations
    lstBookMasterData = []
    
    lstBookTitles = ['Persepolis Rising (The Expanse)'
                     ,'The Girl With All the Gifts'
                     ,'The Dark Tower I: The Gunslinger'
                     ,'The Human Division (Old Man\'s War Book 5)'
                     ,'Ninefox Gambit (Machineries of Empire Book 1)'
                     ]

    lstBookPrices = [25.20, 27.14, 24.52, 8.99, 8.81]

    lstBookQuantities = [185, 134, 164, 424, 439]

    ## conslidate lists into master list
    for i in range(len(lstBookTitles)):
        lstBookMasterData.append([  #making a list of lists
             lstBookTitles[i]       #position 0 = title
            ,lstBookPrices[i]       #position 1 = price
            ,lstBookQuantities[i]   #position 2 = quantity
            ])

    ## print each book title and associated inventory value (quantity * price)
    for i in range(len(lstBookMasterData)):
        strTitle            = lstBookMasterData[i][0]
        fltInventoryValue   = lstBookMasterData[i][1] * lstBookMasterData[i][2]
        print('The book "{0}" has an inventory value of ${1:,.2f}.'.format(
            strTitle
            ,fltInventoryValue
            )
              )
main()
