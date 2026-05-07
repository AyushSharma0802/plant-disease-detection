"""
Disease information and product recommendations database
"""

DISEASES_INFO = {
    "Apple___Apple_scab": {
        "name": "Apple Scab",
        "description": "Fungal infection causing dark lesions on leaves and fruit",
        "severity": "high",
        "impact": "Reduces fruit quality, causes premature leaf drop",
        "treatment_period": "4-6 weeks",
        "affected_parts": "Leaves, stems, fruit"
    },
    "Apple___Black_rot": {
        "name": "Apple Black Rot",
        "description": "Dark brown/black rot on fruit and leaves",
        "severity": "critical",
        "impact": "Complete fruit loss if untreated",
        "treatment_period": "3-4 weeks",
        "affected_parts": "Fruit, leaves, twigs"
    },
    "Apple___Cedar_apple_rust": {
        "name": "Apple Cedar Apple Rust",
        "description": "Orange fungal growth on leaves and fruit",
        "severity": "high",
        "impact": "Defoliates trees, reduces fruit quality",
        "treatment_period": "3-4 weeks",
        "affected_parts": "Leaves, fruit, stems"
    },
    "Apple___healthy": {
        "name": "Healthy Apple Plant",
        "description": "Plant shows no signs of disease",
        "severity": "none",
        "impact": "Continue regular maintenance",
        "treatment_period": "N/A",
        "affected_parts": "None"
    },
    "Corn_(maize)___Cercospora_leaf_spot Gray_leaf_spot": {
        "name": "Corn Gray Leaf Spot",
        "description": "Gray rectangular spots on leaves",
        "severity": "medium",
        "impact": "Reduces grain yield by 20-30%",
        "treatment_period": "3-4 weeks",
        "affected_parts": "Leaves"
    },
    "Corn_(maize)___Common_rust_": {
        "name": "Corn Common Rust",
        "description": "Reddish-brown pustules on leaves",
        "severity": "high",
        "impact": "Can reduce yield by 50%",
        "treatment_period": "2-3 weeks",
        "affected_parts": "Leaves"
    },
    "Corn_(maize)___Northern_Leaf_Blight": {
        "name": "Corn Northern Leaf Blight",
        "description": "Elongated tan lesions with dark borders",
        "severity": "high",
        "impact": "Significant yield reduction",
        "treatment_period": "3-4 weeks",
        "affected_parts": "Leaves, stalks"
    },
    "Corn_(maize)___healthy": {
        "name": "Healthy Corn Plant",
        "description": "Plant shows no signs of disease",
        "severity": "none",
        "impact": "Continue regular maintenance",
        "treatment_period": "N/A",
        "affected_parts": "None"
    },
    "Pepper__bell___Bacterial_spot": {
        "name": "Pepper Bacterial Spot",
        "description": "Small dark spots with yellow halo",
        "severity": "high",
        "impact": "Reduced fruit quality and marketability",
        "treatment_period": "2-3 weeks",
        "affected_parts": "Leaves, fruit, stems"
    },
    "Pepper__bell___healthy": {
        "name": "Healthy Pepper Plant",
        "description": "Plant shows no signs of disease",
        "severity": "none",
        "impact": "Continue regular maintenance",
        "treatment_period": "N/A",
        "affected_parts": "None"
    },
    "Potato___Early_blight": {
        "name": "Potato Early Blight",
        "description": "Brown spots with concentric rings on lower leaves",
        "severity": "high",
        "impact": "Can destroy entire crop if untreated",
        "treatment_period": "2-3 weeks",
        "affected_parts": "Lower leaves, stems"
    },
    "Potato___Late_blight": {
        "name": "Potato Late Blight",
        "description": "Water-soaked spots on leaves and stems",
        "severity": "critical",
        "impact": "Complete crop failure possible",
        "treatment_period": "1-2 weeks",
        "affected_parts": "All plant parts"
    },
    "Potato___healthy": {
        "name": "Healthy Potato Plant",
        "description": "Plant shows no signs of disease",
        "severity": "none",
        "impact": "Continue regular maintenance",
        "treatment_period": "N/A",
        "affected_parts": "None"
    },
    "Tomato_Bacterial_spot": {
        "name": "Tomato Bacterial Spot",
        "description": "Small dark spots with greasy appearance",
        "severity": "high",
        "impact": "Reduces fruit quality and marketability",
        "treatment_period": "2-3 weeks",
        "affected_parts": "Leaves, fruit, stems"
    },
    "Tomato_Early_blight": {
        "name": "Tomato Early Blight",
        "description": "Brown spots with concentric rings",
        "severity": "high",
        "impact": "Reduces fruit production",
        "treatment_period": "2-3 weeks",
        "affected_parts": "Lower leaves, stems"
    },
    "Tomato_Late_blight": {
        "name": "Tomato Late Blight",
        "description": "Water-soaked spots spreading rapidly",
        "severity": "critical",
        "impact": "Can destroy entire crop",
        "treatment_period": "1-2 weeks",
        "affected_parts": "All parts"
    },
    "Tomato_Leaf_Mold": {
        "name": "Tomato Leaf Mold",
        "description": "Yellow spots with gray-brown mold underneath",
        "severity": "medium",
        "impact": "Reduces leaf area for photosynthesis",
        "treatment_period": "2-3 weeks",
        "affected_parts": "Leaves"
    },
    "Tomato_Septoria_leaf_spot": {
        "name": "Tomato Septoria Leaf Spot",
        "description": "Small circular spots with dark borders",
        "severity": "medium",
        "impact": "Progressive defoliation",
        "treatment_period": "2-3 weeks",
        "affected_parts": "Leaves"
    },
    "Tomato_Spider_mites_Two_spotted_spider_mite": {
        "name": "Tomato Spider Mites",
        "description": "Fine webbing, yellowing leaves",
        "severity": "high",
        "impact": "Severe leaf damage and fruit drop",
        "treatment_period": "1-2 weeks",
        "affected_parts": "Leaves"
    },
    "Tomato__Target_Spot": {
        "name": "Tomato Target Spot",
        "description": "Circular spots with concentric rings",
        "severity": "medium",
        "impact": "Reduces fruit quality",
        "treatment_period": "2-3 weeks",
        "affected_parts": "Leaves, fruit"
    },
    "Tomato__Tomato_YellowLeaf__Curl_Virus": {
        "name": "Tomato Yellow Leaf Curl Virus",
        "description": "Leaves curl upward and turn yellow",
        "severity": "critical",
        "impact": "Severe growth stunting and fruit loss",
        "treatment_period": "3-4 weeks",
        "affected_parts": "Entire plant"
    },
    "Tomato__Tomato_mosaic_virus": {
        "name": "Tomato Mosaic Virus",
        "description": "Mottled leaves, stunted growth",
        "severity": "high",
        "impact": "Significantly reduced yield",
        "treatment_period": "3-4 weeks",
        "affected_parts": "Entire plant"
    },
    "Tomato_healthy": {
        "name": "Healthy Tomato Plant",
        "description": "Plant shows no signs of disease",
        "severity": "none",
        "impact": "Continue regular maintenance",
        "treatment_period": "N/A",
        "affected_parts": "None"
    }
}

