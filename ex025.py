from random import randint

print('Try to guess the number I am thinking of between 0 and 5.')
number = int(input("Enter a number: "))

randomNumber = randint(0, 5)

if(number == randomNumber):
    print(f"Congratulations! You guessed the number {randomNumber}.")
else:
    print(f"Sorry, you guessed {number}, but I was thinking of {randomNumber}.")