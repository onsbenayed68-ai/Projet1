from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI()
prompt="Explain what tokenization is. "

instructions = """You are an AI instructor teaching absolute beginners.
Always use simple language and real-world analogies."""

conversation_history = []

while True:
    prompt = input("user: ")

    if prompt == "exit":
        break

    conversation_history.append({
        "role": "user",
        "content": prompt
    })

    response = client.responses.create(
        model="gpt-6-luna",
        input=conversation_history,
        instructions=instructions
    )

    answer = response.output_text

    conversation_history.append({
        "role": "assistant",
        "content": answer
    })

    print("AI :", answer)