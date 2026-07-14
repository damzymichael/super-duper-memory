from art import logo, vs
from game_data import data
import random 

print(logo)
def format_choice(choice) -> str:
    return f"{choice["name"]}, a {choice["description"]}, from {choice["country"]}"

def generate_and_print_choices(correct_choice=None):
    choices = [None] * 2
    if correct_choice is None:
        choices = random.sample(data, k=2)
    else:
        choices[0] = correct_choice
        new_option = random.choice(data)
        while new_option["name"] == correct_choice["name"]:
            new_option = random.choice(data)
        choices[1] = new_option

    print(f"Compare A: {format_choice(choices[0])}")
    print(vs)
    print(f"Against B: {format_choice(choices[1])}")
    return choices

score = 0
keep_playing = True
choices = generate_and_print_choices()
while keep_playing:
    choice_input = ""
    correct_option = False

    while not correct_option:
        choice_input = input("Who has more followers? Type 'A' or 'B': ").capitalize()
        if choice_input == 'A' or choice_input == 'B':
            correct_option = True
        else:
            print("Incorrect option, try again")

    choice = choices[0 if choice_input == 'A' else 1]
    compare_against_index = 1 if choice_input == 'A' else 0
    if choice["follower_count"] > choices[compare_against_index]["follower_count"]:
        score += 1
        # Mimicking clear screen
        # print("\n" * 20)
        # print(logo)
        # Mimicking clear screen
        print(f"You're right! Current score: {score}")
        choices = generate_and_print_choices(choice)
    else:
        print(f"Wrong answer, Your score is {score}")
        keep_playing = False
