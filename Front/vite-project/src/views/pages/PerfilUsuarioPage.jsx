import React from 'react';
import Cabecalho from '../../components/layouts/Cabecalho';
import PerfilUsuario from '../../components/layouts/PerfilUsuario';
import ListaViagens from '../../components/layouts/ListaViagens';
import AcoesNavegacao from '../../components/layouts/AcoesNavegacao';

const PerfilUsuarioPage = () => {
  return (
    <div>
      <Cabecalho />
      <PerfilUsuario />
      <h1>Minhas Viagens</h1>
      <ListaViagens />
      <AcoesNavegacao />
    </div>
  );
};

export default PerfilUsuarioPage;
