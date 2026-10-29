# 🤖 CodeAlpha Python Internship — Basic Rule-Based Chatbot

![Python](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python)
![Internship](https://img.shields.io/badge/CodeAlpha-Internship-orange?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Completed-brightgreen?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-lightgrey?style=for-the-badge)

---

## 📌 Project Overview

The **Basic Chatbot** is an interactive, rule-based conversational agent developed in Python as part of the **CodeAlpha Python Programming Internship**. 

It simulates conversational exchange by processing natural language input through string normalization, keyword mapping, contextual conditionals, and dynamic system functions (such as system time/date querying and mini-games like Rock-Paper-Scissors).

🔗 **GitHub Repository:** [https://github.com/itsSonam01/CodeAlpha-Projects.git](https://github.com/itsSonam01/CodeAlpha-Projects.git)

---

## ✨ Features & Capabilities

- 💬 **Smart Conversational Logic**: Recognizes everyday greetings, inquiries, compliments, and standard conversation starters.
- 🕒 **Live Utilities**: Returns real-time system clock time and formatted date upon request.
- 🎮 **Interactive Rock-Paper-Scissors Game**: Built-in mini-game using Python's `random` module for instant player-vs-bot games.
- 💡 **Quotes & Motivation**: Shares inspirational quotes, life advice, programming trivia, and fun riddles with answers.
- ❓ **Built-in Guidance**: Integrated `help` command lists accepted triggers and conversation options.
- 🛡️ **Input Sanitization & Graceful Fallback**: Strips casing and extraneous whitespace, and handles unrecognized queries politely.
- 👋 **Clean Exit**: Allows users to terminate sessions cleanly with commands like `bye`, `exit`, or `quit`.

---

## 🛠️ Technologies & Concepts Used

| Technology / Concept | Usage & Implementation |
| :--- | :--- |
| **Language** | Python 3.x |
| **Standard Libraries** | `datetime` (clock & calendar lookups), `random` (decision logic for RPS mini-game) |
| **Control Flow** | Infinite `while` event loop, structured `if-elif-else` conditional dispatch |
| **Data Structures** | Python Lists & String manipulation methods (`lower()`, `strip()`) |
| **Console I/O** | Formatted string outputs and user command prompt reading |

---

## 📂 Project Directory Structure

```text
CodeAlpha_BasicChatbot-main/
│
├── Basic_Chatbot/
│   ├── chatbot.py        # Core application source code
│   └── Readme.md         # Internal module readme
└── README.md             # Main repository documentation
```

---

## 🚀 Getting Started & Execution

### Prerequisites
- Python 3.6 or higher installed on your system.
- No external 3rd-party dependencies or pip packages required (runs purely on standard libraries).

### Running the Chatbot
Open your terminal or command prompt, navigate to the project directory, and execute:

```bash
# Navigate to the chatbot source directory
cd Basic_Chatbot

# Run the chatbot script
python chatbot.py
```

---

## 💬 Supported Commands & Queries

You can interact with the bot using any of the following sample queries:

| Category | Input Prompts / Examples | Bot Response Type |
| :--- | :--- | :--- |
| **Greetings** | `hello`, `hi`, `hey` | Friendly warm welcome |
| **Identity** | `what is your name`, `who are you` | Explains bot identity & CodeAlpha context |
| **Status** | `how are you`, `how are you doing` | Cheerful status reply |
| **Live Time & Date** | `what time is it`, `date`, `what's the date today` | Current time (`HH:MM:SS`) and date (`YYYY-MM-DD`) |
| **Entertainment** | `joke`, `tell me a joke`, `fun fact`, `riddle` | Curated developer jokes, trivia, and riddles |
| **Inspiration** | `quote`, `motivation`, `advice` | Inspiring quotes and motivation |
| **Mini-Game** | `rock`, `paper`, or `scissors` | Plays Rock-Paper-Scissors against random bot pick |
| **Coding Guidance** | `help me with code`, `pattern` | Offers Python guidance and notes |
| **Assistance** | `help` | Lists available commands |
| **Exit** | `bye`, `exit`, `quit` | Polite sign-off and loop termination |

---

## 🖥️ Sample Terminal Interaction

```text
Bot: Chatbot Started!
Bot: Type 'help' to see available commands.
Bot: Type 'bye' to exit.

You: hello
Bot: Hi there! How can I help you?

You: what time is it
Bot: The current time is 11:15:30.

You: tell me a joke
Bot: Why did the computer go to the doctor? Because it caught a virus!

You: rock
Bot: You win! I chose scissors.

You: bye
Bot: Goodbye! Have a great day :)
```

---

## 👩‍💻 Author & Internship Details
- **Author:** **Sonam Thakur**
- **GitHub:** [@itsSonam01](https://github.com/itsSonam01)
- **Repository:** [CodeAlpha-Projects](https://github.com/itsSonam01/CodeAlpha-Projects.git)
- **Company:** [CodeAlpha](https://codealpha.tech/)
- **Domain:** Python Programming Internship
- **Task:** Task 3 — Basic Chatbot
- **License:** MIT License © 2026 Sonam Thakur
