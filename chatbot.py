from openai import OpenAI

client= OpenAI(
    api_key="your_api_key_here",
    base_url="https://api.groq.com/openai/v1"
)
while True:
    user_input = input("You: ")

    if user_input.lower() in ["quit", "exit", "bye"]:
        print("Bot: Goodbye!")
        break

    response = client.chat.completions.create(
        model="llama3-70b-8192",
        messages=[
            {
                "role": "system",
                "content": (
                    "You are an expert coding assistant. You can write and explain code in any programming language. "
                    "If the user does not specify a language, respond with Python by default. "
                    "If the user requests a specific language (e.g., C, C++, Java, JavaScript, C#, etc.), respond in that language. "
                    "Always provide accurate, clear, and well-explained code suited to the user's request or problem."
                )
            },
            {
                "role": "user",
                "content": user_input
            }
        ]
    )

    print("Bot:", response.choices[0].message.content,"\n")
