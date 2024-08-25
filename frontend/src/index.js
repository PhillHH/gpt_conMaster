import React from 'react';
import ReactDOM from 'react-dom/client'; // Import für createRoot
import App from './App';
import './styles.css';

// Erstelle die Root
const root = ReactDOM.createRoot(document.getElementById('root'));

// Rendere die App in die Root
root.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>
);
