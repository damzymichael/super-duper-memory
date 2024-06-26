import random
from hangman_art import stages, logo
from hangman_words import word_list

end_of_game = False
chosen_word = random.choice(word_list)

print(logo)
# print(f'Pssst, the solution is {chosen_word}.')

display = []
word_length = len(chosen_word)
lives = 6
for _ in range(word_length):
  display += '_'

print(display)

while not end_of_game:
  guess = input('Guess a letter:\n').lower()
  if guess in display:
    print(f'You have already guessed {guess}')
  for position in range(word_length):
    letter = chosen_word[position]
    if letter == guess:
      display[position] = letter
  if guess not in chosen_word:
    print(f'{guess} is not in the word')
    lives -= 1
    if lives == 0:
      end_of_game = True
      print('You lose')
    print(stages[lives])
  print(f"{' '.join(display)}")
  if "_" not in display:
    end_of_game = True
    print('You win')
