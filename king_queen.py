import numpy as up
from sentence_transformers import SentenceTransformer

model= SentenceTransformer("sentence-transformers/all-minilm-l12-v2")

words = [
    "King",
    "Queen",
    "Woman",
    "Main"
]

embedding = model.encode(words)

Queen_embedding = embedding[1]

calculated_embedding = embedding[0] - embedding[3] + embedding[2]
print("similarity:" , up.dot(Queen_embedding , calculated_embedding ))
