import os
from google import genai
from google.genai import types
from dotenv import load_dotenv

# Load API key from .env file
load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

# Check API key
if not api_key:
    print("Error: Gemini API key not found!")
    print("Please check your .env file.")
    exit()

# Connect to Gemini AI
client = genai.Client(api_key=api_key)

# Create chatbot with conversation memory
chat = client.chats.create(
    model="gemini-flash-latest",
    config=types.GenerateContentConfig(
        system_instruction=(
            "You are a professional AI customer support assistant. "
            "Greet customers politely. "
            "Answer questions clearly and simply. "
            "Help with orders, payments, refunds, returns and delivery. "
            "If you do not know an answer, say so honestly. "
            "Never invent order details or payment information."
        )
    )
)

print("=" * 45)
print("   AI CUSTOMER SUPPORT CHATBOT")
print("=" * 45)
print("Welcome! How can I help you today?")
print("Type 'exit' to close the chatbot.")
print("-" * 45)

# Chatbot conversation
while True:

    user_input = input("\nYou: ").strip()

    if not user_input:
        print("Chatbot: Please enter your question.")
        continue

    if user_input.lower() == "exit":
        print("\nChatbot: Thank you for contacting us!")
        print("Have a great day. Goodbye!")
        break

    try:
        response = chat.send_message(user_input)

        print("\nChatbot:", response.text)

    except Exception as e:
        print("\nChatbot: Sorry, something went wrong.")
        print("Error:", e)