import random

def comp_guess_game():
    hidden_number = int(input("This is the secret number I've picked, between 1 and 10."))
    computer_guess = random.randint(1, 10)
    guesses = list()

    while True:
        guesses.append(computer_guess)
        if computer_guess == hidden_number:
            if len(guesses) == 1:
                print("The computer guessed your secret number on the first try!")
                break
            else:
                print("The computer guessed your secret number " + str(hidden_number) + " with only " + str(
                    len(guesses)) + " guesses!")
                break
        elif len(guesses) < 5:
            if computer_guess < hidden_number:
                print("The computer's guess is: " + str(computer_guess) + ". Let's tell them it's too low.")
                x = computer_guess+1
                computer_guess = random.randint(x,10)

            elif computer_guess > hidden_number:
                print("The computer's guess is: " + str(computer_guess) + ". Let's tell them it's too high.")
                x = computer_guess-1
                computer_guess = random.randint(1,x)
        else:
            print("""You win!
The computer was unable to guess your number in 4 guesses.
""")
            break
comp_guess_game()