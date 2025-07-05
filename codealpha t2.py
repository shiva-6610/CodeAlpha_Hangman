import random

# Predefined list of words
word_list = ["apple", "banana", "grape", "mango", "peach"]

# Randomly choose a word from the list
secret_word = random.choice(word_list)
guessed_letters = []
attempts_left = 6
display_word = ["_"] * len(secret_word)

print("🎮 Welcome to Hangman!")
print("Try to guess the word, one letter at a time.")
print("You have 6 incorrect guesses allowed.\n")

# Main game loop
while attempts_left > 0 and "_" in display_word:
    print("Word:", " ".join(display_word))
    print("Guessed letters:", " ".join(guessed_letters))
    guess = input("Enter a letter: ").lower()

    # Validate input
    if len(guess) != 1 or not guess.isalpha():
        print("❗ Invalid input. Enter only a single letter.\n")
        continue

    # Check if letter was already guessed
    if guess in guessed_letters:
        print("⚠️ You already guessed that letter.\n")
        continue

    # Add guess to guessed letters
    guessed_letters.append(guess)

    if guess in secret_word:
        print("✅ Correct!\n")
        # Reveal the letter in the word
        for i in range(len(secret_word)):
            if secret_word[i] == guess:
                display_word[i] = guess
    else:
        attempts_left -= 1
        print(f"❌ Wrong! You have {attempts_left} guesses left.\n")

# Game over
if "_" not in display_word:
    print(f"🎉 You guessed it! The word was '{secret_word}'. You win!")
else:
    print(f"💀 Game Over! The word was '{secret_word}'. Better luck next time.")
