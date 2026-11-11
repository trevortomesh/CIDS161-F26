import random

# Generate a random number to be guessed
number = random.randint(0,100)

print("Guess a magic number between 0 and 100!")

guess = eval(input("Enter your guess: "))

while guess != number:
    if guess == number:
        print("You are correct! The number is ", number)
    elif guess > number:
        print("Your guess it too high!")
    else:
        print("Your guess is too low!")
    guess = eval(input("Enter your guess: "))

