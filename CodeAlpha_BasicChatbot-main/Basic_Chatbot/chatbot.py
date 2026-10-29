def chatbot_response(user_input):
    user_input = user_input.lower().strip()

    if user_input in ["hello", "hi", "hey"]:
        return "Hi there! How can I help you?"

    elif user_input in ["how are you", "how are you doing"]:
        return "I'm doing great! Thanks for asking :)"

    elif user_input in ["what is your name", "who are you"]:
        return "I am a simple Python chatbot created for CodeAlpha internship."

    elif user_input in ["help"]:
        return "You can say: hello, how are you, what is your name, bye"

    elif user_input in ["joke", "tell me a joke"]:
        return "Why did the computer go to the doctor? Because it caught a virus!"

    elif user_input in ["weather", "what's the weather like"]:
        return "I can't provide real-time weather updates, but you can check your local weather service!"

    elif user_input in ["news", "latest news"]:
        return "I can't fetch real-time news, but you can check news websites or apps for the latest updates."

    elif user_input in ["time", "what time is it"]:
        from datetime import datetime
        current_time = datetime.now().strftime("%H:%M:%S")
        return f"The current time is {current_time}."

    elif user_input in ["date", "what's the date today"]:
        from datetime import datetime
        current_date = datetime.now().strftime("%Y-%m-%d")
        return f"Today's date is {current_date}."

    elif user_input in ["pattern", "show patterns", "list patterns"]:
        return "You can view the pattern printing programs by running the main function in the code."

    elif user_input in ["help me with code", "code help"]:
        return "I can provide guidance on Python programming. What do you need help with?"

    elif user_input in ["motivation", "inspire me"]:
        return "Keep pushing forward! Every step you take is a step closer to your goals."

    elif user_input in ["quote", "inspirational quote"]:
        return "Believe you can and you're halfway there. - Theodore Roosevelt"

    elif user_input in ["advice", "give me advice"]:
        return "Always keep learning and stay curious. The world is full of opportunities."

    elif user_input in ["fun fact", "tell me a fun fact"]:
        return "Did you know? Python is named after the British comedy series 'Monty Python's Flying Circus', not the snake!"

    elif user_input in ["riddle", "tell me a riddle"]:
        return "I speak without a mouth and hear without ears. I have no body, but I come alive with wind. What am I? (Answer: An echo)"

    elif user_input in ["game", "play a game"]:
        return "I can play simple text-based games. Let's play! Type 'rock', 'paper', or 'scissors' to start."

    elif user_input in ["rock", "paper", "scissors"]:
        import random
        choices = ["rock", "paper", "scissors"]
        bot_choice = random.choice(choices)
        if user_input == bot_choice:
            return f"It's a tie! We both chose {bot_choice}."
        elif (user_input == "rock" and bot_choice == "scissors") or \
             (user_input == "paper" and bot_choice == "rock") or \
             (user_input == "scissors" and bot_choice == "paper"):
            return f"You win! I chose {bot_choice}."
        else:
            return f"You lose! I chose {bot_choice}."
        

    elif user_input in ["thank you", "thanks"]:
        return "You're welcome! Happy to help."

    elif user_input in ["bye", "exit", "quit"]:
        return "Goodbye! Have a great day :)"

    else:
        return "Sorry, I didn't understand that. Type 'help' for options."

def start_chatbot():
    print("Bot: Chatbot Started!")
    print("Bot: Type 'help' to see available commands.")
    print("Bot: Type 'bye' to exit.\n")

    while True:
        user_input = input("You: ")
        response = chatbot_response(user_input)
        print("Bot:", response)

        if user_input.lower().strip() in ["bye", "exit", "quit"]:
            break

start_chatbot()
