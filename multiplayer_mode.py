from hangman_visual import display_hangman
from christmas_words import christmas_words
import random
import string

def multiplayer_game():
    """Multiplayer mode where two players guess a random word together."""
    word = random.choice(christmas_words).upper()
    word_letters = set(word)  # letters in the word
    alphabet = set(string.ascii_uppercase)
    used_letters = set()  # what the users have guessed

    lives = 7
    turn = 1  # Player turn tracker

    print("\n🎮 Multiplayer Mode 🎮")
    print("Both players will take turns guessing the same word!\n")
    print("\n🎄 Welcome to Christmas Hangman! 🎅")  # festive welcome message
    
    while len(word_letters) > 0 and lives > 0:
        # Display whose turn it is
        current_player = f"Player {turn}"
        print(f"\n{current_player}, it's your turn!")

        # Show lives and used letters
        print('You have', lives, 'lives left and you have used these letters: ', ' '.join(sorted(used_letters)) if used_letters else 'None')

        # Show the current state of the word
        word_list = [letter if letter in used_letters else '-' for letter in word]
        display_hangman(lives)
        print('Current word: ', ' '.join(word_list))

        # Get user input
        user_letter = input('Guess a letter: ').upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
                print(f"Nice guess, {current_player}! 🎉")
            else:
                lives -= 1  # Deduct a life for an incorrect guess
                print(f"\nSorry, {current_player}, '{user_letter}' is not in the word. 🧁")
        elif user_letter in used_letters:
            print("\nYou've already guessed that letter. Try again! ✨")
        else:
            print("\nInvalid letter. Please enter a valid alphabet letter.")

        # Switch to the other player
        turn = 2 if turn == 1 else 1

    # Game Over: Check if players won or lost
    if lives == 0:
        display_hangman(lives)
        print(f'\nGame Over! 🎅 The word was: {word}. Better luck next time!')
    else:
        print(f'\n🎉 Congratulations! Player {2 if turn == 1 else 1} guessed the word: {word}! 🎄')
