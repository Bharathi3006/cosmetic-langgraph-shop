from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from database import get_all_products, search_products
from agent import run_agent

app = FastAPI(title="Cosmetic LangGraph Shop API")

# Allow CORS for frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, replace with specific domain
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class ChatRequest(BaseModel):
    message: str

@app.get("/")
def read_root():
    return {"message": "Welcome to the Cosmetic Shop API with LangGraph"}

@app.get("/api/products")
def get_products():
    return get_all_products()

@app.get("/api/products/search")
def search_products_endpoint(q: str):
    return search_products(q)

@app.post("/api/chat")
def chat_endpoint(request: ChatRequest):
    try:
        response = run_agent(request.message)
        return {"response": response}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