PRODUCTS = [
    {
        "product_id": "prod_001",
        "name": "Organic Fungicide Spray",
        "price": 24.99,
        "category": "fungicide",
        "description": "Broad-spectrum organic fungicide for fungal diseases",
        "active_ingredient": "Neem Oil & Sulfur",
        "efficacy": 85,
        "application_period": "Weekly",
        "for_diseases": ["Apple___Apple_scab", "Tomato_Early_blight"],
        "rating": 4.5,
        "stock": 150
    },
    {
        "product_id": "prod_002",
        "name": "Copper Bactericide",
        "price": 32.50,
        "category": "bactericide",
        "description": "Effective against bacterial leaf spots",
        "active_ingredient": "Copper Hydroxide",
        "efficacy": 90,
        "application_period": "Every 7-10 days",
        "for_diseases": ["Pepper__bell___Bacterial_spot", "Tomato_Bacterial_spot"],
        "rating": 4.7,
        "stock": 120
    },
    {
        "product_id": "prod_003",
        "name": "Systemic Fungicide",
        "price": 45.99,
        "category": "fungicide",
        "description": "Systemic action for severe fungal infections",
        "active_ingredient": "Azoxystrobin",
        "efficacy": 95,
        "application_period": "Every 14 days",
        "for_diseases": ["Apple___Black_rot", "Potato___Late_blight", "Tomato_Late_blight"],
        "rating": 4.8,
        "stock": 100
    },
    {
        "product_id": "prod_004",
        "name": "Insecticide Concentrate",
        "price": 28.50,
        "category": "insecticide",
        "description": "Controls spider mites and other pests",
        "active_ingredient": "Pyrethrin",
        "efficacy": 88,
        "application_period": "Weekly or as needed",
        "for_diseases": ["Tomato_Spider_mites_Two_spotted_spider_mite"],
        "rating": 4.6,
        "stock": 200
    },
    {
        "product_id": "prod_005",
        "name": "Rust Prevention Formula",
        "price": 26.50,
        "category": "fungicide",
        "description": "Specifically for rust diseases",
        "active_ingredient": "Sulfur & Oil",
        "efficacy": 89,
        "application_period": "Every 10-14 days",
        "for_diseases": ["Corn_(maize)___Common_rust_"],
        "rating": 4.7,
        "stock": 125
    },
    {
        "product_id": "prod_006",
        "name": "Antiviral Spray",
        "price": 35.00,
        "category": "antiviral",
        "description": "For viral diseases like mosaic virus",
        "active_ingredient": "Plant extracts",
        "efficacy": 75,
        "application_period": "Every 5-7 days",
        "for_diseases": ["Tomato__Tomato_mosaic_virus", "Tomato__Tomato_YellowLeaf__Curl_Virus"],
        "rating": 4.3,
        "stock": 90
    },
    {
        "product_id": "prod_007",
        "name": "Leaf Spot Treatment",
        "price": 22.99,
        "category": "fungicide",
        "description": "Targeted treatment for leaf spots",
        "active_ingredient": "Mancozeb",
        "efficacy": 87,
        "application_period": "Every 7-14 days",
        "for_diseases": ["Tomato_Septoria_leaf_spot", "Tomato__Target_Spot"],
        "rating": 4.5,
        "stock": 140
    },
    {
        "product_id": "prod_008",
        "name": "Powdery Mildew Control",
        "price": 19.99,
        "category": "fungicide",
        "description": "Organic treatment for mold and mildew",
        "active_ingredient": "Potassium Bicarbonate",
        "efficacy": 80,
        "application_period": "Weekly",
        "for_diseases": ["Tomato_Leaf_Mold"],
        "rating": 4.4,
        "stock": 180
    },
    {
        "product_id": "prod_009",
        "name": "Blight Elimination Kit",
        "price": 59.99,
        "category": "fungicide",
        "description": "Complete solution for early and late blight",
        "active_ingredient": "Copper + Sulfur",
        "efficacy": 92,
        "application_period": "Every 10 days",
        "for_diseases": ["Potato___Early_blight", "Potato___Late_blight"],
        "rating": 4.7,
        "stock": 85
    },
    {
        "product_id": "prod_010",
        "name": "Comprehensive Disease Prevention",
        "price": 49.99,
        "category": "multi-purpose",
        "description": "Multi-purpose fungicide for various crops",
        "active_ingredient": "Multiple active ingredients",
        "efficacy": 85,
        "application_period": "Every 7-14 days",
        "for_diseases": ["Apple___Apple_scab", "Corn_(maize)___Northern_Leaf_Blight", "Potato___Early_blight"],
        "rating": 4.6,
        "stock": 110
    }
]

def get_disease_info(disease_class):
    """Get detailed information about a disease"""
    return DISEASES_INFO.get(disease_class, {
        "name": "Unknown Disease",
        "description": "Unable to identify disease",
        "severity": "unknown",
        "impact": "Consult an expert",
        "treatment_period": "Unknown",
        "affected_parts": "Unknown"
    })

def get_recommended_products(disease_class):
    """Get products that treat a specific disease"""
    recommended = []
    for product in PRODUCTS:
        if disease_class in product.get("for_diseases", []):
            recommended.append(product)
    
    recommended.sort(key=lambda x: x.get("efficacy", 0), reverse=True)
    return recommended

def get_all_products():
    """Get all available products"""
    return PRODUCTS