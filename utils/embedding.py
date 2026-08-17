from fastembed import TextEmbedding

embedder = TextEmbedding(model_name="BAAI/bge-small-en-v1.5")

def get_embedding(text):
    return list(embedder.embed([text]))[0]