
from fastapi import FastAPI
from src.api.chat_router import router

app = FastAPI()
app.include_router(router)


