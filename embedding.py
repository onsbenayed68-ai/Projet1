from sentence_transformers import SentenceTransformer

model= SentenceTransformer("sentence-transformers/all-minilm-l12-v2")

sentences = [
    "The weather is lovely today.",
    "It's so sunny outside!",
    "He drove to the stadium.",
]
embeddings = model.encode(sentences)
print("embedding:", embeddings)

