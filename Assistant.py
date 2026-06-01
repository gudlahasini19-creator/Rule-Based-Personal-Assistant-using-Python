import datetime
import webbrowser
import pyttsx3

# Initialize Text-to-Speech
engine = pyttsx3.init()

def speak(text):
    """Convert text to speech."""
    engine.say(text)
    engine.runAndWait()

def get_response(user_input):
    """Match user input to a command and return a response."""
    command = user_input.lower().strip()

    # Greetings
    if command in ["hello", "hi", "hey"]:
        return "Hello! I'm your personal assistant. Type help to see what I can do."

    # Tell time
    elif "time" in command:
        now = datetime.datetime.now()
        return f"The current time is {now.strftime('%I:%M %p')}."

    # Tell date
    elif "date" in command:
        today = datetime.datetime.now()
        return f"Today's date is {today.strftime('%A, %B %d, %Y')}."

    # Open browser
    elif "open browser" in command or "open google" in command:
        webbrowser.open("https://www.google.com")
        return "Opening Google in your browser."

    # Play music
    elif "play music" in command:
        webbrowser.open("https://music.youtube.com")
        return "Opening YouTube Music. Enjoy!"

    # Joke
    elif "joke" in command:
        return "Why do programmers prefer dark mode? Because light attracts bugs."

    # Calculator
    elif "calculate" in command or "calculator" in command:
        webbrowser.open("https://www.google.com/search?q=calculator")
        return "Opening calculator in your browser."

    # Weather
    elif "weather" in command:
        webbrowser.open("https://www.google.com/search?q=weather+today")
        return "Opening weather information in your browser."

    # Help Menu
    elif command == "help":
        return (
            "\nAvailable Commands:\n"
            "hello / hi / hey  -> Greet the assistant\n"
            "time              -> Get current time\n"
            "date              -> Get today's date\n"
            "open browser      -> Open Google\n"
            "play music        -> Open YouTube Music\n"
            "joke              -> Hear a joke\n"
            "calculate         -> Open calculator\n"
            "weather           -> Check weather\n"
            "quit / exit       -> Close assistant"
        )

    # Exit
    elif command in ["quit", "exit", "bye"]:
        return "EXIT"

    # Unknown command
    else:
        return f"Sorry, I don't understand '{user_input}'. Type help to see available commands."


def main():
    print("=" * 55)
    print("🤖 Rule-Based Personal Assistant")
    print("=" * 55)
    print("Type 'help' to see commands. Type 'quit' to exit.\n")

    speak("Hello! I am your personal assistant. Type help to see available commands.")

    while True:
        user_input = input("You: ").strip()

        if not user_input:
            continue

        response = get_response(user_input)

        if response == "EXIT":
            goodbye = "Goodbye! Have a great day."
            print(f"Assistant: {goodbye}")
            speak(goodbye)
            break

        print(f"Assistant: {response}\n")
        speak(response)


if __name__ == "__main__":
    main()