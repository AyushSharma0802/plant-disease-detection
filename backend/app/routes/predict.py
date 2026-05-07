"""
Disease prediction and product recommendation endpoint
"""

from fastapi import APIRouter, File, UploadFile, HTTPException, status
from datetime import datetime
import tensorflow as tf
from tensorflow import keras
import numpy as np
from PIL import Image
import io
import json
import uuid
import logging
from app.database import get_disease_info, get_recommended_products

logger = logging.getLogger(__name__)
router = APIRouter(prefix="/predict", tags=["Prediction"])

# Load model once
_model = None
_disease_mapping = None

def load_model():
    """Load model if not already loaded"""
    global _model, _disease_mapping
    
    if _model is None:
        logger.info("Loading ML model...")
        try:
            _model = keras.models.load_model("ml_model/model.h5")
            logger.info("Model loaded successfully!")
        except Exception as e:
            logger.error(f"Failed to load model: {e}")
            raise
    
    if _disease_mapping is None:
        try:
            with open("ml_model/disease_mapping.json", "r") as f:
                _disease_mapping = json.load(f)
        except Exception as e:
            logger.error(f"Failed to load disease mapping: {e}")
            raise
    
    return _model, _disease_mapping

def preprocess_image(image_bytes: bytes) -> np.ndarray:
    """Preprocess image for model"""
    try:
        image = Image.open(io.BytesIO(image_bytes))
        if image.mode != 'RGB':
            image = image.convert('RGB')
        
        image = image.resize((224, 224), Image.Resampling.LANCZOS)
        image_array = np.array(image, dtype=np.float32)
        image_array = (image_array / 127.5) - 1
        image_array = np.expand_dims(image_array, axis=0)
        
        return image_array
    except Exception as e:
        logger.error(f"Image preprocessing error: {e}")
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Invalid image: {str(e)}"
        )

@router.post("/disease")
async def predict_disease(file: UploadFile = File(...)):
    """
    Predict disease from leaf image and recommend products
    """
    
    # Validate file
    if file.content_type not in ["image/jpeg", "image/png", "image/jpg"]:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Only JPEG and PNG images allowed"
        )
    
    logger.info(f"Processing image: {file.filename}")
    
    # Read file
    contents = await file.read()
    
    # Check size
    if len(contents) > 50 * 1024 * 1024:
        raise HTTPException(
            status_code=status.HTTP_413_REQUEST_ENTITY_TOO_LARGE,
            detail="Image too large. Max 50MB"
        )
    
    # Load model
    model, disease_mapping = load_model()
    
    # Preprocess
    image_array = preprocess_image(contents)
    
    # Predict
    logger.info("Making prediction...")
    predictions = model.predict(image_array, verbose=0)
    
    # Get results
    top_idx = np.argmax(predictions[0])
    confidence = float(predictions[0][top_idx])
    disease_class = disease_mapping[str(top_idx)]
    
    # Get disease info
    disease_info = get_disease_info(disease_class)
    
    # Get recommended products
    recommended_products = get_recommended_products(disease_class)
    
    # Get top-5 predictions
    top_5_indices = np.argsort(predictions[0])[-5:][::-1]
    top_5 = [
        {
            "disease": disease_mapping[str(idx)],
            "confidence": float(predictions[0][idx])
        }
        for idx in top_5_indices
    ]
    
    # Prepare response
    response = {
        "success": True,
        "scan_id": str(uuid.uuid4()),
        "timestamp": datetime.now().isoformat(),
        "image_name": file.filename,
        
        # Disease prediction
        "prediction": {
            "disease_class": disease_class,
            "disease_name": disease_info.get("name"),
            "confidence": round(confidence * 100, 2),
            "description": disease_info.get("description"),
            "severity": disease_info.get("severity"),
            "impact": disease_info.get("impact"),
            "treatment_period": disease_info.get("treatment_period"),
            "affected_parts": disease_info.get("affected_parts")
        },
        
        # Recommended products
        "recommendations": {
            "total_products": len(recommended_products),
            "products": [
                {
                    "product_id": product["product_id"],
                    "name": product["name"],
                    "price": product["price"],
                    "category": product["category"],
                    "description": product["description"],
                    "active_ingredient": product["active_ingredient"],
                    "efficacy": f"{product['efficacy']}%",
                    "application_period": product["application_period"],
                    "rating": product["rating"],
                    "stock": product["stock"],
                    "in_stock": product["stock"] > 0
                }
                for product in recommended_products[:5]
            ]
        },
        
        # Debug info
        "debug": {
            "top_5_predictions": top_5,
            "inference_time_ms": "< 2000"
        }
    }
    
    logger.info(f"Prediction complete: {disease_class} ({confidence*100:.2f}%)")
    
    return response

@router.get("/health")
async def health_check():
    """Health check for prediction service"""
    return {
        "status": "healthy",
        "service": "prediction",
        "model_loaded": _model is not None
    }