import os
# pyrefly: ignore [missing-import]
from dotenv import load_dotenv
# pyrefly: ignore [missing-import]
from groq import Groq

# 1. Load the environment variables from your .env file
load_dotenv()
api_key = os.getenv("GROQ_API_KEY")

if not api_key:
    print("❌ Error: GROQ_API_KEY not found. Please check your .env file.")
    exit(1)

print("✅ API Key loaded successfully!")
print("⏳ Connecting to Groq...\n")

try:
    # 2. Initialize the Groq client
    client = Groq(api_key=api_key)

    # 3. Make a simple test request using a fast LLaMA model
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": "Hello! Please reply with strictly 'Groq is working perfectly!'"
            }
        ],
        model="llama3-8b-8192", 
    )

    # 4. Print the response from the AI
    print("🤖 --- AI Response ---")
    print(chat_completion.choices[0].message.content)
    print("----------------------\n")
    print("🎉 Day 1 is 100% Complete!")

except Exception as e:
    print(f"❌ An error occurred: {e}")
