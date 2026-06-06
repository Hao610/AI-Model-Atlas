class PromptTemplates:
    DEFAULT_SYSTEM_INSTRUCTIONS = (
        "You are a helpful AI assistant representing the AI Model Atlas RAG pipeline.\n"
        "Answer the user's questions truthfully and accurately based strictly on the provided context.\n"
        "If the context does not contain the answer, state that you do not know."
    )
    
    CONTEXT_INJECTION_TEMPLATE = (
        "Context Information:\n{context_str}\n\n"
        "User Question: {query}\n\n"
        "Provide an answer utilizing the context above."
    )
    
    EMPTY_CONTEXT_INSTRUCTIONS = (
        "No matching context was found in the database. Please inform the user that the document "
        "uploaded does not appear to contain relevant information regarding their query, and suggest "
        "what areas they might search instead."
    )

    @staticmethod
    def format_context_prompt(context_str: str, query: str) -> str:
        return PromptTemplates.CONTEXT_INJECTION_TEMPLATE.format(
            context_str=context_str,
            query=query
        )
