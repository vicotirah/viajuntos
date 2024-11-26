import React from 'react';

function Comentario({ nome, conteudo }) {
  return (
    <div className="comentario">
      <p><strong>{nome}:</strong> {conteudo}</p>
    </div>
  );
}

export default Comentario;
