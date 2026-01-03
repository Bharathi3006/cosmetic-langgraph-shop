from typing import TypedDict, List
from langgraph.graph import StateGraph, END
from typing import Annotated
import operator
from database import search_products, get_all_products

# Since we don't have a real LLM API key configured for this environment usually,
# We will simulate the LLM's decision making logic with rule-based heuristics for this demo.
# If an API key were available, we would use ChatOpenAI or similar.

class AgentState(TypedDict):
    messages: List[str]
    context: List[dict]
    final_response: str

def understand_intent(state: AgentState):
    """
    Simulates an LLM analyzing the user's last message to determine intent.
    """
    last_message = state["messages"][-1].lower()
    
    # Simple keyword detection
    search_keywords = ["looking for", "buy", "recommand", "need", "want", "search", "find", "show me"]
    greeting_keywords = ["hi", "hello", "hey"]
    
    intent = "chat"
    query = ""
    
    if any(k in last_message for k in greeting_keywords):
        intent = "greeting"
    elif any(k in last_message for k in search_keywords) or "?" in last_message:
        intent = "search"
        # Extract potential query (very naive)
        query = last_message
    
    return {"intent": intent, "query": query}

def retriever_node(state: AgentState):
    """
    Retrieves products based on the query.
    """
    # We need to pass the query from the previous step, but state is immutable in structure 
    # typically in these functions unless we update it. 
    # For this simple graph, let's just re-parse or rely on context.
    
    last_message = state["messages"][-1]
    results = search_products(last_message)
    
    # Update context with results
    return {"context": results}

def generator_node(state: AgentState):
    """
    Generates a response based on context and messages.
    """
    context = state.get("context", [])
    last_message = state["messages"][-1].lower()
    
    if not context:
        if "hi" in last_message or "hello" in last_message:
             response = "Hello! Welcome to our Cosmetic Shop. I am your AI Beauty Advisor. How can I help you sparkle today?"
        else:
            response = "I'm not sure I have that specific item, but I can help you find lipsticks, eyeliners, or brushes! Try asking for 'lipstick' or 'brushes'."
    else:
        product_names = ", ".join([p["name"] for p in context[:3]])
        response = f"I found some fabulous items for you: {product_names}. Would you like to know more about any of them?"
        
    return {"final_response": response}

# Define the Graph
workflow = StateGraph(AgentState)

# Add nodes
workflow.add_node("generator", generator_node)
# In a real LangGraph, we would have a conditional edge to a retriever.
# To keep this "simulated" but structured like a graph:
workflow.add_node("retriever", retriever_node)

# We'll use a simple linear flow for this demo: 
# Input -> Retriever (always tries to find stuff) -> Generator
workflow.set_entry_point("retriever")
workflow.add_edge("retriever", "generator")
workflow.add_edge("generator", END)

# Compile
app = workflow.compile()

def run_agent(message: str):
    inputs = {"messages": [message], "context": [], "final_response": ""}
    result = app.invoke(inputs)
    return result["final_response"]
