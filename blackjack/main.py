from art import logo
import random

# print(logo)

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def generate_two_cards():
   return [random.choice(cards), random.choice(cards)]

computer = generate_two_cards()
user =  generate_two_cards()

def print_current_values(userValues, computerValues):
   print(f"Your cards {userValues}, current score: {sum(userValues)}")
   print(f"Computer's first card {computerValues[0]}")

def print_final_values(userValues, computerValues):
   print(f"Your final hand {userValues}, final score: {sum(userValues)}")
   print(f"Computer's final hand {computerValues}, final score: {sum(computerValues)}")

print_current_values(user, computer)

keep_playing = True
get_new_card = True

#Todo Reset values when new game is requested
def end_game():
   global keep_playing
   global get_new_card
   get_new_card = False
   replay =  input("Do you want to play another game of blackjack? 'y' or 'n' \n")
   if replay.lower() == 'y':
      keep_playing = True
      get_new_card = True
      play_game()
   else:
      exit()

# Todo Computer loses if computer goes above 21
def play_game():
   while get_new_card:
      continue_play = input("Type 'y' to get another card, type 'n' to pass: \n")
      if sum(computer) < 17:
         computer.append(random.choice(cards))
      if continue_play.lower() == 'y':
         user.append(random.choice(cards))
         if sum(user) > 21:
            print_final_values(user, computer)
            print('You lose')
            # get_new_card = False
            end_game()
         else:
            print_current_values(user, computer)
      else:
         print_final_values(user, computer)
         if sum(user) > sum(computer):
            print('You win')
         elif sum(computer) > sum(user):
            print('Comuter wins')
         else:
            print("It's a draw")
         # get_new_card = False
         end_game()

while keep_playing:
   play_game()
