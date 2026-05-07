import React from 'react';
import { ArrowLeft, Trash2, Plus, Minus } from 'lucide-react';
import { useCart } from '../context/CartContext';
import '../styles/Cart.css';

export default function Cart({ onBack }) {
  const { cartItems, removeFromCart, updateQuantity, getTotalPrice, getTotalItems } = useCart();

  const handleCheckout = () => {
    alert(`Order placed! Total: $${getTotalPrice().toFixed(2)}`);
    // Here you would integrate payment gateway
  };

  return (
    <div className="cart-container">
      <div className="cart-header">
        <button className="btn-back" onClick={onBack}>
          <ArrowLeft size={20} /> Back
        </button>
        <h1>🛒 Shopping Cart</h1>
        <div className="cart-count">{getTotalItems()}</div>
      </div>

      <div className="cart-content">
        {cartItems.length === 0 ? (
          <div className="empty-cart">
            <h2>Your cart is empty</h2>
            <p>Add products from disease recommendations</p>
          </div>
        ) : (
          <>
            <div className="cart-items">
              {cartItems.map((item) => (
                <div key={item.product_id} className="cart-item">
                  <div className="item-info">
                    <h3>{item.name}</h3>
                    <p>{item.description}</p>
                    <div className="item-meta">
                      <span className="efficacy">⭐ {item.rating}</span>
                      <span className="efficacy">{item.efficacy}</span>
                    </div>
                  </div>

                  <div className="item-quantity">
                    <button onClick={() => updateQuantity(item.product_id, item.quantity - 1)}>
                      <Minus size={16} />
                    </button>
                    <input
                      type="number"
                      value={item.quantity}
                      onChange={(e) =>
                        updateQuantity(item.product_id, parseInt(e.target.value) || 1)
                      }
                    />
                    <button onClick={() => updateQuantity(item.product_id, item.quantity + 1)}>
                      <Plus size={16} />
                    </button>
                  </div>

                  <div className="item-price">
                    <div className="unit-price">${item.price}</div>
                    <div className="total-price">${(item.price * item.quantity).toFixed(2)}</div>
                  </div>

                  <button
                    className="btn-remove"
                    onClick={() => removeFromCart(item.product_id)}
                  >
                    <Trash2 size={18} />
                  </button>
                </div>
              ))}
            </div>

            <div className="cart-summary">
              <div className="summary-row">
                <span>Subtotal:</span>
                <span>${getTotalPrice().toFixed(2)}</span>
              </div>
              <div className="summary-row">
                <span>Shipping:</span>
                <span>Free</span>
              </div>
              <div className="summary-row">
                <span>Tax:</span>
                <span>${(getTotalPrice() * 0.1).toFixed(2)}</span>
              </div>
              <div className="summary-row total">
                <span>Total:</span>
                <span>${(getTotalPrice() * 1.1).toFixed(2)}</span>
              </div>

              <button className="btn-checkout" onClick={handleCheckout}>
                💳 Proceed to Checkout
              </button>
            </div>
          </>
        )}
      </div>
    </div>
  );
}