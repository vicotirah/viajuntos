import React from 'react';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { faUser } from '@fortawesome/free-solid-svg-icons';
import './Cabecalho.css';

function Cabecalho() {
  return (
    <header className="cabecalho">
      <h1>Viajuntos</h1>
      <nav>
        <button className="menu-icon">☰</button>
        <button className="profile-icon">
          <FontAwesomeIcon icon={faUser} />
        </button>
      </nav>
    </header>
  );
}

export default Cabecalho;
