def main():
    intAge = 0
    while intAge < 21:
        intAge = int(input("What age would you like to enter?"))
        if intAge == 7:
              intAge = intAge + 14
        else:
            print("you are",intAge)
            intAge = 0

    print("You are out")

main()
