import art
import game_data
import random
import os


def choice():
    global choice_a
    global choice_b
    global last_choice_b

    if len(last_choice_b) == 0:
        choice_a = random.choice(game_data.data)
    else:
        choice_a = last_choice_b

    while True:
        choice_b = random.choice(game_data.data)
        if choice_a != choice_b:
            break


def comparison():
    global choice_a
    global choice_b

    print(f"Compare A: {format_choice(choice_a)}")
    print(art.vs)
    print(f"Against B: {format_choice(choice_b)}")


def format_choice(choice):
    choice_name = choice["name"]
    choice_descr = choice["description"]
    choice_country = choice["country"]
    return f"{choice_name}, a {choice_descr}, from {choice_country}"


def check():
    global choice_a
    global choice_b
    if choice_a["follower_count"] > choice_b["follower_count"]:
        return "a"
    else:
        return "b"


score = 0
streak = 0

last_choice_b = {}

game = True

while game:
    print(art.logo)

    choice_a = {}
    choice_b = {}

    if streak == 1:
        print(f"You are right! Current score: {score}.")

    choice()

    winner = check()

    comparison()

    while True:
        guess = input("Who has more followers? Type 'A' or 'B': ").lower()
        if guess == "a" or guess == "b":
            break

    if guess == winner:
        score += 1
        streak = 1
        last_choice_b = choice_b
        os.system("clear")
    else:
        print(f"Sorry, that is wrong. Final score: {score}.")
        streak = 0
        break
