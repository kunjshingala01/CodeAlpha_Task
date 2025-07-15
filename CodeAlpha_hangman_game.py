import random

# Predefined list of 5 words
word_list = ['apple', 'house', 'train', 'robot', 'chair']

# Randomly choose a word
secret_word = random.choice(word_list)

# Game setup
guessed_letters = []
wrong_guesses = 0
max_wrong_guesses = 6
display_word = ['_' for _ in secret_word]

print("🎮 Welcome to Hangman!")
print("Guess the word, one letter at a time.")

# Main game loop
while wrong_guesses < max_wrong_guesses and '_' in display_word:
    print("\nWord:", ' '.join(display_word))
    print("Guessed letters:", ' '.join(guessed_letters))
    print(f"Remaining attempts: {max_wrong_guesses - wrong_guesses}")
    
    guess = input("Enter a letter: ").lower()

    if not guess.isalpha() or len(guess) != 1:
        print("⚠️ Please enter a single alphabet letter.")
        continue

    if guess in guessed_letters:
        print("🔁 You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    if guess in secret_word:
        print("✅ Correct!")
        for i in range(len(secret_word)):
            if secret_word[i] == guess:
                display_word[i] = guess
    else:
        print("❌ Incorrect.")
        wrong_guesses += 1

# Game result
if '_' not in display_word:
    print("\n🎉 You won! The word was:", secret_word)
else:
    print("\n💀 You lost! The word was:", secret_word)
