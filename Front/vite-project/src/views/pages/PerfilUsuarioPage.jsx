import React from 'react';
import Cabecalho from '../../components/layouts/Cabecalho';
import PerfilUsuario from '../../components/layouts/PerfilUsuario';
import ListaViagens from '../../components/layouts/ListaViagens';

const PerfilUsuarioPage = () => {
    return (
        <div>
            <Cabecalho />
            <PerfilUsuario />
            <ListaViagens />
        </div>
    );
};

export default PerfilUsuarioPage;
