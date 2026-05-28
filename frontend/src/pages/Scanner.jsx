import React, { useState } from 'react';
import '../styles/Scanner.css';

const API_URL = import.meta.env.VITE_API_URL || 'http://localhost:8000/api';

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
      setError('Please select an image');
      return;
    }

    setLoading(true);
    setError(null);
    setResult(null);

    try {
      const formData = new FormData();
      formData.append('file', selectedImage);

      console.log('Sending request to:', `${API_URL}/predict/disease`);

      const response = await fetch(`${API_URL}/predict/disease`, {
        method: 'POST',
        body: formData,
      });

      console.log('Response status:', response.status);

      if (!response.ok) {
        throw new Error(`HTTP ${response.status}: ${response.statusText}`);
      }

      const data = await response.json();
      console.log('Response data:', data);

      setResult(data.prediction);
    } catch (err) {
      console.error('Error:', err);
      setError(err.message || 'Prediction failed. Please try again.');
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="scanner-container">
      <h1>🌿 Scan Your Plant</h1>

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
      </div>

      {preview && (
        <div className="preview-section">
          <img src={preview} alt="Preview" className="preview-image" />
          <button onClick={handlePredict} disabled={loading} className="predict-button">
            {loading ? '⏳ Analyzing...' : '🔍 Analyze Plant'}
          </button>
        </div>
      )}

      {error && (
        <div className="error-message">
          ❌ Error: {error}
        </div>
      )}

      {result && (
        <div className="result-section">
          <h2>✅ Analysis Result</h2>
          <div className="result-card">
            <p><strong>Disease:</strong> {result.disease_name}</p>
            <p><strong>Confidence:</strong> {result.confidence}%</p>
            <p><strong>Status:</strong> Detected</p>
          </div>
        </div>
      )}

      {!selectedImage && (
        <div className="info-section">
          <p>Upload a clear photo of a plant leaf to get started!</p>
        </div>
      )}
    </div>
  );
}