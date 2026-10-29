"""
Filname: NumberGuessing_Game.py
Author: Raynor Matos Berry
Created: 10/29/2026
Instructor: Burgess
"""
import random
#prints a random number between 1 & 100
number = random.randint(1,100)
print(number)

guess = 0
attempts = guess+1
print("greetings user please guess a number between 1 and 100")
#while
while (guess != number):
guess = int(input (" guess a number:"))
if guess < number:
    print("Too low! Try again")
    attempts = attempts + 1
elif guess > number:
    print("Too high! Try again")
    attempts = attempts + 1
else: guess == number

#conditional
print("Congratulations! You guessed the number")
print(attempts)
