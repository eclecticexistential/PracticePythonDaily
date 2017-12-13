import random

def get_words():
    print("Which word bank do you want to use?")
    choice = input("Enter f for fruits or w for words.").lower()
    secret_word = ""
    if choice == "f":
        secret_word = random.choice(fruits)
    elif choice == "w":
        secret_word = random.choice(words)
    return secret_word

fruits = ['apple','banana','orange','coconut','strawberry','lime','grapefruit','lemon','kumquat','blueberry','melon']
words = ['brutus','golden','tribute','growth','dedicate','winged','police']
