
import colorama
import nltk
from colorama import Fore, Style
from textblob import TextBlob

# Download required NLTK resources
nltk.download("punkt")
nltk.download("averaged_perceptron_tagger")

# Initialize Colorama
colorama.init(autoreset=True)

# Welcome message
print(f"{Fore.CYAN}🕵️ Welcome to Sentiment Spy! 🕵️")

user_name = input(
    f"{Fore.MAGENTA}Please enter your name: {Style.RESET_ALL}"
).strip()

if not user_name:
    user_name = "Mystery Agent"

# Store conversation history
conversation_history = []

print(f"\n{Fore.CYAN}Hello, Agent {user_name}!")
print(
    "Type a sentence and I will analyze it using TextBlob "
    "and show you its sentiment. 🔍"
)

print(
    f"Type {Fore.YELLOW}'reset'{Fore.CYAN}, "
    f"{Fore.YELLOW}'history'{Fore.CYAN}, "
    f"or {Fore.YELLOW}'exit'{Fore.CYAN} to quit.\n"
)

while True:
    user_input = input(f"{Fore.GREEN}>> {Style.RESET_ALL}").strip()

    # Handle empty input
    if not user_input:
        print(
            f"{Fore.RED}Please enter some text or a valid command."
        )
        continue

    # Exit command
    if user_input.lower() == "exit":
        print(
            f"\n{Fore.BLUE}👋 Exiting Sentiment Spy. "
            f"Farewell, Agent {user_name}! 🕵️"
        )
        break

    # Reset command
    elif user_input.lower() == "reset":
        conversation_history.clear()
        print(f"{Fore.CYAN}🧹 All conversation history cleared!")
        continue

    # History command
    elif user_input.lower() == "history":
        if not conversation_history:
            print(f"{Fore.YELLOW}No conversation history yet.")
        else:
            print(f"{Fore.CYAN}📜 Conversation History:")

            for idx, (text, polarity, sentiment_type) in enumerate(
                conversation_history, start=1
            ):
                if sentiment_type == "Positive":
                    color = Fore.GREEN
                    emoji = "😊"
                elif sentiment_type == "Negative":
                    color = Fore.RED
                    emoji = "😞"
                else:
                    color = Fore.YELLOW
                    emoji = "😐"

                print(
                    f"{idx}. {color}{emoji} {text} "
                    f"(Polarity: {polarity:.2f}, "
                    f"{sentiment_type}){Style.RESET_ALL}"
                )

        continue

    # Analyze sentiment
    polarity = TextBlob(user_input).sentiment.polarity

    if polarity > 0.25:
        sentiment_type = "Positive"
        color = Fore.GREEN
        emoji = "😊"

    elif polarity < -0.25:
        sentiment_type = "Negative"
        color = Fore.RED
        emoji = "😞"

    else:
        sentiment_type = "Neutral"
        color = Fore.YELLOW
        emoji = "😐"

    # Save result to conversation history
    conversation_history.append(
        (user_input, polarity, sentiment_type)
    )

    # Display sentiment result
    print(
        f"{color}{emoji} {sentiment_type} sentiment detected! "
        f"(Polarity: {polarity:.2f}){Style.RESET_ALL}"
    )
