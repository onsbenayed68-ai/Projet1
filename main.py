import tiktoken 

enc = tiktoken.encoding_for_model("gpt-5-nano-2025-08-07")

tokens = enc.encode("Hello, World!")
text= enc.decode(tokens)

print("tokens:", tokens)
print("text:", text)