# Rule-Based Chatbot

This is a simple console-based chatbot built using Python as part of the **CODSOFT AI Internship**. The chatbot responds to user inputs using predefined rules and basic pattern matching with `if-else` conditions.

It is a beginner-friendly project that demonstrates how conversational flow can be implemented without using any machine learning or external libraries.

## About the Project

The chatbot takes user input and processes it by matching keywords and patterns. Based on the input, it returns an appropriate response such as greetings, jokes, facts, or general help messages.

This project helps in understanding the basics of **natural language processing concepts** and **rule-based systems**.

## Features

* Responds to greetings like "hello", "hi", "hey"
* Answers basic questions like "how are you?" and "what is your name?"
* Provides jokes and fun facts
* Displays help instructions for users
* Handles exit commands like "bye", "exit", or "quit"
* Runs continuously until the user exits

## Technologies Used

* Python 3

## Project Structure

```text
RuleBasedChatbot/
├── chatbot.py
└── README.md
```

## How to Run

1. Make sure Python 3 is installed on your system.
2. Open terminal in the project folder.
3. Run the program using:

```bash
python chatbot.py
```

4. Start chatting by typing messages.
5. Type `exit`, `quit`, or `bye` to close the chatbot.

## Example Interaction

```text
You: hello
Chatty: Hello! How can I help you today?

You: tell me a joke
Chatty: Why don't scientists trust atoms? Because they make up everything!

You: what is your name?
Chatty: I am Chatty, your friendly rule-based chatbot assistant!

You: bye
Chatty: Goodbye! Have a wonderful day!
```

## Logic Overview

* User input is converted to lowercase and cleaned
* Keywords are matched using `if-elif-else` conditions
* Responses are returned based on detected patterns
* Default response is shown for unknown inputs

## Future Improvements

* Add machine learning-based responses
* Improve natural language understanding
* Store chat history
* Build a GUI using Tkinter or a web interface

## Author

Developed as part of the **CODSOFT AI Internship**
