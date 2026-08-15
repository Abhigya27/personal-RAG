from langchain_huggingface import HuggingFaceEmbeddings

embedder = HuggingFaceEmbeddings(model_name="BAAI/bge-small-en-v1.5")

def get_embedding(text):
    return embedder.embed_query(text)