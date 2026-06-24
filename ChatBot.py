"""
Basic Rule-Based Chatbot
--------------------------
CodeAlpha Internship - Python Programming
Task: Build a simple rule-based chatbot that replies to predefined
user inputs like greetings, questions, and goodbyes.

Author: [Your Name]
"""

import random


def get_response(user_input):
    """
    Takes the user's message, checks it against known patterns,
    and returns an appropriate reply.
    """
    # Convert to lowercase so the chatbot understands
    # "Hello", "HELLO", "hello" all the same way.
    text = user_input.lower().strip()

    # ---------------- Greetings ----------------
    if text in ["hello", "hi", "hey"]:
        return random.choice(["Hi!", "Hello there!", "Hey, good to see you!"])

    # ---------------- How are you ----------------
    elif "how are you" in text:
        return "I'm fine, thanks! How about you?"

    elif text in ["i am fine", "i'm fine", "i am good", "i'm good"]:
        return "Glad to hear that!"

    # ---------------- Name ----------------
    elif "your name" in text:
        return "I'm a simple chatbot made in Python!"

    elif "my name is" in text:
        name = text.split("is")[-1].strip().title()
        return f"Nice to meet you, {name}!"

    # ---------------- Help ----------------
    elif "help" in text:
        return "I can chat about basic things. Try saying hello, how are you, or bye."

    # ---------------- Thanks ----------------
    elif text in ["thanks", "thank you"]:
        return "You're welcome!"

    # ---------------- Goodbye ----------------
    elif text in ["bye", "goodbye", "see you"]:
        return "Goodbye! Take care."

    # ---------------- Default ----------------
    else:
        return "Sorry, I didn't understand that. Can you rephrase?"


def chat():
    """
    Runs the main chat loop. Keeps asking for input until the
    user says a goodbye keyword.
    """
    print("=" * 50)
    print("Welcome! I'm a basic chatbot. Type 'bye' to exit.")
    print("=" * 50)

    while True:
        user_input = input("You: ")

        # Don't let the bot crash on empty input
        if user_input.strip() == "":
            print("Bot: Please type something.")
            continue

        response = get_response(user_input)
        print(f"Bot: {response}")

        # End the loop if the user said a goodbye word
        if user_input.lower().strip() in ["bye", "goodbye", "see you"]:
            break


# Run the chatbot
if __name__ == "__main__":
    chat()