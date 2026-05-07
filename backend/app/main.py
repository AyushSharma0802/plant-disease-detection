"""
🌿 Plant Disease Detection - FastAPI Backend

Main application entry point
"""
from dotenv import load_dotenv
import os

# Load .env file FIRST
load_dotenv(os.path.join(os.path.dirname(__file__), '../.env'))

import logging
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes.chat import router as chat_router
# Import routes
from app.routes.predict import router as predict_router

# Setup logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Create FastAPI app
app = FastAPI(
    title="🌿 Plant Disease Detection API",
    description="ML-powered disease identification and product recommendations",
    version="1.0.0",
    docs_url="/api/docs",
    openapi_url="/api/openapi.json"
)

# ============================================================================
# MIDDLEWARE - CORS (Allow frontend to call backend)
# ============================================================================

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000",
        "http://localhost:5173",
        "http://127.0.0.1:3000",
        "http://127.0.0.1:5173",
        "*"  # Allow all for development
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ============================================================================
# STARTUP & SHUTDOWN EVENTS
# ============================================================================

@app.on_event("startup")
async def startup_event():
    """Run when app starts"""
    logger.info("🚀 Starting Plant Disease Detection API...")
    logger.info("✅ API ready at http://localhost:8000")
    logger.info("📚 Docs available at http://localhost:8000/api/docs")

@app.on_event("shutdown")
async def shutdown_event():
    """Run when app shuts down"""
    logger.info("🛑 Shutting down application...")

# ============================================================================
# ROUTES
# ============================================================================

# Include prediction routes
app.include_router(predict_router, prefix="/api")
app.include_router(chat_router, prefix="/api")

# ============================================================================
# ROOT ENDPOINT
# ============================================================================

@app.get("/")
async def root():
    """Root endpoint"""
    return {
        "message": "🌿 Plant Disease Detection API",
        "docs": "/api/docs",
        "health": "/api/health",
        "predict": "/api/predict/disease"
    }

@app.get("/api/health")
async def health_check():
    """Health check endpoint"""
    return {
        "status": "healthy",
        "service": "Plant Disease Detection API",
        "version": "1.0.0"
    }

# ============================================================================
# ERROR HANDLERS
# ============================================================================

@app.exception_handler(Exception)
async def global_exception_handler(request, exc):
    """Handle unexpected errors"""
    logger.error(f"❌ Error: {str(exc)}")
    return {
        "success": False,
        "error": str(exc)
    }