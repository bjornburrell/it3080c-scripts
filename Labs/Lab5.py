#Lab 5
#Bjorn Burrell
#Assignment: Write a ‘guess the number game’ where a random number is generated and the user must guess the number. The program says if their number is too high or too low until the right answer is guessed.

import random

numberGuessed = False
number = random.randint(1,99)

print('Mr.Both, the best teacher ever, is thinking of a number between 1 and 99.... guess until you are right!')

while numberGuess is False:
    print('Enter a number...')
    guess = int(input())
    if guess < number:
        print('Your guess is too low!')
    if guess > number:
        print('Your guess is too high!')
    if guess == number:
        print('Good job! You guessed the number ' + str(number) + ' correctly! A+ for you...')
        numberGuessed = True
