from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from langserve import add_routes
from trials.modelinvocation import agent

app = FastAPI(
    title="RAG Agent API",
    description="Local RAG agent with streaming support"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],        # Agent UI requires wildcard OR explicit URLs
    allow_origin_regex=".*",    # Required for websocket upgrades!
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Disable API key requirement
add_routes(
    app, 
    agent, 
    path="/rag",
)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=2024)
