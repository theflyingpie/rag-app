# RAG App Documentation

## Overview

Here are setup instructions, rationale behind tool choices, and the development process for the CLI-based RAG application. The app is designed to be lightweight and run locally using the LlamaIndex library.

---

## Setup Instructions

### Requirements

- MacOS (Development environment)
- Python 3.x
- Pip (Python package installer)

### Installation

To install all necessary dependencies, run the following commands in the project directory:

```bash
pip install -U llama-index
pip install llama-index-vector-stores-chroma
pip install llama-index-llms-ollama
pip install llama-index-embeddings-huggingface
```

### Downloading LLama2

I chose to use LLama2 because its performance is comparable to other leading models (including GPT-4) and it is open-source.
To download LLama2, run:

```bash
ollama pull llama2
```

### Making `rag.py` Executable

1. Replace the first line of `rag.py` with the output of running:

```bash
which python
```

2. Make the script executable:

```bash
chmod +x rag.py
```

3. Add the script to your PATH:

```bash
export PATH="/Users/sophiasunkin/code/rag-app/rag.py:$PATH"
```

### Running the App

To verify the CLI works, run:

```bash
rag.py -h
```

To ask a question:

```bash
python rag.py rag -q "YOUR-QUESTION-HERE"
```

---

## Framework/Tools Choices

### Why I Chose These Tools

- **LlamaIndex:** Optimized for indexing and retrieving data efficiently.
- **LLama2 (via Ollama):** Open-source model with performance on par with GPT-4, providing a high-quality LLM without requiring API calls to external services.
- **RAG CLI:** Simplifies the implementation of a local RAG application with minimal setup and high efficiency.

### What Worked

- Using `VectorStoreIndex.from_documents(documents).vector_store` as a simple solution for vector storage.
- Implementing a chat engine using:

```python
chat_engine = index.as_chat_engine(chat_mode="condense_question")
```

### What Didn't Work & How I Dealt With It

- Initial attempts to use `docstore` were unnecessary since the app does not require persistent document storage.
- Trying `docarray` for `vec_store` compatibility failed, so I opted to use `VectorStoreIndex` instead.
- `FAISS` was considered but was too time-consuming to set up, so I went with a built-in vector store solution.
- I encountered a `Nonetype has no attribute 'chat'` error due to a missing chat engine, which was resolved by adding a compatible chat engine.

---

## Potential Improvements

If I had more time, I would:

- **Add Chat History:** Make the app remember and build upon previous queries.
- **Implement History Management:** Allow clearing or saving history as needed.
- **Testing:** Add unit tests to ensure reliability.

