from art import logo
import random

print(logo)

random_number = random.randint(1, 100)
print('Welcome to the Number Guessing Game!')
print("I'm thinking of a number between 1 and 100.")
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': \n")
attempts = 10 if difficulty == 'easy' else 5

#Todo Remove guess again message when chances have run out
while attempts > 0:
  print(f"You have {attempts} attempts remaining to guess the number.")
  guess = input('Make a guess: ')
  attempts -= 1
  if int(guess) > random_number:
    print('Too high')
    print('Guess again' if attempts > 0 else 'You have run out of chances')
  elif int(guess) < random_number:
    print('Too low')
    print('Guess again' if attempts > 0 else 'You have run out of chances')
  else:
    print(f'You got it! The answer was {random_number}')
    attempts = 0
