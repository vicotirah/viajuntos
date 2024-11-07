import React from 'react';
import './Cabecalho.css';

function Cabecalho() {
  return (
    <header className="cabecalho">
      <h1>Viajuntos</h1>
      <nav>
        <button className="menu-icon">☰</button>
        <button className="profile-icon">👤</button>
      </nav>
    </header>
  );
}

export default Cabecalho;