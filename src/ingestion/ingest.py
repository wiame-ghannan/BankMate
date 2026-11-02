
from langchain_community.document_loaders import TextLoader,PyPDFLoader,DirectoryLoader,PDFPlumberLoader
from src.core.config import config
loader=DirectoryLoader(
    config.DATA_DIR,
    glob=config.DATA_GLOB,
    loader_cls=PDFPlumberLoader
    )
documents=loader.load()