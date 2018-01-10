import os
import random
import sys
import words

#clear doesn't ?
def clear():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def draw(bad_guesses, good_guesses, secret_word):
    clear()
    print('Strikes: {}/7'.format(len(bad_guesses)))
    print('')

    for letter in bad_guesses:
        print(letter, end=" ")
    print('\n\n')

    for letter in secret_word:
        if letter in good_guesses:
            print(letter, end="")
        else:
            print('_ ', end="")
    print('')

def get_guess(bad_guesses,good_guesses):
    while True:
        guess = input("Guess a letter: ").lower()

        if guess in bad_guesses or guess in good_guesses:
            print("You've already guessed that letter!")
        elif not guess.isalpha():
            print("You can only guess letters!")
        else:
            return guess

def winning_guess(guess,secret_word):
    if guess == secret_word:
        print("You win!")
        play_again()
    elif len(guess) != 1:
        print("You can only guess a single letter.")

def play(done):
    clear()
    secret_word = words.get_words() # set(words.get_words())
    bad_guesses = [] #set() ?
    good_guesses = [] # set() ?

    while True:
        draw(bad_guesses, good_guesses, secret_word)
        guess = get_guess(bad_guesses,good_guesses) #bad_guesses | good_guesses set?
        winning_guess(guess,secret_word)

        if guess in secret_word:
            good_guesses.append(guess) #use add instead because set
            #if secret_word is a set the following part can be omitted
            found = True
            for letter in secret_word:
                if letter not in good_guesses:
                    found = False
            # and the next if statement would be "if not word_set.symmetric_difference(correct):
            if found:
                print("You win!")
                print("The secret word was {}".format(secret_word))
                done = True
        else:
            bad_guesses.append(guess) #use add instead because set
            if len(bad_guesses) == 7:
                draw(bad_guesses,good_guesses,secret_word)
                print("You lost!")
                print("The secret word was {}".format(secret_word))
                done = True

        if done:
            play_again()

def play_again():
    play_again = input("Play again? Y/n ").lower()
    if play_again != "n":
        return play(done=False)
    else:
        sys.exit()

def welcome():
    start = input("Press enter/return to start or Q to quit").lower()
    if start == 'q':
        print('Bye!')
        sys.exit()
    else:
        return True

done = False

while True:
    clear()
    welcome()
    play(done)
