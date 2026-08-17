import streamlit as st
from utils.embedding import get_embedding
from utils.chunking import chunk_text
from utils.retrieval import load_faiss_index, retrieve_chunks
from utils.prompt import build_prompt
from utils.call import generate_chat

st.title("Ask Abhigya")
st.write("Ask questions about Abhigya Narain")

query = st.text_input("enter your question")

if query:
    index, chunk_mapping = load_faiss_index()
    top_chunks = retrieve_chunks(query, index, chunk_mapping)

    prompt = build_prompt(top_chunks, query)

    st.subheader("Answer")
    st.write_stream(generate_chat(prompt))

    with st.expander("Retrieved Chunks"):
        for chunk in top_chunks:
            st.markdown(f"- {chunk}")