from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI()
prompt = "Explain what tokenization is."

instructions = """You are an AI instructor teaching absolute beginners.
Always use simple language and real-world analogies."""

stream = client.responses.create(
    model="gpt-6-luna",
    input=prompt,
    instructions=instructions,
    stream=True,
)

for event in stream:
    if event.type == "response.output_text.delta":
        print(event.delta, end="", flush=True)