import React, { useState, useRef, useEffect } from 'react';
import { ArrowLeft, Send, Loader } from 'lucide-react';
import '../styles/Chat.css';

const API_URL = import.meta.env.VITE_API_URL || 'http://localhost:8000/api';

export default function Chat({ onBack }) {
  const [messages, setMessages] = useState([
    {
      id: 1,
      type: 'bot',
      text: '🌿 Hello! I\'m your Plant Disease Expert AI. I can help you with:\n\n✓ Disease identification and symptoms\n✓ Treatment recommendations\n✓ Prevention strategies\n✓ Product suggestions\n✓ Plant care tips\n\nWhat would you like to know about your plants?',
    },
  ]);
  const [input, setInput] = useState('');
  const [loading, setLoading] = useState(false);
  const messagesEndRef = useRef(null);

  const scrollToBottom = () => {
    messagesEndRef.current?.scrollIntoView({ behavior: 'smooth' });
  };

  useEffect(() => {
    scrollToBottom();
  }, [messages]);

  const handleSendMessage = async () => {
    if (!input.trim()) return;

    const userMessage = {
      id: messages.length + 1,
      type: 'user',
      text: input,
    };

    setMessages((prev) => [...prev, userMessage]);
    setInput('');
    setLoading(true);

    try {
      const response = await fetch(`${API_URL}/chat/expert`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          message: input,
          conversation_history: messages,
        }),
      });

      if (!response.ok) {
        throw new Error('Failed to get response');
      }

      const data = await response.json();

      const botMessage = {
        id: messages.length + 2,
        type: 'bot',
        text: data.response,
      };

      setMessages((prev) => [...prev, botMessage]);
    } catch (error) {
      console.error('Error:', error);

      const errorMessage = {
        id: messages.length + 2,
        type: 'bot',
        text: '❌ Sorry, I encountered an error. Please try again.',
      };

      setMessages((prev) => [...prev, errorMessage]);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="chat-container">
      <div className="chat-header">
        <button className="btn-back" onClick={onBack}>
          <ArrowLeft size={20} /> Back
        </button>
        <div className="chat-title">
          <h1>🌿 Plant Expert AI</h1>
          <p>Get instant advice from our AI expert</p>
        </div>
      </div>

      <div className="chat-messages">
        {messages.map((message) => (
          <div key={message.id} className={`message ${message.type}`}>
            <div className={`message-content ${message.type}`}>
              {message.text}
            </div>
          </div>
        ))}

        {loading && (
          <div className="message bot">
            <div className="message-content bot loading">
              <Loader size={20} className="spinner" />
              <span>Thinking...</span>
            </div>
          </div>
        )}

        <div ref={messagesEndRef} />
      </div>

      <div className="chat-input-area">
        <div className="input-wrapper">
          <input
            type="text"
            value={input}
            onChange={(e) => setInput(e.target.value)}
            onKeyPress={(e) => e.key === 'Enter' && handleSendMessage()}
            placeholder="Ask me anything about plant diseases..."
            className="chat-input"
            disabled={loading}
          />
          <button
            onClick={handleSendMessage}
            disabled={loading || !input.trim()}
            className="btn-send"
          >
            <Send size={20} />
          </button>
        </div>
        <p className="input-hint">💡 Tip: Ask about symptoms, treatments, or prevention strategies</p>
      </div>
    </div>
  );
}