import random
n = 50
to_be_guessed = int(n * random.random()) + 1
guess = 0

while guess != to_be_guessed:
    guess = int(input("New number: "))

    if guess > 0:       # program will exit if 0 or -1 is entered
        if guess > to_be_guessed:
            print("Number too large")
        elif guess < to_be_guessed:
            print("Number too small")
    else:
        print("Sorry that you couldn't find the number!") 
else:
    print("Congratulation. You found it!")