import random


def game():
    print("Hello! What is your name? ")
    name = input()
    b = random.randint(1, 20)
    print(f"Well, {name}, I am thinking of a number between 1 and 20.")
    counter = 0
    while True:
        counter += 1
        print("Take a guess.")
        a = int(input())
        if a > b:
            print("Your guess is too high.")
            continue
        elif a < b:
            print("Your guess is too low.")
            continue
        else:
            print(f"Good job, {name}! You guessed my number in {counter} guesses!")
            break


game()

