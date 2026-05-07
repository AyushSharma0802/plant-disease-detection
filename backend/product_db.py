"""
Products database with disease-to-product mapping
"""

# Product catalog
PRODUCTS = {
    "PROD_001": {
        "name": "Copper Fungicide Spray",
        "price": 250,
        "category": "Fungicide",
        "description": "Organic copper-based fungicide for apple scab, early blight",
        "image_url": "https://via.placeholder.com/300?text=Copper+Fungicide",
        "rating": 4.5,
        "stock": 50,
        "for_diseases": ["Apple_scab", "Tomato_Early_blight"]
    },
    "PROD_002": {
        "name": "Neem Oil Organic",
        "price": 180,
        "category": "Insecticide",
        "description": "100% organic neem oil for pest and disease control",
        "image_url": "https://via.placeholder.com/300?text=Neem+Oil",
        "rating": 4.7,
        "stock": 75,
        "for_diseases": ["Apple_disease_1", "Pepper_disease_1", "Corn_disease_1"]
    },
    "PROD_003": {
        "name": "Sulfur Dust 500g",
        "price": 120,
        "category": "Fungicide",
        "description": "Powdered sulfur for powdery mildew prevention",
        "image_url": "https://via.placeholder.com/300?text=Sulfur+Dust",
        "rating": 4.3,
        "stock": 100,
        "for_diseases": ["Tomato_powdery_mildew", "Grape_powdery_mildew"]
    },
    "PROD_004": {
        "name": "Potassium Permanganate 250g",
        "price": 150,
        "category": "Bactericide",
        "description": "For bacterial leaf spots and blights",
        "image_url": "https://via.placeholder.com/300?text=Potassium+Permanganate",
        "rating": 4.4,
        "stock": 40,
        "for_diseases": ["Tomato_bacterial_spot", "Pepper_bacterial_spot"]
    },
    "PROD_005": {
        "name": "Mancozeb Fungicide",
        "price": 200,
        "category": "Fungicide",
        "description": "Broad spectrum fungicide for late blight control",
        "image_url": "https://via.placeholder.com/300?text=Mancozeb",
        "rating": 4.6,
        "stock": 60,
        "for_diseases": ["Potato_Late_blight", "Tomato_Late_blight"]
    }
}

