from langchain_openai import ChatOpenAI
from src.core.config import config
llm = ChatOpenAI(
    model=config. OPENAI_MODEL,
    api_key=config.OPENAI_API_KEY
)