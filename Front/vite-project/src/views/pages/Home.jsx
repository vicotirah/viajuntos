// src/pages/Home.jsx
import React from 'react';
import Cabecalho from '../components/layouts/Cabecalho';
import Logo from '../components/layouts/Logo';
import Postagem from '../components/layouts/Postagem';

function Home() {
  return (
    <div>
      <Cabecalho />
      <Logo />
      {/* Exemplo de renderização de uma lista de postagens */}
      <div className="lista-postagens">
        <Postagem />
        <Postagem />
        <Postagem />
      </div>
    </div>
  );
}

export default Home;