# Disease information with severity and impact
DISEASE_INFO = {
    "Apple_scab": {
        "full_name": "Apple Scab",
        "severity": "high",
        "impact": "Causes brownish lesions on leaves and fruit. Can reduce yield by 40-60%. Spreads in wet conditions.",
        "treatment": "Use fungicides, prune infected branches, maintain tree hygiene",
        "prevention": "Avoid overhead irrigation, ensure proper spacing"
    },
    "Apple_disease_1": {
        "full_name": "Apple Disease 1",
        "severity": "medium",
        "impact": "Moderate damage to foliage. Can cause 20-30% yield loss.",
        "treatment": "Apply organic fungicides regularly",
        "prevention": "Monitor plants weekly"
    },
    "Apple_disease_2": {
        "full_name": "Apple Disease 2",
        "severity": "low",
        "impact": "Minor leaf damage, less than 10% yield impact",
        "treatment": "Monitor and treat if spreading",
        "prevention": "Regular inspection"
    },
    "Apple_disease_3": {
        "full_name": "Apple Disease 3",
        "severity": "high",
        "impact": "Severe damage, can cause 50%+ yield loss",
        "treatment": "Immediate fungicide application required",
        "prevention": "Preventive spraying during season"
    },
    "Apple_healthy": {
        "full_name": "Healthy Apple Plant",
        "severity": "none",
        "impact": "Plant is healthy, no treatment needed",
        "treatment": "Maintain regular care and monitoring",
        "prevention": "Continue regular maintenance"
    },
    "Corn_disease_1": {
        "full_name": "Corn Leaf Blight",
        "severity": "high",
        "impact": "Causes rapid leaf death, yield loss up to 50%",
        "treatment": "Fungicide spray required",
        "prevention": "Use resistant varieties, crop rotation"
    },
    "Corn_disease_2": {
        "full_name": "Corn Rust",
        "severity": "medium",
        "impact": "Orange pustules on leaves, 20-40% yield loss",
        "treatment": "Fungicide application",
        "prevention": "Avoid moisture stress"
    },
    "Corn_disease_3": {
        "full_name": "Corn Smut",
        "severity": "low",
        "impact": "Gall formation, mostly cosmetic, 5-15% loss",
        "treatment": "Remove affected ears",
        "prevention": "Plant hygiene"
    },
    "Corn_healthy": {
        "full_name": "Healthy Corn Plant",
        "severity": "none",
        "impact": "Plant is healthy and thriving",
        "treatment": "Routine maintenance",
        "prevention": "Regular monitoring"
    },
    "Pepper_disease_1": {
        "full_name": "Pepper Anthracnose",
        "severity": "medium",
        "impact": "Causes fruit rot, 30% yield loss possible",
        "treatment": "Fungicide spray, remove infected fruit",
        "prevention": "Good air circulation, avoid wetting leaves"
    },
    "Pepper_disease_2": {
        "full_name": "Pepper Phytophthora",
        "severity": "critical",
        "impact": "Root rot, plant death possible, total crop failure risk",
        "treatment": "Improve drainage, use fungicides",
        "prevention": "Ensure well-draining soil"
    },
    "Pepper_healthy": {
        "full_name": "Healthy Pepper Plant",
        "severity": "none",
        "impact": "Plant is healthy",
        "treatment": "Standard care",
        "prevention": "Continue monitoring"
    },
    "Potato_disease_1": {
        "full_name": "Potato Early Blight",
        "severity": "medium",
        "impact": "Causes necrotic spots on leaves, 20-30% yield loss",
        "treatment": "Fungicide spray, remove infected leaves",
        "prevention": "Avoid overhead irrigation"
    },
    "Potato_disease_2": {
        "full_name": "Potato Late Blight",
        "severity": "critical",
        "impact": "Rapid plant death, tuber rot, total crop failure possible",
        "treatment": "Immediate fungicide application required",
        "prevention": "Plant resistant varieties, avoid moisture"
    },
    "Potato_disease_3": {
        "full_name": "Potato Leaf Roll",
        "severity": "high",
        "impact": "Virus disease, affects tuber quality, 40% loss possible",
        "treatment": "Remove infected plants, control aphids",
        "prevention": "Use certified seed, control vectors"
    },
    "Potato_healthy": {
        "full_name": "Healthy Potato Plant",
        "severity": "none",
        "impact": "Plant is healthy",
        "treatment": "Routine care",
        "prevention": "Continue monitoring"
    },
    "Tomato_disease_1": {
        "full_name": "Tomato Early Blight",
        "severity": "high",
        "impact": "Lower leaf death, fruit spotting, 40-50% yield loss",
        "treatment": "Remove affected leaves, fungicide spray",
        "prevention": "Improve air circulation, stake plants"
    },
    "Tomato_disease_2": {
        "full_name": "Tomato Late Blight",
        "severity": "critical",
        "impact": "Rapid plant and fruit rot, total crop loss possible",
        "treatment": "Immediate fungicide required, remove infected parts",
        "prevention": "Use resistant varieties, avoid moisture"
    },
    "Tomato_disease_3": {
        "full_name": "Tomato Leaf Mold",
        "severity": "medium",
        "impact": "Yellow patches on leaves, 20-30% yield loss",
        "treatment": "Improve ventilation, fungicide spray",
        "prevention": "Avoid wetting foliage"
    },
    "Tomato_disease_4": {
        "full_name": "Tomato Septoria Leaf Spot",
        "severity": "medium",
        "impact": "Small circular spots, 15-25% yield loss",
        "treatment": "Remove infected leaves, fungicide spray",
        "prevention": "Rotate crops, sanitize tools"
    },
    "Tomato_disease_5": {
        "full_name": "Tomato Powdery Mildew",
        "severity": "low",
        "impact": "White powder on leaves, minimal yield loss (5-10%)",
        "treatment": "Sulfur spray or oil-based fungicide",
        "prevention": "Improve air circulation"
    },
    "Tomato_disease_6": {
        "full_name": "Tomato Mosaic Virus",
        "severity": "high",
        "impact": "Stunted growth, mottled leaves, 50%+ yield loss",
        "treatment": "Remove infected plants, control aphids",
        "prevention": "Use resistant varieties, control vectors"
    },
    "Tomato_healthy": {
        "full_name": "Healthy Tomato Plant",
        "severity": "none",
        "impact": "Plant is healthy and productive",
        "treatment": "Regular care",
        "prevention": "Continue monitoring"
    }
}

def get_disease_info(disease_name):
    """Get disease information"""
    return DISEASE_INFO.get(disease_name, {
        "full_name": disease_name,
        "severity": "unknown",
        "impact": "Unknown disease",
        "treatment": "Consult expert",
        "prevention": "Monitor closely"
    })

def get_recommended_products(disease_name):
    """Get products recommended for a disease"""
    recommended = []
    for product_id, product in PRODUCTS.items():
        if disease_name in product["for_diseases"]:
            recommended.append({
                "product_id": product_id,
                "name": product["name"],
                "price": product["price"],
                "category": product["category"],
                "description": product["description"],
                "rating": product["rating"],
                "stock": product["stock"]
            })
    return recommended

def get_all_products():
    """Get all products"""
    return list(PRODUCTS.values())