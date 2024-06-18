import sys
from art import logo

alphabet = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
]

print(logo)
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
if (direction != 'encode' and direction != 'decode'):
  sys.exit('Invalid action')
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


def encrypt(text, shift):
  encrypted = []
  for ch in text:
    if ch not in alphabet:
      new_char = ch
    else:
      id = alphabet.index(ch)
      shift_by = id + shift
      if (shift_by > len(alphabet) - 1):
        available_to_shift = len(alphabet) - 1 - id
        shift_by = shift - available_to_shift - 1
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

if direction == 'encode':
  encrypt(text, shift)
else:
  decrypt(text, shift)

#TODO-1: Import and print the logo from art.py when the program starts.
#TODO-2: What if the user enters a shift that is greater than the number of letters in the alphabet?
#Try running the program and entering a shift number of 45.
#Add some code so that the program continues to work even if the user enters a shift number greater than 26. 
#Hint: Think about how you can use the modulus (%).
#TODO-3: What happens if the user enters a number/symbol/space?
#Can you fix the code to keep the number/symbol/space when the text is encoded/decoded?
#e.g. start_text = "meet me at 3"
#end_text = "•••• •• •• 3"
#TODO-4: Can you figure out a way to ask the user if they want to restart the cipher program?
#e.g. Type 'yes' if you want to go again. Otherwise type 'no'.
#If they type 'yes' then ask them for the direction/text/shift again and call the caesar() function again?
#Hint: Try creating a while loop that continues to execute the program if the user types 'yes'. 
#TODO-5: Refactor into one function