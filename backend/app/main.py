from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import logging
from app.routes import predict, chat

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI(
    title="Plant Disease Detection API",
    description="AI-powered plant disease detection system",
    version="1.0.0"
)

# CORS Middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Root endpoint
@app.get("/")
async def root():
    return {
        "message": "🌿 Plant Disease Detection API",
        "docs": "/api/docs",
        "health": "/api/health",
        "predict": "/api/predict/disease",
        "chat": "/api/chat/expert"
    }

# Health check
@app.get("/api/health")
async def health():
    return {"status": "healthy"}

# Include routers - CORRECT PREFIXES
app.include_router(predict.router, prefix="/api/predict", tags=["Predict"])
app.include_router(chat.router, prefix="/api", tags=["Chat"])

logger.info("✅ FastAPI app initialized with all routes")