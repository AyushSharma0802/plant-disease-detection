import React, { useState } from 'react';
import '../styles/Scanner.css';

const API_URL = import.meta.env.VITE_API_URL || 'http://localhost:8000/api';

// Disease information database
const DISEASE_INFO = {
  0: { name: 'Apple Scab', severity: 'medium', impact: 'Leaf spotting and defoliation' },
  1: { name: 'Apple Black Rot', severity: 'critical', impact: 'Fruit rot and canker' },
  2: { name: 'Cedar Apple Rust', severity: 'high', impact: 'Orange spots on leaves' },
  3: { name: 'Apple Healthy', severity: 'none', impact: 'No disease detected' },
  4: { name: 'Corn Gray Leaf Spot', severity: 'high', impact: 'Gray lesions on leaves' },
  5: { name: 'Corn Common Rust', severity: 'medium', impact: 'Reddish pustules' },
  6: { name: 'Corn Northern Leaf Blight', severity: 'critical', impact: 'Elongated lesions' },
  7: { name: 'Corn Healthy', severity: 'none', impact: 'No disease detected' },
  8: { name: 'Pepper Bacterial Spot', severity: 'high', impact: 'Dark spots on leaves' },
  9: { name: 'Pepper Healthy', severity: 'none', impact: 'No disease detected' },
  10: { name: 'Potato Early Blight', severity: 'high', impact: 'Brown circular spots' },
  11: { name: 'Potato Late Blight', severity: 'critical', impact: 'Water-soaked lesions' },
  12: { name: 'Potato Healthy', severity: 'none', impact: 'No disease detected' },
  13: { name: 'Tomato Bacterial Spot', severity: 'high', impact: 'Dark lesions on fruit' },
  14: { name: 'Tomato Early Blight', severity: 'high', impact: 'Brown spots on leaves' },
  15: { name: 'Tomato Late Blight', severity: 'critical', impact: 'Water-soaked spots' },
  16: { name: 'Tomato Leaf Mold', severity: 'medium', impact: 'Yellow-brown patches' },
  17: { name: 'Tomato Septoria Spot', severity: 'medium', impact: 'Small circular spots' },
  18: { name: 'Tomato Spider Mites', severity: 'high', impact: 'Fine webbing on leaves' },
  19: { name: 'Tomato Target Spot', severity: 'high', impact: 'Concentric rings on leaves' },
  20: { name: 'Tomato Yellow Leaf Curl', severity: 'critical', impact: 'Leaf curling and yellowing' },
  21: { name: 'Tomato Mosaic Virus', severity: 'high', impact: 'Mottled leaves' },
  22: { name: 'Tomato Healthy', severity: 'none', impact: 'No disease detected' },
};

// Recommended products
const PRODUCTS = [
  { id: 1, name: 'Systemic Fungicide', price: 45.99, efficacy: 95 },
  { id: 2, name: 'Copper Sulfate', price: 32.50, efficacy: 88 },
  { id: 3, name: 'Neem Oil Spray', price: 28.99, efficacy: 85 },
  { id: 4, name: 'Sulfur Dust', price: 22.50, efficacy: 80 },
  { id: 5, name: 'Bacterial Spray', price: 38.99, efficacy: 92 },
];

