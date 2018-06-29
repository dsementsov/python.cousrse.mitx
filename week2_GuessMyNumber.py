# guess my number 


def guess_my_number ():
    guess_low = 0
    guess_high = 100
    print ("Please think of a number between " + str(guess_low) +  " and " + str(guess_high) + "!")
    while True:
        guess = int((guess_high + guess_low)/2)
        print("Is your secret number " + str(guess) + "?")
        guess_direction = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.")   
        if guess_direction == "h":
            guess_high = guess
        elif guess_direction == "l":
            guess_low = guess
        elif guess_direction == "c":
            print("Game over. Your secret number was: " + str(guess))
            break
        else:
            print("Sorry, I did not understand your input.")
guess_my_number()
