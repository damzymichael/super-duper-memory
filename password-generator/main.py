import random

#Improve to make sure length is not greater than available letters

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Style One
# password_1 = ''
# password_2 = []

# for char in range(1, nr_letters + 1):
#   random_char = random.choice(letters)
#   password_1 += random_char

password = []
for n in range(1, nr_letters + 1):
  random_index = random.randint(0, len(letters) - 1)
  password.append(letters[random_index])

for n in range(1, nr_symbols + 1):
  random_index = random.randint(0, len(symbols) - 1)
  password.append(symbols[random_index])

for n in range(1, nr_numbers + 1):
  random_index = random.randint(0, len(numbers) - 1)
  password.append(numbers[random_index])

random.shuffle(password)
password = ''.join(password)
print(f"Your password is {password}")
