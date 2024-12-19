import random

import pygame
from christmas_words import christmas_words
from hangman_visual import display_hangman
from multiplayer_mode import multiplayer_game
import string
import pygame

def play_music():
    """Play Christmas music in the background using pygame."""
    pygame.mixer.init()
    pygame.mixer.music.load("jingle_bells.mp3")
    pygame.mixer.music.play(-1)  # Loop indefinitely

def get_valid_word():
    word = random.choice(christmas_words)  # randomly chooses something from the list
    while '-' in word or ' ' in word:
        word = random.choice(christmas_words)

    return word.upper()

def single_player():
    """Single-player mode for Christmas Hangman."""
    word = get_valid_word()
    word_letters = set(word)  # letters in the word
    alphabet = set(string.ascii_uppercase)
    used_letters = set()  # what the user has guessed

    lives = 7

    print("\n🎄 Welcome to Christmas Hangman! 🎅")# getting user input
    while len(word_letters) > 0 and lives > 0:
        # letters used
        # ' '.join(['a', 'b', 'cd']) --> 'a b cd'
        print('You have', lives, 'lives left and you have used these letters: ', ' '.join(sorted(used_letters)) if used_letters else 'None')

        # what current word is (ie W - R D)
        word_list = [letter if letter in used_letters else '-' for letter in word]
        display_hangman(lives)
        print('Current word: ', ' '.join(word_list))

        user_letter = input('Guess a letter: ').upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
                print('')

            else:
                lives = lives - 1  # takes away a life if wrong
                print('\nYour letter,', user_letter, 'is not in the word.❌')

        elif user_letter in used_letters:
            print('\nYou have already used that letter. Guess another letter.✨')

        else:
            print('\nThat is not a valid letter.')

    # gets here when len(word_letters) == 0 OR when lives == 0
    if lives == 0:
        display_hangman(lives)
        print('You died, sorry.❄️ The word was', word)
    else:
        print('YAY! You guessed the word🎅', word, '!!')

def main():

    """Main menu to choose modes."""
    print("🎄 Welcome to the Hangman Game with Christmas Theme 🎄")
    play_music()
    while True:
        print("\nChoose a mode:")
        print("1. Single Player 🎁")
        print("2. Multiplayer 🎮")
        print("Q. Quit")

        choice = input("Enter your choice: ").lower()
        # Condition to check if the user selects single-player mode
        if choice == "1": 
            single_player()
        # Condition to check if the user selects multiplayer mode
        elif choice == "2": 
            multiplayer_game()
        elif choice == "q": # Condition to quit the game
            print("🎅 Goodbye! Have a Merry Christmas! 🎄")
            break
        else:
            print("Invalid choice. Please try again!")

if __name__ == "__main__":
    main()
