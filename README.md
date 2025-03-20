# Number Guessing Game

A simple yet engaging command-line number guessing game written in Python where players try to guess a randomly generated number between 1 and 100.

## 🎮 Game Overview

Test your intuition and deduction skills by trying to guess a secret number. The game provides feedback after each guess, helping you narrow down the possibilities with each attempt.

### Features:
- Randomly generated number between 1 and 100
- Two difficulty levels: easy (10 attempts) and hard (5 attempts)
- Helpful hints after each guess (too high/too low)
- Input validation to handle non-numeric entries
- Progressive feedback on remaining attempts

## 🎯 How to Play

1. Run the game in your terminal
2. Choose a difficulty level: 'easy' or 'hard'
   - Easy mode gives you 10 attempts
   - Hard mode gives you 5 attempts
3. Guess a number between 1 and 100
4. After each guess, you'll receive feedback:
   - "Too high!" if your guess is above the target number
   - "Too low!" if your guess is below the target number
   - "YOU GUESSED THE NUMBER YAAAYY" if you guess correctly
5. Keep guessing until you find the number or run out of attempts

## 💻 Technical Implementation

### Dependencies
- Python 3.x
- `art.py` module (contains the `LOGO` constant for display)
- `random` module (for generating the secret number)

### Key Functions
- `get_valid_guess()`: Ensures the player enters a valid number and handles exceptions
- `check_guess()`: Compares the player's guess with the target number and provides feedback
- `play_game()`: Manages the game loop, attempts tracking, and win/loss conditions

## 🚀 Installation and Setup

1. Clone this repository:
```
git clone https://github.com/yourusername/number-guessing-game.git
```

2. Navigate to the project directory:
```
cd number-guessing-game
```

3. Ensure you have the `art.py` file with the required `LOGO` constant

4. Run the game:
```
python number_game.py
```

## 🧠 Strategy Tips

1. Start with a guess in the middle of the range (50)
2. Use binary search principles - if too high, guess between your last guess and 1; if too low, guess between your last guess and 100
3. With optimal play, you should be able to find any number within 7 guesses
4. Hard mode requires more efficient guessing!

## 🛠️ Customization Ideas

- Add a scoring system based on number of attempts used
- Implement a leaderboard functionality
- Allow custom number ranges
- Add a time limit for each guess
- Create a two-player mode where one player sets the number

## 📝 License

This project is open source and available under the [MIT License](LICENSE).
