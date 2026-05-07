import React from 'react';
import { Leaf, Upload, Brain, ShoppingCart, TrendingUp } from 'lucide-react';
import '../styles/Home.css';

export default function Home({ onNavigate }) {
  return (
    <div className="home-container">
      <nav className="navbar">
        <div className="navbar-content">
          <div className="logo">
            <Leaf size={32} color="#10b981" />
            <h1>LeafCare</h1>
          </div>
          <div className="nav-links">
            <button className="btn-secondary" onClick={() => onNavigate('chat')}>
              💬 Chat with Expert
            </button>
            <button className="btn-secondary" onClick={() => onNavigate('cart')}>
              🛒 Cart
            </button>
            <button className="btn-primary" onClick={() => onNavigate('scanner')}>
              Get Started
            </button>
          </div>
        </div>
      </nav>

      <section className="hero">
        <div className="hero-content">
          <h1 className="hero-title">🌿 AI-Powered Plant Disease Detection</h1>
          <p className="hero-subtitle">
            Identify plant diseases instantly. Get disease impact, severity levels, 
            and personalized product recommendations to save your crops.
          </p>
          
          <div className="cta-buttons">
            <button className="btn-primary-large" onClick={onNavigate}>
              📸 Scan Plant Now
            </button>
            <button className="btn-secondary">Learn More</button>
          </div>

          <div className="stats">
            <div className="stat">
              <div className="stat-number">94.5%</div>
              <div className="stat-label">Accuracy</div>
            </div>
            <div className="stat">
              <div className="stat-number">&lt;2s</div>
              <div className="stat-label">Inference Time</div>
            </div>
            <div className="stat">
              <div className="stat-number">23</div>
              <div className="stat-label">Disease Classes</div>
            </div>
          </div>
        </div>
      </section>

      <section className="features">
        <h2>How It Works</h2>
        <div className="features-grid">
          <FeatureCard
            icon={<Upload size={40} />}
            title="Upload Image"
            description="Take a photo of your plant leaf or upload from gallery"
          />
          <FeatureCard
            icon={<Brain size={40} />}
            title="AI Analysis"
            description="Advanced ML model analyzes and identifies diseases instantly"
          />
          <FeatureCard
            icon={<TrendingUp size={40} />}
            title="Disease Impact"
            description="See severity level, affected parts, and treatment duration"
          />
          <FeatureCard
            icon={<ShoppingCart size={40} />}
            title="Get Solutions"
            description="Receive curated product recommendations to treat the disease"
          />
        </div>
      </section>

      <section className="crops">
        <h2>Crops We Support</h2>
        <div className="crops-list">
          <CropBadge name="🍎 Apple" diseases={4} />
          <CropBadge name="🌽 Corn" diseases={4} />
          <CropBadge name="🫑 Pepper" diseases={3} />
          <CropBadge name="🥔 Potato" diseases={4} />
          <CropBadge name="🍅 Tomato" diseases={8} />
        </div>
      </section>

      <footer className="footer">
        <p>🌾 Helping farmers save crops with AI &copy; 2024</p>
      </footer>
    </div>
  );
}

function FeatureCard({ icon, title, description }) {
  return (
    <div className="feature-card">
      <div className="feature-icon">{icon}</div>
      <h3>{title}</h3>
      <p>{description}</p>
    </div>
  );
}

function CropBadge({ name, diseases }) {
  return (
    <div className="crop-badge">
      <div className="crop-name">{name}</div>
      <div className="crop-diseases">{diseases} diseases</div>
    </div>
  );
}