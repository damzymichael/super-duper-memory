import sys
from art import logo

alphabet = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
]

print(logo)

def caeser_cipher(start_text, shift_by, cipher_direction):
  result_text = ''
  if cipher_direction == 'decode':
    shift_by *= -1
  for char in start_text:
    if char in alphabet:
      position = alphabet.index(char)
      new_position = position + shift_by
      #Replacement for adding another set of alphabets to the list
      if new_position > len(alphabet):
        available_to_shift = len(alphabet) - 1 - position
        new_position = shift_by - available_to_shift - 1
      result_text += alphabet[new_position]
    else:
      result_text += char
  print(result_text)


should_continue = True

while should_continue:
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  if (direction != 'encode' and direction != 'decode'):
    sys.exit('Invalid action')
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))

  shift = shift % 26

  caeser_cipher(start_text=text, shift_by=shift, cipher_direction=direction)

  user_continue_preference = input("Type 'yes' if you want to go again. Otherwise type 'no'. \n")
  if user_continue_preference == 'no':
    should_continue = False
    print('Goodbye!')

