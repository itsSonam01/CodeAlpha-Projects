# 🎯 CodeAlpha Python Internship — Ultimate Hangman Game

![Python](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python)
![Internship](https://img.shields.io/badge/CodeAlpha-Internship-orange?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Completed-brightgreen?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-lightgrey?style=for-the-badge)

---

## 📌 Project Overview

The **Ultimate Hangman Game** is an enhanced, interactive word puzzle challenge built in Python for the **CodeAlpha Python Programming Internship**. 

While fulfilling the core requirements of Task 1 (random word selection, 6 maximum incorrect attempts, and letter-by-letter guessing), this implementation elevates the classic terminal game into an engaging experience featuring themed categories, dynamic contextual hints, animated ASCII art stages, ANSI color-coded feedback, and special gameplay power-ups.

A lightweight baseline version (`simple_hangman.py`) is also included alongside the advanced game (`hangman_game.py`) for architectural comparison.

🔗 **GitHub Repository:** [https://github.com/itsSonam01/CodeAlpha-Projects.git](https://github.com/itsSonam01/CodeAlpha-Projects.git)

---

## ✨ Key Features & Highlights

- 🎨 **Themed Categories & Vocabulary**:
  - 🌟 **SPACE**: Galaxy, Nebula, Quasar, Cosmos, Asteroid
  - 🐾 **ANIMALS**: Elephant, Octopus, Penguin, Giraffe, Butterfly
  - 🏛️ **ANCIENT**: Pyramid, Sphinx, Pharaoh, Temple, Oracle
  - 🔬 **SCIENCE**: Molecule, Quantum, Neutron, Plasma, Enzyme
  - 🎨 **MYSTERY**: Enigma, Cipher, Puzzle, Riddle, Secret
- 💡 **Contextual & Bonus Hints**:
  - Every word has a custom descriptive clue displayed on screen.
  - Players can invoke a one-time power-up (`HINT`) to reveal an unguessed secret letter.
- ⚡ **Full Word Guessing**: Players confident in their answer can type `WORD` to guess the entire solution at once.
- 🎭 **Evolutionary ASCII Art**: 7-stage visual scaffold with expressive emoji reactions tracking remaining lives.
- 🌈 **Terminal Aesthetics**: ANSI color formatting (cyan titles, green victories, red alerts) and pacing delays for suspense.
- 🔁 **Replayability**: Option to select a category manually or choose a random surprise, followed by prompt-based rematch looping.

---

## 🛠️ Technical Concepts & Architecture

- **Object-Oriented Design (OOP)**: Structured inside a robust `HangmanGame` class cleanly isolating state reset, input validation, clue dispatch, guess evaluation, and victory/defeat rendering.
- **Data Structures**:
  - Nested Python `dict` mapping themes to word and hint arrays.
  - Python `set` collections for $O(1)$ letter containment checks and tracking correct/incorrect guesses.
- **Error Handling**: Graceful interception of invalid inputs, repeated letter guesses, and `KeyboardInterrupt` (`Ctrl+C`).
- **Standard Libraries**: Built exclusively using `random`, `time`, and `sys` (zero external dependencies).

---

## 📂 Project Directory Structure

```text
CodeAlpha_Hangman-Game/
│
├── hangman_game.py       # Feature-rich OOP Ultimate Hangman game
├── simple_hangman.py     # Minimalist classic script (Task 1 specification baseline)
├── Task1.txt             # Original CodeAlpha internship assignment requirements
└── README.md             # Detailed project documentation
```

---

## 🚀 How to Run the Game

### Prerequisites
- Python 3.x installed on your operating system.

### Execution
From your terminal or command prompt, navigate to the folder and run:

```bash
# Run the Ultimate Feature-Rich Version
python hangman_game.py

# Or run the Simple Traditional Version
python simple_hangman.py
```

---

## 🎮 How to Play & Controls

1. **Category Selection**: Choose your favorite subject (1–5) or let fate decide with option 2.
2. **Guessing Options**:
   - Enter any letter from **A to Z** to guess one character.
   - Type **`HINT`** to use your single-use bonus clue revealing a secret letter.
   - Type **`WORD`** to attempt solving the full puzzle in a single shot.
3. **Winning & Losing**:
   - You have **6 allowed mistakes**.
   - Reveal all missing characters before the hangman scaffold is complete to win!

---

## 🖥️ Preview / Sample Gameplay

```text
╔══════════════════════════════════════════════════╗
║        🎯 ULTIMATE HANGMAN CHALLENGE 🎯          ║
╚══════════════════════════════════════════════════╝

════════════════════════════════════════════════════════════
🎮 CATEGORY: 🌟 SPACE
💡 HINT: Colorful space cloud
════════════════════════════════════════════════════════════

   ┌─────┐
   │     │
   │     😟
   │     │
   │     
   │     
───┴─────
Getting risky!

🎯 WORD: 🔤 N  🔤 E  🔤 B  ❓ _  🔤 L  🔤 A 
💔 Wrong guesses: 2/6
✅ Correct: A B E L N
❌ Wrong: T X
════════════════════════════════════════════════════════════

📝 Your guess: U
🎉 Great job! 'U' is in the word!

🏆 CONGRATULATIONS! YOU WON! 🏆
✨ You successfully guessed: NEBULA
```

---

## 👩‍💻 Author & Internship Details
- **Author:** **Sonam Thakur**
- **GitHub:** [@itsSonam01](https://github.com/itsSonam01)
- **Repository:** [CodeAlpha-Projects](https://github.com/itsSonam01/CodeAlpha-Projects.git)
- **Company:** [CodeAlpha](https://codealpha.tech/)
- **Domain:** Python Programming Internship
- **Task:** Task 1 — Hangman Game
- **License:** MIT License © 2026 Sonam Thakur
