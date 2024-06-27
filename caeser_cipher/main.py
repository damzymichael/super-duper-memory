import sys
from art import logo

alphabet = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
]

print(logo)

def encrypt(text, shift):
  encrypted = []
  for ch in text:
    if ch not in alphabet:
      new_char = ch
    else:
      id = alphabet.index(ch)
      shift_by = id + shift
      new_char = alphabet[shift_by]
    encrypted.append(new_char)
  print(''.join(encrypted))

def decrypt(text, shift):
  decrypted = ''
  for ch in text:
    if ch not in alphabet:
      new_char = ch
    else:
      id = alphabet.index(ch)
      shift_by = id - shift
      new_char = alphabet[shift_by]  
    decrypted += new_char
  print(decrypted)

# def caeser()

should_continue = True

while should_continue:
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  if (direction != 'encode' and direction != 'decode'):
    sys.exit('Invalid action')
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))

  shift = shift % 26

  if direction == 'encode':
    encrypt(text, shift)
  else:
    decrypt(text, shift)

  user_continue_preference = input("Type 'yes' if you want to go again. Otherwise type 'no'. \n")
  if user_continue_preference == 'no':
    should_continue = False
    print('Goodbye!')

#TODO-4: Can you figure out a way to ask the user if they want to restart the cipher program?
#e.g. Type 'yes' if you want to go again. Otherwise type 'no'.
#If they type 'yes' then ask them for the direction/text/shift again and call the caesar() function again?
#Hint: Try creating a while loop that continues to execute the program if the user types 'yes'. 
# TODO-5: Refactor into one function 