from langchain_openai import OpenAIEmbeddings
from src.core.config import config
from src.ingestion.splitter import chunks

Embeddings=embeddings = OpenAIEmbeddings(
    model=config.EMBEDDING_MODEL,
    openai_api_key=config.OPENAI_API_KEY
    )

