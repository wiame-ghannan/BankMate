import os
from langchain_chroma import Chroma
from src.ingestion.splitter import chunks
from src.ingestion.embeddings import Embeddings
from src.core.config import config

if os.path.exists(config.CHROMA_PERSIST_DIRECTORY):
    vector_store = Chroma(
        persist_directory=config.CHROMA_PERSIST_DIRECTORY,
        embedding_function=Embeddings,
    )
else:
    vector_store = Chroma.from_documents(
        documents=chunks,
        embedding=Embeddings,
        persist_directory=config.CHROMA_PERSIST_DIRECTORY,
    )