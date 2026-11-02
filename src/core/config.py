import os
from dotenv import load_dotenv

load_dotenv()

class Config: 
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
    OPENAI_MODEL = "gpt-6-luna"
    
    # Embeddings
    EMBEDDING_MODEL = "text-embedding-3-small"
    
    # Document loading
    DATA_DIR = "data/"
    DATA_GLOB = "**/*.pdf"

    # Text splitting
    CHUNK_SIZE = 800
    CHUNK_OVERLAP = 100
    
    # Vector store
    CHROMA_PERSIST_DIRECTORY = "data/chroma_db"
    
    # Retrieval
    SEARCH_TYPE = "similarity"
    RETRIEVER_K = 3
    
config = Config()    