from src.ingestion.vector_store import vector_store
from src.core.config import config

retriever = vector_store.as_retriever(search_type=config.SEARCH_TYPE, search_kwargs={"k": config.RETRIEVER_K})