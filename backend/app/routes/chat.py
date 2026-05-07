"""
Expert chat endpoint using NVIDIA NIM API
"""

from fastapi import APIRouter, HTTPException, status
import requests
import logging
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

logger = logging.getLogger(__name__)
router = APIRouter(prefix="/chat", tags=["Chat"])

# NVIDIA NIM Configuration from .env
NIM_API_KEY = os.getenv("NVIDIA_NIM_API_KEY","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")
NIM_URL = os.getenv("NIM_URL", "https://integrate.api.nvidia.com/v1/chat/completions")
NIM_MODEL = os.getenv("NIM_MODEL", "meta/llama-3.2-3b-instruct")

logger.info(f"NIM Configuration:")
logger.info(f"  Model: {NIM_MODEL}")
logger.info(f"  URL: {NIM_URL}")
logger.info(f"  API Key: {'Set' if NIM_API_KEY else 'NOT SET'}")

SYSTEM_PROMPT = """You are an expert plant disease consultant with deep knowledge of:
- Plant diseases and symptoms
- Disease identification and diagnosis
- Treatment recommendations
- Prevention strategies
- Product recommendations
- Plant care and maintenance

You have access to knowledge about diseases affecting:
- Apple (scab, black rot, cedar apple rust)
- Corn/Maize (gray leaf spot, common rust, northern leaf blight)
- Pepper (bacterial spot)
- Potato (early blight, late blight)
- Tomato (multiple diseases and viruses)

When helping users:
1. Ask clarifying questions if needed
2. Provide specific, actionable advice
3. Recommend products when appropriate
4. Emphasize prevention methods
5. Be empathetic and encouraging

Keep responses concise but informative."""

@router.post("/expert")
async def chat_expert(request: dict):
    """
    Chat with plant disease expert AI using NVIDIA NIM
    """
    
    try:
        message = request.get("message", "")
        conversation_history = request.get("conversation_history", [])
        
        if not message:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Message is required"
            )
        
        if not NIM_API_KEY:
            logger.error("NVIDIA_NIM_API_KEY not configured")
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail="API key not configured. Check .env file."
            )
        
        logger.info(f"Processing message: {message[:50]}...")
        
        # Build message history
        messages = []
        
        # Add system prompt
        messages.append({
            "role": "system",
            "content": SYSTEM_PROMPT
        })
        
        # Add conversation history (last 10 messages)
        for msg in conversation_history[-10:]:
            msg_type = msg.get("type", "")
            msg_text = msg.get("text", "")
            
            if msg_type == "user":
                messages.append({
                    "role": "user",
                    "content": msg_text
                })
            elif msg_type == "bot":
                messages.append({
                    "role": "assistant",
                    "content": msg_text
                })
        
        # Add current message
        messages.append({
            "role": "user",
            "content": message
        })
        
        logger.info(f"Total messages in context: {len(messages)}")
        
        # Prepare headers
        headers = {
            "Authorization": f"Bearer {NIM_API_KEY}",
            "Content-Type": "application/json"
        }
        
        # Prepare payload
        payload = {
            "model": NIM_MODEL,
            "messages": messages,
            "temperature": 0.7,
            "top_p": 0.9,
            "max_tokens": 512,
            "stream": False
        }
        
        logger.info(f"Calling NVIDIA NIM API with model: {NIM_MODEL}")
        
        # Call NVIDIA NIM API
        response = requests.post(
            NIM_URL,
            headers=headers,
            json=payload,
            timeout=30
        )
        
        logger.info(f"Response status code: {response.status_code}")
        
        # Handle errors
        if response.status_code != 200:
            error_text = response.text
            logger.error(f"NVIDIA NIM API Error (Status {response.status_code}): {error_text}")
            
            try:
                error_json = response.json()
                error_msg = error_json.get("error", {}).get("message", error_text)
            except:
                error_msg = error_text
            
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail=f"NVIDIA API Error: {error_msg}"
            )
        
        # Parse response
        try:
            result = response.json()
            logger.info(f"Response received: {str(result)[:100]}")
        except:
            logger.error(f"Failed to parse JSON response: {response.text}")
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail="Failed to parse API response"
            )
        
        # Extract bot response
        try:
            bot_response = result["choices"][0]["message"]["content"]
        except (KeyError, IndexError) as e:
            logger.error(f"Failed to extract response content: {str(e)}, Response: {result}")
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail="Invalid response format from API"
            )
        
        if not bot_response or not bot_response.strip():
            logger.error("Empty response received from API")
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail="Empty response from API"
            )
        
        logger.info(f"Bot response (first 50 chars): {bot_response[:50]}")
        
        return {
            "success": True,
            "response": bot_response.strip()
        }
        
    except HTTPException:
        raise
    except requests.exceptions.Timeout:
        logger.error("Request timeout to NVIDIA NIM API")
        raise HTTPException(
            status_code=status.HTTP_504_GATEWAY_TIMEOUT,
            detail="API request timeout. Please try again."
        )
    except requests.exceptions.ConnectionError as e:
        logger.error(f"Connection error: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail="Cannot connect to chat service. Check your internet."
        )
    except Exception as e:
        logger.error(f"Unexpected error: {type(e).__name__}: {str(e)}", exc_info=True)
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error: {str(e)}"
        )

@router.get("/health")
async def chat_health():
    """Health check for chat service"""
    return {
        "status": "healthy",
        "service": "chat",
        "api": "nvidia_nim",
        "model": NIM_MODEL,
        "api_key_set": bool(NIM_API_KEY)
    }