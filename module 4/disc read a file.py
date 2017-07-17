# Project:      DISC: Read a File
# Name:         Mark Kazzaz
# Goal:         Read dog data file and determine best ranking breed

def main():

    # initialize variables
    dataFileName = 'dogs.txt'
    intLowestRank = 0
    strBestBreed = ''
    isAfterFirstRun = False

    # open the data file in read-only mode
    dataFile = open(dataFileName, 'r')

    # loop through each line of the file
    for line in dataFile:

        # save data from the current line into variables
        strBreed, intRank = line.split()

        # for the first line, set the initial variables to the first line's values
        if isAfterFirstRun == False:
            intLowestRank = intRank
            strBestBreed = strBreed
            isAfterFirstRun = True

        # for the subsequent lines, consider if the current line rank
        # is lower than the overall lowest rank.  If so, overwrite the
        # best rank breed values with the current line values.
        if intRank < intLowestRank:
            intLowestRank = intRank
            strBestBreed = strBreed

    # close the file
    dataFile.close

    # print results
    print('Best ranked breed is: {0}'.format(strBestBreed))

main()
