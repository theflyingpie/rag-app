#!/Users/sophiasunkin/code/rag-app/.venv/bin/python
import os
from llama_index.core.ingestion import IngestionPipeline, IngestionCache
from llama_index.core.query_pipeline import QueryPipeline
from llama_index.core import VectorStoreIndex, SimpleDirectoryReader, Settings
from llama_index.cli.rag import RagCLI
from llama_index.llms.ollama import Ollama
from llama_index.embeddings.huggingface import HuggingFaceEmbedding



Settings.embed_model = HuggingFaceEmbedding(model_name="BAAI/bge-base-en-v1.5")
Settings.llm = Ollama(model="llama2", request_timeout=360.0)

documents = SimpleDirectoryReader("data").load_data()
index = VectorStoreIndex.from_documents(documents)  # No docstore, just embeddings

vec_store = index.vector_store

custom_ingestion_pipeline = IngestionPipeline(
    transformations=[],
    vector_store=vec_store,
    cache=IngestionCache(),
)


query_pipeline = QueryPipeline()

query_engine = index.as_query_engine(llm=Settings.llm)

chat_engine = index.as_chat_engine(chat_mode="condense_question")


rag_cli_instance = RagCLI(
    ingestion_pipeline=custom_ingestion_pipeline,
    query_pipeline=query_pipeline,
    query_engine=query_engine,
    chat_engine=chat_engine,
)

if __name__ == "__main__":
    rag_cli_instance.cli()