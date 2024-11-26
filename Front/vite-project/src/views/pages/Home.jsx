import React from 'react';
import Cabecalho from '../../components/layouts/Cabecalho';
import BarraPesquisa from '../../components/layouts/BarraPesquisa';
import MenuFiltro from '../../components/layouts/MenuFiltro';
import ListaViagens from '../../components/layouts/ListaViagens';
import './Home.css'


const Home = () => {
  return (
    <>
    <Cabecalho />
        <BarraPesquisa />
      <div class="home">
        <MenuFiltro />
        <ListaViagens />
      </div>
    </>
  );
};

export default Home;
