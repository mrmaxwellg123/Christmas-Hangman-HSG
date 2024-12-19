# The Festive Hangman

## Autumn Semester 2024

### Course: 3,793,1.00: Skills: Programming  
**Submitted on**: 19.12.2024  

#### Authors:
- **Manon Genier**: 23-610-431  
- **Maxwell Guettinger**: 23-620-776  
- **Janushani Ranvindran**: 24-607-772  
- **Rinor Abazi**: 23-613-151  
- **Tristan Perroud**: 23-620-123  

---

## 1. Overview

This project is an extended version of the childhood game “Hangman.” It includes a festive Christmas theme which can be played in both single-player and multiplayer modes. Players must guess the hidden word, one letter at a time, while they see their progress through the Hangman figure. Additional features include a Christmas-themed word list, custom visual elements, and background music, bringing the holiday spirit to life. Multiplayer mode allows players to challenge their friends in a fun and competitive setting.

This documentation outlines the key features and instructions for running and experiencing the game.

---

## 2. Description of Code

| **File Name**          | **Description**                                    |
|-------------------------|----------------------------------------------------|
| `main.py`              | Starts the game                                   |
| `christmas_words.py`   | Provides the list of Christmas-themed words        |
| `hangman_visual.py`    | Displays the Hangman figure in the different stages |
| `multiplayer_mode.py`  | Handles multiplayer gameplay logic                 |
| `jingle_bells.mp3`     | Festive background music for the game              |

---

## 3. How to Run the Code

1. **Download the GitHub Folder**:
   - Obtain the folder containing all the game files from the GitHub repository.

2. **Install Required Dependencies**:
   - Make sure `pygame` is installed. Open your terminal or command prompt and type:
     ```
     pip install pygame
     ```

3. **Run the Game**:
   - Locate the folder where the files are saved, then launch `main.py` by typing:
     ```
     python main.py
     ```

4. **Enjoy the Game!**

---

## 4. How to Play

To play the Hangman game, your objective is to guess the hidden word by suggesting letters one at a time. The game offers two modes: **single-player** and **multiplayer**.

- **Single-Player Mode**:  
  The game randomly selects a word from a festive Christmas-themed word list, and your task is to uncover the word before the Hangman figure is fully drawn.

- **Multiplayer Mode**:  
  One player enters a word while the other player attempts to guess it.

After selecting the game mode, you will be prompted to guess a letter:
- If the letter is part of the hidden word, it will be revealed in the correct position.
- If the letter is not part of the word, a part of the Hangman figure will be drawn.

The game continues until:
1. You uncover the entire word (you win!), or  
2. The Hangman figure is completely drawn (you lose!).

Enjoy this Christmas Hangman game!
