"""
FastAPI Backend for Video Creator Agent
Connects the web interface to the Python agent
"""

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import sys
import os
from typing import Optional

# Add parent directory to path to import agent
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

try:
    from agent import run_agent
    AGENT_AVAILABLE = True
except ImportError as e:
    print(f"Warning: Could not import agent: {e}")
    AGENT_AVAILABLE = False

# Initialize FastAPI app
app = FastAPI(
    title="Video Creator AI API",
    description="AI-powered content creation and task automation",
    version="1.0.0"
)

# Enable CORS for all origins (restrict in production)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, specify exact origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Request/Response models
class ChatRequest(BaseModel):
    message: str
    max_iterations: Optional[int] = 10

class ChatResponse(BaseModel):
    message: str
    success: bool
    timestamp: str

class HealthResponse(BaseModel):
    status: str
    agent_available: bool
    version: str


@app.get("/", response_model=dict)
async def root():
    """Root endpoint with API info"""
    return {
        "message": "Video Creator AI API",
        "version": "1.0.0",
        "endpoints": {
            "health": "/health",
            "chat": "/api/chat",
            "docs": "/docs"
        }
    }


@app.get("/health", response_model=HealthResponse)
async def health_check():
    """Health check endpoint"""
    return HealthResponse(
        status="healthy",
        agent_available=AGENT_AVAILABLE,
        version="1.0.0"
    )


@app.post("/api/chat", response_model=ChatResponse)
async def chat_endpoint(request: ChatRequest):
    """
    Chat endpoint that processes user messages through the AI agent

    Args:
        request: ChatRequest with message and optional max_iterations

    Returns:
        ChatResponse with agent's response
    """
    try:
        if not AGENT_AVAILABLE:
            # Return a helpful message if agent is not available
            return ChatResponse(
                message="⚠️ AI Agent is not available on this server. Please ensure the agent module is properly installed.\n\nCurrent Status: Demo Mode\n\nYou can:\n1. Install required dependencies\n2. Configure environment variables\n3. Check agent.py is available\n\nFor now, I can help you with basic information about the platform.",
                success=False,
                timestamp=__import__('datetime').datetime.now().isoformat()
            )

        # Run the agent with the user's message
        agent_response = run_agent(request.message, max_iterations=request.max_iterations)

        return ChatResponse(
            message=agent_response,
            success=True,
            timestamp=__import__('datetime').datetime.now().isoformat()
        )

    except Exception as e:
        # Return error message
        return ChatResponse(
            message=f"❌ Error processing your request: {str(e)}\n\nPlease try again or contact support.",
            success=False,
            timestamp=__import__('datetime').datetime.now().isoformat()
        )


@app.get("/api/stats")
async def get_stats():
    """Get agent usage statistics"""
    try:
        if not AGENT_AVAILABLE:
            return {"error": "Agent not available"}

        from agent import load_statistics
        stats = load_statistics()

        return {
            "success": True,
            "stats": {
                "total_actions": stats.total_actions,
                "tool_calls": stats.tool_calls,
                "first_usage": stats.first_usage,
                "last_usage": stats.last_usage
            }
        }
    except Exception as e:
        return {"success": False, "error": str(e)}


# Startup event
@app.on_event("startup")
async def startup_event():
    """Run on startup"""
    print("🚀 Video Creator AI API starting...")
    print(f"📊 Agent Available: {AGENT_AVAILABLE}")

    if AGENT_AVAILABLE:
        print("✅ Ready to process requests!")
    else:
        print("⚠️ Running in demo mode - agent module not available")


# Shutdown event
@app.on_event("shutdown")
async def shutdown_event():
    """Run on shutdown"""
    print("👋 Video Creator AI API shutting down...")


if __name__ == "__main__":
    import uvicorn

    # Run the server
    uvicorn.run(
        "server:app",
        host="0.0.0.0",
        port=8000,
        reload=True,  # Enable auto-reload during development
        log_level="info"
    )
