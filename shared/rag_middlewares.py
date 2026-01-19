from langchain.agents.middleware import dynamic_prompt, ModelRequest, after_model, AgentState
from shared.vector_store_config import vector_store
from langgraph.runtime import Runtime
from typing import Any

@dynamic_prompt
def prompt_with_context(request: ModelRequest) -> str:
    """Inject context into state message"""
    print("Tool call: prompt_with_context")
    last_query = request.state["messages"][-1].text
    retrieved_docs = vector_store.similarity_search(last_query)
    docs_content = "\n\n".join(doc.page_content for doc in retrieved_docs)
    system_message = (
        "You are a helpful assistant. Use the following context in your response:"
        f"\n\n{docs_content}"
    )
    return system_message

@after_model
def log_response(state: AgentState, runtime: Runtime) -> dict[str, Any] | None:
    print(f"Model returned: Response")
    return state
    