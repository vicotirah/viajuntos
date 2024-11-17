import React from 'react';
import Cabecalho from '../../components/layouts/Cabecalho';
import BarraPesquisa from '../../components/layouts/BarraPesquisa';
import MenuFiltro from '../../components/layouts/MenuFiltro';
import ListaViagens from '../../components/layouts/ListaViagens';


const Home = () => {
  return (
    <div>
      <Cabecalho />
      <BarraPesquisa />
      <MenuFiltro />
      <ListaViagens />
    </div>
  );
};

export default Home;
