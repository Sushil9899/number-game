import random

number = random.randint(1,9)
chances = 0
print("guess a number between 1 - 9")

while chances < 5 :
    guess = int(input("enter your guess"))

    if guess == number:
        print("You win.")
        break

    elif guess  < number :
        print("Your guess was too low", guess)

    else :
        print("Your guess was too high", guess)

    chances = chances + 1

if not chances < 5 :
    print("You lose.")    