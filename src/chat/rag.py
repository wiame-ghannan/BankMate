from src.retriever.retrievel import retriever
from src.prompts.main_prompt import prompt_template
from src.llms.openai import llm

def ask_question(question: str) -> str:
        
    retrieved_docs = retriever.invoke(question)
    context = "\n\n".join(document.page_content for document in retrieved_docs)


    formatted_prompt = prompt_template.format(
        context=context,
        question=question
    )

    response = llm.invoke(formatted_prompt)
    return response.content