export default function Scanner() {
  const [selectedImage, setSelectedImage] = useState(null);
  const [preview, setPreview] = useState(null);
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  const handleImageSelect = (e) => {
    const file = e.target.files[0];
    if (file) {
      setSelectedImage(file);
      setPreview(URL.createObjectURL(file));
      setResult(null);
      setError(null);
    }
  };

  const handlePredict = async () => {
    if (!selectedImage) {
      setError('Please select an image first');
      return;
    }

    setLoading(true);
    setError(null);
    setResult(null);

    try {
      const formData = new FormData();
      formData.append('file', selectedImage);

      console.log('Sending to:', `${API_URL}/predict/disease`);

      const response = await fetch(`${API_URL}/predict/disease`, {
        method: 'POST',
        body: formData,
      });

      console.log('Response status:', response.status);

      if (!response.ok) {
        const errorText = await response.text();
        throw new Error(`HTTP ${response.status}: ${errorText}`);
      }

      const data = await response.json();
      console.log('Received data:', data);

      if (data.success && data.prediction) {
        const classIdx = data.prediction.class_index;
        const diseaseInfo = DISEASE_INFO[classIdx] || DISEASE_INFO[0];
        
        setResult({
          ...data.prediction,
          ...diseaseInfo,
          products: PRODUCTS.slice(0, 3), // Show top 3 products
        });
      } else {
        throw new Error('Invalid response format');
      }
    } catch (err) {
      console.error('Full error:', err);
      setError(err.message || 'Prediction failed. Please try again.');
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="scanner-container">
      <h1>🌿 Scan Your Plant</h1>
      <p className="subtitle">Upload a photo of your plant leaf to detect diseases</p>

      {/* Upload Section */}
      <div className="upload-section">
        <input
          type="file"
          accept="image/*"
          onChange={handleImageSelect}
          id="image-input"
          style={{ display: 'none' }}
        />
        <label htmlFor="image-input" className="upload-button">
          📸 Choose Image
        </label>
        {selectedImage && <p className="file-name">✅ {selectedImage.name}</p>}
      </div>

      {/* Preview Section */}
      {preview && (
        <div className="preview-section">
          <img src={preview} alt="Plant leaf" className="preview-image" />
          <button
            onClick={handlePredict}
            disabled={loading}
            className="predict-button"
          >
            {loading ? '⏳ Analyzing... (This may take 10-15 seconds)' : '🔍 Analyze Plant'}
          </button>
        </div>
      )}

      {/* Error Section */}
      {error && (
        <div className="error-message">
          <p>❌ {error}</p>
        </div>
      )}

      {/* Result Section */}
      {result && (
        <div className="result-section">
          <h2>✅ Analysis Complete</h2>

          {/* Disease Info */}
          <div className="result-card disease-card">
            <h3>🌾 Detected Disease</h3>
            <div className="disease-info">
              <p className="disease-name">{result.name}</p>
              <p className="confidence">
                Confidence: <strong>{result.confidence}%</strong>
              </p>
              <p className={`severity severity-${result.severity}`}>
                Severity: <strong>{result.severity.toUpperCase()}</strong>
              </p>
              <p className="impact">Impact: {result.impact}</p>
            </div>
          </div>

          {/* Product Recommendations */}
          {result.products && (
            <div className="result-card products-card">
              <h3>💊 Recommended Products</h3>
              <div className="products-list">
                {result.products.map((product) => (
                  <div key={product.id} className="product-item">
                    <p className="product-name">{product.name}</p>
                    <p className="product-efficacy">
                      Efficacy: {product.efficacy}%
                    </p>
                    <p className="product-price">₹{product.price}</p>
                    <button className="add-to-cart">🛒 Add to Cart</button>
                  </div>
                ))}
              </div>
            </div>
          )}

          {/* Treatment Advice */}
          <div className="result-card advice-card">
            <h3>📋 Treatment Advice</h3>
            <ul>
              <li>Apply recommended fungicide/pesticide as per product instructions</li>
              <li>Ensure proper leaf coverage during spraying</li>
              <li>Repeat treatment every 7-10 days if needed</li>
              <li>Consult our AI Expert for more detailed guidance</li>
            </ul>
            <button className="chat-button" onClick={() => window.location.href = '/chat'}>
              💬 Chat with Expert
            </button>
          </div>
        </div>
      )}

      {/* Initial Message */}
      {!selectedImage && !result && (
        <div className="info-section">
          <div className="info-card">
            <h3>📸 How to use:</h3>
            <ol>
              <li>Take a clear photo of an affected plant leaf</li>
              <li>Ensure good lighting</li>
              <li>Upload the image</li>
              <li>Get instant disease diagnosis</li>
            </ol>
          </div>
        </div>
      )}
    </div>
  );
}