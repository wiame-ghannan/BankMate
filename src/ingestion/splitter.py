from langchain_text_splitters import RecursiveCharacterTextSplitter
from src.ingestion.ingest import documents
from src.core.config import config

text_splitter=RecursiveCharacterTextSplitter(
    chunk_size=config.CHUNK_SIZE,
    chunk_overlap=config.CHUNK_OVERLAP
)
chunks=text_splitter.split_documents(documents)
