import random

numberGuess = False
number = random.randint(1,99)

print('Mr.Both is thinking of a number between 1 and 99.... guess until you are right')

while numberGuess is False:
    print('Enter a number...')
    guess = int(input())
    if guess < number:
        print('Your guess is too low')
    if guess > number:
        print('Your guess is too high')
    if guess == number:
        print('Good job! You guessed the number ' + str(number) + ' correctly! A+ for you...')
        numberGuess = True
