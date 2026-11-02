import os
from src.retriever.retrievel import retriever
from src.prompts.main_prompt import prompt_template
from src.llms.openai import llm

NO_ANSWER = "I don't have this information"


def ask_question(question: str) -> str:
    retrieved_docs = retriever.invoke(question)
    context = "\n\n".join(document.page_content for document in retrieved_docs)

    messages = prompt_template.format_messages(
        context=context,
        question=question
    )
    response = llm.invoke(messages)
    answer = response.content

    # Pas de sources si l'assistant n'a pas trouvé la réponse
    if NO_ANSWER in answer:
        return answer

    sources = sorted({
        f"{os.path.basename(doc.metadata['source'])}, page {doc.metadata.get('page', 0) + 1}"
        for doc in retrieved_docs
    })
    sources_text = "\n".join(f"{s}" for s in sources)

    return f"{answer}\n\n**Sources:**\n{sources_text}"