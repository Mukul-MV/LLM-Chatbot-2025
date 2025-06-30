from langchain_community.llms import Ollama
from langchain.retrivers import create_history_aware_retriever
from langchain.chains import create_retrieval_chain,create_stuff_documents_chain

def get_rag_chain(model = "llama3.1"):
    llm = Ollama(model)

    # Assume 'retriever' is created from chroma_utils (not shown here)
    history_aware_retriver = create_history_aware_retriever(llm,retriever,contextualize_q_prompt)
    question_answer_chain = create_stuff_documents_chain(llm,qa_prompt)
    rag_chain = create_retrieval_chain(history_aware_retriver,question_answer_chain)

    return rag_chain

