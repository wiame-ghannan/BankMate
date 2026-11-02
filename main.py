from fastapi import FastAPI
import gradio as gr

from src.api.chat_router import router
from src.ui.gradio_app import demo

app = FastAPI()
app.include_router(router)

app = gr.mount_gradio_app(app, demo, path="/")