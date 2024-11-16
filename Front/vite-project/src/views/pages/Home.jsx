import React from 'react';
import Cabecalho from '../../components/layouts/Cabecalho';
import BarraPesquisa from '../../components/layouts/BarraPesquisa';
import MenuFiltro from '../../components/layouts/MenuFiltro';
import ListaViagens from '../../components/layouts/ListaViagens';
import AcoesNavegacao from '../../components/layouts/AcoesNavegacao';

const Home = () => {
  return (
    <div>
      <Cabecalho />
      <BarraPesquisa />
      <MenuFiltro />
      <h1>Viagens Populares</h1>
      <ListaViagens />
      <AcoesNavegacao />
    </div>
  );
};

export default Home;
