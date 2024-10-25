from art import logo
import random

print(logo)

def play_again():
  still_playing = input("Do you want to play another game? type 'y' for yes and 'n' for no: ")
  if still_playing == 'y':
    play_game()

def retry(attempts, guess):
  if attempts > 0 :
    print('Guess again')
  else: 
    print('You have run out of chances')
    print(f"The correct guess is {guess}")
    play_again()

def play_game():
  random_number = random.randint(1, 100)
  print('Welcome to the Number Guessing Game!')
  print("I'm thinking of a number between 1 and 100.")
  difficulty = input("Choose a difficulty. Type 'easy' or 'hard': \n")
  attempts = 10 if difficulty == 'easy' else 5
  while attempts > 0:
    print(f"You have {attempts} attempts remaining to guess the number.")
    guess = input('Make a guess: ')
    attempts -= 1
    if int(guess) > random_number:
      print('Too high')
      retry(attempts, random_number)
    elif int(guess) < random_number:
      print('Too low')
      retry(attempts, random_number)
    else:
      print(f'You got it! The answer was {random_number}')
      attempts = 0
      play_again()

play_game()
