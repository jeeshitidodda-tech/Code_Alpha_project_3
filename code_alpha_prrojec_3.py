import random
from datetime import datetime


# Function for chatbot responses
def chatbot_response(user_input):

    user_input = user_input.lower()

    greetings = ["hello", "hi", "hey"]
    exit_words = ["bye", "exit", "quit"]

    jokes = [
        "Why did the computer get cold? Because it forgot to close Windows.",
        "Why was the Python developer calm? Because he handled every exception.",
        "Why do programmers hate nature? Too many bugs."
    ]

    motivation_quotes = [
        "Success starts with consistency.",
        "Your future is created by what you do today.",
        "Small steps every day lead to big achievements."
    ]

    movies = [
        "Interstellar",
        "Inception",
        "3 Idiots",
        "The Dark Knight",
        "Bahubali"
    ]

    if user_input in greetings:
        return "Welcome to CineBot. Ready for some fun conversations?"

    elif "how are you" in user_input:
        return "I'm functioning perfectly and ready to chat."

    elif "your name" in user_input:
        return "I am CineBot, your entertainment assistant."

    elif "movie" in user_input:
        return f"You should watch: {random.choice(movies)}"

    elif "joke" in user_input:
        return random.choice(jokes)

    elif "motivate" in user_input:
        return random.choice(motivation_quotes)

    elif "sad" in user_input:
        return "Bad days are temporary. Keep moving forward."

    elif "happy" in user_input:
        return "That's great to hear. Happiness looks good on everyone."

    elif "time" in user_input:
        current_time = datetime.now().strftime("%I:%M %p")
        return f"Current time is {current_time}"

    elif "game" in user_input:
        number = random.randint(1, 5)

        guess = int(input("Guess a number between 1 and 5: "))

        if guess == number:
            return "Correct guess. You won the game."
        else:
            return f"Wrong guess. The correct number was {number}"

    elif user_input in exit_words:
        return "Session ended. Have a great day."

    else:
        return "I do not understand that command yet."


# Main Program
print("===================================")
print("       Welcome to CineBot")
print("===================================")
print("Type 'bye' anytime to exit.")
print()

while True:

    user_message = input("You: ")

    response = chatbot_response(user_message)

    print("CineBot:", response)

    if user_message.lower() in ["bye", "exit", "quit"]:
        break