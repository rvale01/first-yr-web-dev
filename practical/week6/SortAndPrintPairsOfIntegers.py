import random

integerOne = 0
integerTwo = 0
temporaryInteger = 0
continueOrStop = "Continue"
reply = ""


while continueOrStop == "Continue":
    print("Please enter a pair of positive integers, e.g. 456 and 10. \n")
    integerOne = int(input())
    integerTwo = int(input())

    if integerOne > integerTwo:
        temporaryInteger = integerOne
        integerOne = integerTwo
        integerTwo = temporaryInteger

    print("The correct ordering of the entered pair of integers is : " . integerOne . " " . integerTwo . "\n")
    print("\n")
    continueOrStop = "Not known"

    print("If you do not wish to enter another pair of positive integers, input 'Stop'." . 
          "If you do want to enter another pair of positive integers, input 'Continue'. \n")

    while (!(continueOrStop == "Continue") || (continueOrStop == "Stop")):
        reply = input()
        if reply == "Stop":
            continueOrStop = "Stop"
        elif reply == "Continue"
            continueOrStop = "Continue"
        else
            print("Please enter either 'Continue' or 'Stop'. Nothing else \n")
