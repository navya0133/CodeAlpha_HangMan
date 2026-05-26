import random

# Predefined list of words
words = ["python", "apple", "tiger", "chair", "music"]

# Randomly choose a word
chosen_word = random.choice(words)

# Store guessed letters
guessed_letters = []

# Number of incorrect guesses allowed
attempts = 6

print("🎮 Welcome to Hangman Game!")

# Game loop
while attempts > 0:
    display_word = ""

    # Display guessed letters and underscores
    for letter in chosen_word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "

    print("\nWord:", display_word)

    # Check if player guessed the word
    if "_" not in display_word:
        print("🎉 Congratulations! You guessed the word:", chosen_word)
        break

    # Take user input
    guess = input("Guess a letter: ").lower()

    # Validate input
    if len(guess) != 1 or not guess.isalpha():
        print("⚠️ Please enter a single alphabet letter.")
        continue

    # Check repeated guesses
    if guess in guessed_letters:
        print("🔁 You already guessed that letter.")
        continue

    # Add guess to list
    guessed_letters.append(guess)

    # Check correctness
    if guess in chosen_word:
        print("✅ Correct guess!")
    else:
        attempts -= 1
        print("❌ Wrong guess!")
        print("Remaining attempts:", attempts)

# If attempts become 0
if attempts == 0:
    print("\n💀 Game Over!")
    print("The correct word was:", chosen_word)

This is the python code and used concepts are random.choice()
while loop
if-else
Strings
Lists
User input handling
