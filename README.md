# 🚀 CodeAlpha Python Programming Internship — Project Portfolio

![Python](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python)
![Internship](https://img.shields.io/badge/CodeAlpha-Internship-orange?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Completed-brightgreen?style=for-the-badge)
![Projects](https://img.shields.io/badge/Projects-3%2F3%20Completed-success?style=for-the-badge)
![Repository](https://img.shields.io/badge/GitHub-CodeAlpha--Projects-181717?style=for-the-badge&logo=github)
![License](https://img.shields.io/badge/License-MIT-lightgrey?style=for-the-badge)

---

## 📌 Executive Summary

This repository brings together the project portfolio completed by **Sonam Thakur** during the **CodeAlpha Python Programming Internship**. 

The internship curriculum focuses on core computer science fundamentals, algorithmic problem solving, object-oriented software design, dynamic data modeling, and file persistence using modern Python 3.

🔗 **GitHub Repository:** [https://github.com/itsSonam01/CodeAlpha-Projects.git](https://github.com/itsSonam01/CodeAlpha-Projects.git)

---

## 📂 Repository & Project Structure

```text
CodeAlpha-Projects/
│
├── README.md                          # Master overview & portfolio guide (this file)
│
├── CodeAlpha_Hangman-Game/            # Task 1: Word Guessing & State Game
│   ├── hangman_game.py                # Advanced OOP interactive game with animations & hints
│   ├── simple_hangman.py              # Classic baseline implementation (Task 1 specification)
│   ├── Task1.txt                      # Project requirements sheet
│   └── README.md                      # Detailed Task 1 documentation
│
├── CodeAlpha_StockTracker/            # Task 2: Financial Investment & Portfolio Manager
│   ├── stock_tracker.py               # Main tracker with metrics calculation & CSV exporter
│   ├── requirements.txt               # Dependencies documentation (Python Standard Library)
│   ├── .gitignore                     # Git tracking exclusions
│   ├── output/
│   │   └── sample_output.txt          # Sample terminal session output
│   └── README.md                      # Detailed Task 2 documentation
│
└── CodeAlpha_BasicChatbot-main/       # Task 3: Rule-Based Conversational Assistant
    ├── README.md                      # Project root documentation
    └── Basic_Chatbot/
        ├── chatbot.py                 # Conversational bot with live time, dates & mini-games
        └── Readme.md                  # Inner module documentation
```

---

## 🌟 Projects Overview

| Task # | Project Name | Directory | Primary Concepts Covered | Status |
| :---: | :--- | :--- | :--- | :---: |
| **01** | **[Ultimate Hangman Game](CodeAlpha_Hangman-Game/README.md)** | `CodeAlpha_Hangman-Game/` | OOP Architecture, Sets, Dictionaries, State Machines, ASCII Art, ANSI Colors | `COMPLETED` ✅ |
| **02** | **[Stock Portfolio Tracker](CodeAlpha_StockTracker/README.md)** | `CodeAlpha_StockTracker/` | Financial Calculations, Asset Share Weighting, CSV Persistence, Input Validation | `COMPLETED` ✅ |
| **03** | **[Basic Rule-Based Chatbot](CodeAlpha_BasicChatbot-main/README.md)** | `CodeAlpha_BasicChatbot-main/` | Natural Language Token Processing, Condition Dispatch, Datetime API, Mini-Games | `COMPLETED` ✅ |

---

## 🔍 Detailed Project Breakdown

### 1. 🎯 Task 1: Ultimate Hangman Game
- **Directory**: `CodeAlpha_Hangman-Game`
- **Primary Script**: `hangman_game.py`
- **Key Features**:
  - **Themed Vocabulary Sets**: 5 categories (Space, Animals, Ancient Civilizations, Science, Mystery).
  - **Contextual Clues & Power-Ups**: Every word has a custom hint; players can invoke a one-time bonus `HINT` command or type `WORD` to guess the entire word.
  - **Dynamic Stage Art**: 7-stage ASCII visual scaffold with reactive emotional emojis indicating remaining chances.
  - **Two Implementations**: Both an enterprise OOP version (`hangman_game.py`) and a lightweight baseline (`simple_hangman.py`) satisfying initial minimalist specs.
- **Execution**:
  ```bash
  cd CodeAlpha_Hangman-Game
  python hangman_game.py
  ```

---

### 2. 📈 Task 2: Stock Portfolio Tracker
- **Directory**: `CodeAlpha_StockTracker`
- **Primary Script**: `stock_tracker.py`
- **Key Features**:
  - **Curated Market Registry**: Pre-loaded with 10 global stocks (Apple, Tesla, Google, Amazon, Microsoft, Meta, Netflix, Nvidia, Uber, PayPal).
  - **Position Accumulation & Weights**: Dynamically aggregates added share purchases and computes individual percentage weights relative to total investment capital.
  - **Portfolio Insights**: Pinpoints highest-priced assets and the positions representing the highest capital concentration.
  - **CSV File Persistence**: Automatically outputs a structured `portfolio.csv` transaction ledger with header row and summary rows.
- **Execution**:
  ```bash
  cd CodeAlpha_StockTracker
  python stock_tracker.py
  ```

---

### 3. 🤖 Task 3: Basic Rule-Based Chatbot
- **Directory**: `CodeAlpha_BasicChatbot-main`
- **Primary Script**: `Basic_Chatbot/chatbot.py`
- **Key Features**:
  - **Rule-Based Intent Recognition**: Strips casing and leading/trailing whitespace, parsing conversational triggers for greetings, inquiries, and status queries.
  - **Dynamic Utilities**: Queries live system time (`HH:MM:SS`) and date (`YYYY-MM-DD`) via Python's `datetime` module.
  - **Mini-Game Engine**: Built-in interactive Rock-Paper-Scissors game with random computer selection.
  - **Knowledge & Motivation**: Delivers programming jokes, philosophical quotes, riddles, and programming advice.
- **Execution**:
  ```bash
  cd CodeAlpha_BasicChatbot-main/Basic_Chatbot
  python chatbot.py
  ```

---

## 💻 Tech Stack & Dependencies

- **Programming Language:** Python 3.6+
- **External Dependencies:** None. All projects were built using the Python Standard Library (`os`, `csv`, `datetime`, `random`, `sys`, `time`), ensuring universal compatibility without complex environment setups.

---

## ⚙️ Installation & Setup

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/itsSonam01/CodeAlpha-Projects.git
   cd CodeAlpha-Projects
   ```

2. **Verify Python Installation:**
   ```bash
   python --version
   ```

3. **Run Any Selected Task:**
   Follow the run commands provided in each task's section above or consult individual project README files.

---

## 👩‍💻 Author & Internship Details

- **Author:** **Sonam Thakur**
- **GitHub:** [@itsSonam01](https://github.com/itsSonam01)
- **Repository:** [CodeAlpha-Projects](https://github.com/itsSonam01/CodeAlpha-Projects.git)
- **Company:** [CodeAlpha](https://codealpha.tech/)
- **Program:** CodeAlpha Python Programming Internship
- **Objective:** Design, implement, document, and test modular Python software solving defined challenges.
- **License:** MIT License © 2026 Sonam Thakur
