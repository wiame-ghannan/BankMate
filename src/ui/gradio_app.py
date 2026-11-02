import gradio as gr
from src.chat.rag import ask_question


def respond(message: str, history: list) -> str:
    return ask_question(message)


demo = gr.ChatInterface(
    fn=respond,
    title="BankMate — Corvelle Bank Assistant",
    description="Ask questions about Corvelle Bank accounts, cards, fees, loans and savings. Answers are based on official bank documents.",
    examples=[
        "What is the annual fee of the Gold card?",
        "What should I do if my card is stolen?",
        "What is the interest rate for a 48-month personal loan?",
    ],
)