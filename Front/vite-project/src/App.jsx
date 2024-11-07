import React from 'react';
import Cabecalho from './components/layouts/Cabecalho';
import BarraPesquisa from './components/layouts/BarraPesquisa';
import ListaViagens from './components/layouts/ListaViagens';
import MenuFiltro from './components/layouts/MenuFiltro';

function App() {
  return (
    <div>
      <Cabecalho />
      <BarraPesquisa />
      <div className="main-container">
        <MenuFiltro />
        <ListaViagens />
      </div>
    </div>
  );
}

export default App;