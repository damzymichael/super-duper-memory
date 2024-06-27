import os
# from replit import clear
from art import logo

print(logo)

bids = []

continue_program = True

while continue_program:
  name = input("What's your name \n")
  price = int(input("How much are you bidding? \n"))

  bids.append({"name": name, "price": price})
  other_users = input("Are there other users who wants to bid? type 'yes' or 'no' \n")
  if other_users == 'yes':
    # clear()
    os.system('clear')
  else:
    continue_program = False  

highest_bid = bids[0]
for bid in bids:
  if bid["price"] > highest_bid["price"]:
    highest_bid = bid

print(f"The winner of the auction is {highest_bid['name']}")
