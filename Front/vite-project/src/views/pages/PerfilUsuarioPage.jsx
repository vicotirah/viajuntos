import React from 'react';
import Cabecalho from '../../components/layouts/Cabecalho';
import PerfilUsuario from '../../components/layouts/PerfilUsuario';
import MinhasViagens from '../../components/layouts/MinhasViagens';

const PerfilUsuarioPage = () => {
  return (
    <div>
      <Cabecalho />
      <PerfilUsuario />
      <MinhasViagens />
    </div>
  );
};

export default PerfilUsuarioPage;
