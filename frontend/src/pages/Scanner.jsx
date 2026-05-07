import React, { useState } from 'react';
import { Upload, ArrowLeft, AlertCircle, Check } from 'lucide-react';
import '../styles/Scanner.css';
import { useCart } from '../context/CartContext';

const API_URL = import.meta.env.VITE_API_URL || 'http://localhost:8000/api';

export default function Scanner({ onBack }) {
  const [selectedFile, setSelectedFile] = useState(null);
  const [preview, setPreview] = useState(null);
  const [loading, setLoading] = useState(false);
  const [result, setResult] = useState(null);
  const [error, setError] = useState(null);

  const handleFileChange = (e) => {
    const file = e.target.files?.[0];
    if (!file) return;

    if (!file.type.startsWith('image/')) {
      setError('Please select an image file');
      return;
    }

    const reader = new FileReader();
    reader.onloadend = () => {
      setPreview(reader.result);
      setError(null);
    };
    reader.readAsDataURL(file);

    setSelectedFile(file);
  };

  const handlePredict = async () => {
    if (!selectedFile) {
      setError('Please select an image');
      return;
    }

    try {
      setLoading(true);
      setError(null);

      const formData = new FormData();
      formData.append('file', selectedFile);

      const response = await fetch(`${API_URL}/predict/disease`, {
        method: 'POST',
        body: formData,
      });

      if (!response.ok) {
        throw new Error('Prediction failed');
      }

      const data = await response.json();
      setResult(data);
    } catch (err) {
      setError('Prediction failed. Try again.');
      console.error('Error:', err);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="scanner-container">
      <div className="scanner-header">
        <button className="btn-back" onClick={onBack}>
          <ArrowLeft size={20} /> Back
        </button>
        <h1>🌿 Scan Your Plant</h1>
      </div>

      <div className="scanner-content">
        <div className="upload-section">
          <h2>Upload Leaf Image</h2>

          <label className="file-input-label">
            <Upload size={40} />
            <p>Click to select or drag image</p>
            <input
              type="file"
              accept="image/*"
              onChange={handleFileChange}
              className="file-input"
            />
          </label>

          {preview && (
            <div className="preview-section">
              <img src={preview} alt="Preview" className="preview-image" />
              <button
                onClick={handlePredict}
                disabled={loading}
                className="btn-analyze"
              >
                {loading ? '🔄 Analyzing...' : '🧠 Analyze Image'}
              </button>
            </div>
          )}

          {error && (
            <div className="error-message">
              <AlertCircle size={20} />
              {error}
            </div>
          )}
        </div>

        <div className="results-section">
          <h2>Analysis Results</h2>

          {!result ? (
            <div className="no-results">
              <p>📸 Upload an image to see disease analysis</p>
            </div>
          ) : (
            <div className="results-content">
              <div className="result-card disease-card">
                <div className="result-header">
                  <h3>Detected Disease</h3>
                  <span className={`confidence ${getSeverityClass(result.prediction.severity)}`}>
                    {result.prediction.confidence}% confident
                  </span>
                </div>
                <div className="disease-name">{result.prediction.disease_name}</div>
                <p className="disease-description">{result.prediction.description}</p>
              </div>

              <div className="result-card impact-card">
                <h3>Disease Impact</h3>
                <div className="impact-details">
                  <DetailRow label="Severity" value={capitalizeFirst(result.prediction.severity)} />
                  <DetailRow label="Impact" value={result.prediction.impact} />
                  <DetailRow label="Treatment Period" value={result.prediction.treatment_period} />
                  <DetailRow label="Affected Parts" value={result.prediction.affected_parts} />
                </div>
              </div>

              {result.recommendations.total_products > 0 && (
                <div className="result-card products-card">
                  <h3>🛒 Recommended Products ({result.recommendations.total_products})</h3>
                  <div className="products-list">
                    {result.recommendations.products.map((product) => (
                      <ProductCard key={product.product_id} product={product} />
                    ))}
                  </div>
                </div>
              )}

              {result.recommendations.total_products === 0 && (
                <div className="result-card">
                  <h3>✅ No Treatment Needed</h3>
                  <p>Your plant appears healthy. Continue regular maintenance.</p>
                </div>
              )}
            </div>
          )}
        </div>
      </div>
    </div>
  );
}

function DetailRow({ label, value }) {
  return (
    <div className="detail-row">
      <span className="label">{label}</span>
      <span className="value">{value}</span>
    </div>
  );
}

function ProductCard({ product }) {
  const { addToCart } = useCart();
  return (
    <div className="product-card">
      <div className="product-header">
        <h4>{product.name}</h4>
        <span className="product-price">${product.price}</span>
      </div>
      <p className="product-description">{product.description}</p>
      
      <div className="product-details">
        <div className="detail">
          <span>Active Ingredient:</span>
          <strong>{product.active_ingredient}</strong>
        </div>
        <div className="detail">
          <span>Efficacy:</span>
          <strong>{product.efficacy}</strong>
        </div>
        <div className="detail">
          <span>Application:</span>
          <strong>{product.application_period}</strong>
        </div>
        <div className="detail">
          <span>Rating:</span>
          <strong>⭐ {product.rating}</strong>
        </div>
      </div>

      <div className="product-footer">
        {product.in_stock ? (
          <span className="in-stock">
            <Check size={16} /> In Stock ({product.stock})
          </span>
        ) : (
          <span className="out-of-stock">Out of Stock</span>
        )}
    <button 
      className="btn-add-cart"
    >
      Add to Cart
    </button>
      </div>
    </div>
  );
}

function getSeverityClass(severity) {
  switch (severity) {
    case 'critical': return 'critical';
    case 'high': return 'high';
    case 'medium': return 'medium';
    case 'none': return 'healthy';
    default: return 'unknown';
  }
}

function capitalizeFirst(str) {
  return str.charAt(0).toUpperCase() + str.slice(1);
}