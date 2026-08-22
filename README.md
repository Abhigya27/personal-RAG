# Personal RAG

A prototype **Retrieval-Augmented Generation (RAG)** application designed to answer questions about me using my personal information as the knowledge base.

The project implements the core RAG workflow: converting personal information into vector embeddings, storing and searching those embeddings, retrieving relevant context for a query, and using an LLM to generate a context-aware response.

> **Note:** This is currently a prototype and learning project. It is intended to serve as a foundation for a more capable personal AI system that will gradually incorporate features such as job-description matching, memory, improved retrieval, and agentic capabilities.

---

## Features

- Ask questions about information stored in a personal knowledge base
- Generate vector embeddings for semantic search
- Retrieve relevant information based on a user's query
- Use retrieved context to generate more grounded LLM responses
- Simple application interface

---

## How It Works

The application follows a basic RAG pipeline:

```text
Personal Information
        │
        ▼
   Text Processing
        │
        ▼
  Embedding Model
        │
        ▼
   FAISS Vector Store
        │
        ▲
        │
     User Query
        │
        ▼
  Query Embedding
        │
        ▼
 Relevant Context
        │
        ▼
       LLM
        │
        ▼
   Final Response
```

Instead of relying entirely on the LLM's existing knowledge, the system retrieves relevant information from the personal knowledge base and provides that context to the model before generating a response.

---

## Tech Stack

### Current Version

- **Python**
- **Streamlit** — User interface
- **FAISS** — Vector similarity search
- **Sentence Transformers** — Text embeddings
- **Groq** — LLM inference

### Planned / Future Technologies

- **LangChain** — For building and managing more advanced RAG pipelines
- Additional memory and retrieval components
- Potential agent and tool integrations

---

## Current Status

This repository represents an **early prototype and proof of concept**.

The current version focuses on implementing and understanding the fundamental components of a RAG application, including embeddings, vector similarity search, context retrieval, and LLM-based response generation.

The project is intentionally being developed incrementally. More advanced abstractions and features will be introduced as the project evolves.

---

# Planned Features

## 🎯 JD Matcher

A job-description matching feature that compares my profile, skills, projects, and experience against a given job description.

Potential functionality includes:

- Identifying matching skills
- Identifying missing or weak skills
- Comparing project experience with role requirements
- Generating a match summary
- Suggesting areas for improvement

---

## 🧠 Persistent Memory

Allow the system to retain useful information and context across conversations instead of treating every interaction independently.

This could enable the assistant to gradually build a more useful understanding of relevant user information and preferences.

---

## 💬 Conversational Memory

Maintain context during a conversation so that follow-up questions can be understood naturally.

For example:

> "What projects have I worked on?"

followed by:

> "Which one is most relevant for an AI Engineer role?"

The system should understand the context of the second question.

---

## 🔍 Improved Retrieval

Experiment with more advanced retrieval techniques, including:

- Better chunking strategies
- Metadata filtering
- Hybrid search
- Reranking
- Query rewriting
- Multi-query retrieval

---

## 📚 Dynamic Knowledge Base

Allow new information and documents to be added dynamically instead of relying on a fixed personal dataset.

Potential sources could include:

- Resume
- Project documentation
- Skills and experience
- Notes
- Other personal or professional documents

---

## 📊 RAG Evaluation

Add an evaluation pipeline to measure:

- Retrieval quality
- Context relevance
- Answer relevance
- Faithfulness of generated responses

This will help improve the reliability and performance of the system.

---

## 🦜 LangChain Integration

Future versions may use **LangChain** to help structure and manage more advanced components of the application, including retrieval pipelines, document processing, memory, chains, and integrations.

The current prototype is intentionally kept closer to the underlying RAG components to better understand how the system works before introducing additional abstractions.

---

## 🤖 Agentic Capabilities

Experiment with AI agents and tools that allow the system to perform tasks beyond simple question answering.

Potential capabilities may include:

- Selecting appropriate tools
- Searching different knowledge sources
- Performing multi-step tasks
- Combining retrieval with external tools

---

## 🎨 Improved User Interface

Improve the current interface with additional features and a more polished user experience.

---

# Project Goal

The long-term goal is to turn this prototype into a **personal AI assistant powered by Retrieval-Augmented Generation**.

The assistant will gradually evolve to understand and retrieve information related to my:

- Professional background
- Technical skills
- Projects
- Resume
- Experience
- Documents
- Other relevant knowledge

The system will eventually combine **RAG, memory, retrieval optimization, evaluation, and potentially agentic workflows** to provide more contextual and personalized responses.

---

## Concepts Explored

This project is being used to learn and experiment with:

- Retrieval-Augmented Generation (RAG)
- Embeddings
- Vector similarity search
- FAISS
- Semantic search
- LLM APIs
- Context augmentation
- Prompt construction

Future iterations will additionally explore:

- LangChain
- Advanced retrieval
- Memory systems
- RAG evaluation
- AI agents and tool use

---

## Running Locally

### 1. Clone the repository

```bash
git clone https://github.com/Abhigya27/personal-RAG.git
cd personal-RAG
```

### 2. Install dependencies

If you are using `uv`:

```bash
uv sync
```

### 3. Configure environment variables

Create a `.env` file and add your required API key:

```env
GROQ_API_KEY=your_key_here
```

### 4. Run the application

```bash
streamlit run app.py
```

---

## Disclaimer

This project is primarily built for learning and experimentation. The current implementation is a prototype, and the architecture, technologies, and features may change significantly as the project evolves.
