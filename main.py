import random

from art import LOGO


def get_valid_guess():
    while True:
        try:
            guess = int(input("Guess the number between 1 and 100: "))
            return guess
        except ValueError:
            print("Wrong input! Please enter a number.")


def check_guess(guess, number):
    if guess > number:
        print("Too high!")
        return False
    elif guess < number:
        print("Too low!")
        return False
    else:
        print("YOU GUESSED THE NUMBER YAAAYY")
        return True


def play_game(lives, random_number):
    """Play the guessing game with the given number of lives."""
    while lives > 0:
        print(f"You have {lives} attempts remaining.")
        guess = get_valid_guess()

        if check_guess(guess, random_number):
            return True

        lives -= 1

    print("You lose :(")
    print(f"The number was {random_number}")
    return False


# Start the game
print(LOGO)
random_number = random.randint(1, 100)

# Keep asking for game mode until valid input is received
while True:
    game_mode = input("Choose 'easy' or 'hard' mode: ").lower()

    if game_mode == 'easy':
        play_game(10, random_number)
        break
    elif game_mode == 'hard':
        play_game(5, random_number)
        break
    else:
        print("Invalid mode! Please choose 'easy' or 'hard'.")