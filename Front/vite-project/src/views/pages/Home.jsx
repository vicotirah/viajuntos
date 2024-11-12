// src/pages/Home.jsx
import React from 'react';
import Cabeçalho from '../components/layout/Cabeçalho';
import Logo from '../components/layout/Logo';
import Postagem from '../components/layout/Postagem';

function Home() {
  return (
    <div>
      <Cabeçalho />
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
