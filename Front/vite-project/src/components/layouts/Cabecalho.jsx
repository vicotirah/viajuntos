import React, { useState } from 'react';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { faGlobe, faBars } from '@fortawesome/free-solid-svg-icons';
import AccountCircleIcon from '@mui/icons-material/AccountCircle';
import HomeIcon from '@mui/icons-material/Home';
import './Cabecalho.css';

function Cabecalho() {
  const [menuOpen, setMenuOpen] = useState(false);

  const toggleMenu = () => {
    setMenuOpen(!menuOpen);
  };

  return (
    <header className="cabecalho">
      <div className="cabecalho-left">
        <button className="menu-icon" onClick={toggleMenu}>
          <FontAwesomeIcon icon={faBars} />
        </button>
        <button className="language-icon">
          <FontAwesomeIcon icon={faGlobe} />
        </button>
      </div>
      <h1 className="titulo">Viajuntos</h1>
      <div className="cabecalho-right">
        <button className="home-icon">
          <HomeIcon style={{ fontSize: 24 }} />
        </button>
        <button className="profile-icon">
          <AccountCircleIcon style={{ fontSize: 24 }} />
        </button>
      </div>
      {menuOpen && (
        <nav className="menu-lateral">
          <ul>
            <li><a href="/">Home</a></li>
            <li><a href="/perfil">Perfil</a></li>
            <li><a href="/postagem">Postagem</a></li>
            <li><a href="/registro">Novo Registro</a></li>
            <li><a href="/login">Login</a></li>
            <li><a href="/post/novopost">Nova Postagem</a></li>
          </ul>
        </nav>
      )}
    </header>
  );
}

export default Cabecalho;
