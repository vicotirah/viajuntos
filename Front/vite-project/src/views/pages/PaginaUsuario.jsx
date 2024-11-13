import React from 'react';
import { useParams } from 'react-router-dom';
import PerfilUsuario from '../components/layouts/PerfilUsuario';
import Postagem from '../components/layouts/Postagem';

function PerfilUsuarioPage() {
  const { userId } = useParams();

  return (
    <div>
      <PerfilUsuario />
      <h2>Postagens de {userId}</h2>
      {/* Exemplo de renderização de postagens do usuário */}
      <Postagem />
      <Postagem />
    </div>
  );
}

export default PerfilUsuarioPage;
