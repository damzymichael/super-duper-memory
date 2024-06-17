import sys

alphabet = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
]

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
if (direction != 'encode' and direction != 'decode'):
  sys.exit('Invalid action')
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


def encrypt(text, shift):
  encrypted = []
  for ch in text:
    id = alphabet.index(ch)
    shift_by = id + shift
    if (shift_by > len(alphabet) - 1):
      available_to_shift = len(alphabet) - 1 - id
      shift_by = shift - available_to_shift - 1
      print(shift_by)
    new_char = alphabet[shift_by]
    encrypted.append(new_char)
  print(''.join(encrypted))

def decrypt(text, shift):
  decrypted = ''
  for ch in text:
    id = alphabet.index(ch)
    shift_by = id - shift
    new_char = alphabet[shift_by]
    decrypted += new_char
  print(decrypted)

if direction == 'encode':
  encrypt(text, shift)
else:
  decrypt(text, shift)
