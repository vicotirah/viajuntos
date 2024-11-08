import React from 'react';
import Comentario from './Comentario';

function Comentarios() {
  return (
    <div className="comentarios">
      <h3>Comentários da Comunidade</h3>
      <Comentario nome="Victoria Rocha" conteudo="Adorei!!" />
      <Comentario nome="Fulano da Silva" conteudo="Detesto esse lugar!" />
    </div>
  );
}

export default Comentarios;
