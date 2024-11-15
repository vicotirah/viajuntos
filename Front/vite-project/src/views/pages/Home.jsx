import React from 'react';
import Cabecalho from '../../components/layouts/Cabecalho';
import BarraPesquisa from '../../components/layouts/BarraPesquisa';
import ListaViagens from '../../components/layouts/ListaViagens';
import MenuFiltro from '../../components/layouts/MenuFiltro';

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
