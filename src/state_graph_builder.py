from langgraph.graph import StateGraph, ToolNode, START, END
from memory_tools import save_recall_memory, search_recall_memories
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate

def build_graph():
    prompt = ChatPromptTemplate.from_messages([...])
    model = ChatOpenAI(model_name="gpt-4o")
    model_with_tools = model.bind_tools([save_recall_memory, search_recall_memories])

    builder = StateGraph(State)
    builder.add_node("load_memories", load_memories)
    builder.add_node("agent", agent)
    builder.add_node("tools", ToolNode([save_recall_memory, search_recall_memories]))
    builder.add_edge(START, "load_memories")
    builder.add_edge("load_memories", "agent")
    builder.add_conditional_edges("agent", route_tools, ["tools", END])
    builder.add_edge("tools", "agent")
    return builder.compile(checkpointer=MemorySaver())

