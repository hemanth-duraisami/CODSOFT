"""
Rule-Based Chatbot

A simple, beginner-friendly console-based chatbot implemented in Python.
This program uses predefined rules and if-elif-else structures to handle user queries.
No external libraries are required.
"""




def get_response(user_input: str) -> str:
    """
    Determines the chatbot's response based on the user's input.
    Matches are case-insensitive and utilize basic pattern matching with 'if-elif-else'.
    
    Args:
        user_input (str): The raw string entered by the user.

    Returns:
        str: The chatbot's response.
    """
    cleaned_input = user_input.lower().strip()

    punctuation = ".,!?;:"
    normalized_input = "".join(char for char in cleaned_input if char not in punctuation)
    words = normalized_input.split()

    if cleaned_input in ["exit", "quit", "bye", "goodbye"] or any(w in ["exit", "quit", "bye"] for w in words):
        return "Goodbye! Have a wonderful day!"

    elif any(greet in words for greet in ["hi", "hello", "hey", "greetings"]):
        return "Hello! How can I help you today?"

    elif "your name" in cleaned_input or "who are you" in cleaned_input:
        return "I am Chatty, your friendly rule-based chatbot assistant!"

    elif "how are you" in cleaned_input or "how is it going" in cleaned_input or "how's it going" in cleaned_input:
        return "I'm just a program, so I don't have feelings, but I am running perfectly! How are you doing?"

    elif "thank you" in cleaned_input or "thanks" in cleaned_input:
        return "You're very welcome! Is there anything else I can do for you?"

    elif "help" in cleaned_input or "what can you do" in cleaned_input or "commands" in cleaned_input:
        return (
            "I can respond to various questions based on predefined rules!\n"
            "Try asking me one of the following:\n"
            "- Greet me: 'Hello' or 'Hi'\n"
            "- Ask my name: 'What is your name?'\n"
            "- Ask how I am: 'How are you?'\n"
            "- Ask for a joke: 'Tell me a joke'\n"
            "- Ask for a fun fact: 'Tell me a fact'\n"
            "- Thank me: 'Thank you'\n"
            "- Ask for help: 'help'\n"
            "- Exit: Type 'exit', 'quit', or 'bye'"
        )

    elif "joke" in words or any("joke" in w for w in words):
        return "Why don't scientists trust atoms? Because they make up everything!"

    elif "fact" in words or any("fact" in w for w in words):
        return "Did you know? Honey is the only food that never spoils. You can eat 3,000-year-old honey safely!"

    else:
        return "I'm sorry, I didn't quite catch that. Type 'help' to see a list of things you can ask me!"


def main():
    """
    Main function to run the console chatbot.
    Greets the user, runs the conversational loop, and exits gracefully.
    """
    print("==================================================")
    print("           Welcome to Rule-Based Chatbot!         ")
    print("==================================================")
    print("Chatty: Hello! I am a rule-based chatbot.")
    print("Chatty: Type 'help' to see what I can do, or 'exit' to end our chat.")
    print("-" * 50)

    while True:
        try:
            user_input = input("You: ")
        except (KeyboardInterrupt, EOFError):
            print("\nChatty: Goodbye! Have a wonderful day!")
            break

        response = get_response(user_input)
        
        print(f"Chatty: {response}")
        print("-" * 50)

        if user_input.lower().strip() in ["exit", "quit", "bye", "goodbye"]:
            break


if __name__ == "__main__":
    main()
