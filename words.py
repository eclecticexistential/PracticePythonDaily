import random

def get_words():
    print("Which word bank do you want to use?")
    choice = input("Enter f for fruits, n for names, w for words, or a for animals.").lower()
    secret_word = ""
    if choice == "f":
        secret_word = random.choice(fruits)
    elif choice == "w":
        secret_word = random.choice(words)
    elif choice == "n":
        secret_word = random.choice(names)
    elif choice == "a":
        secret_word = random.choice(animals)
    return secret_word

fruits = ['apple','banana','orange','coconut','strawberry','lime','grapefruit','lemon','kumquat','blueberry','melon']
names = ['brutus', 'justin','jessica','michael','michelle','chase','brandon','cathy','rebecca','rachael']
words = ['failed','tribute','growth','dedicate','winged','police','charming','capitalize','generate']
animals = ['elephant','wolf','coyote','rhinosaurs','giraffe','gorilla','boar','dolphin','whale']
