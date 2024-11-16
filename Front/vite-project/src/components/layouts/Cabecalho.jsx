import React from 'react';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { faGlobe, faBars } from '@fortawesome/free-solid-svg-icons';
import AccountCircleIcon from '@mui/icons-material/AccountCircle';
import HomeIcon from '@mui/icons-material/Home';
import './Cabecalho.css';

function Cabecalho() {
  return (
    <header className="cabecalho">
      <div className="cabecalho-left">
        <button className="menu-icon">
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
    </header>
  );
}

export default Cabecalho;
