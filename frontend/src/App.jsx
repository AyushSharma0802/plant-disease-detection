import React, { useState } from 'react';
import './App.css';
import Home from './pages/Home';
import Scanner from './pages/Scanner';
import Cart from './pages/Cart';
import Chat from './pages/Chat';
import { CartProvider } from './context/CartContext';

function App() {
  const [currentPage, setCurrentPage] = useState('home');

  return (
    <CartProvider>
      <div className="App">
        {currentPage === 'home' && (
          <Home onNavigate={(page) => setCurrentPage(page)} />
        )}

        {currentPage === 'scanner' && (
          <Scanner onBack={() => setCurrentPage('home')} />
        )}

        {currentPage === 'cart' && (
          <Cart onBack={() => setCurrentPage('home')} />
        )}

        {currentPage === 'chat' && (
          <Chat onBack={() => setCurrentPage('home')} />
        )}
      </div>
    </CartProvider>
  );
}

export default App;