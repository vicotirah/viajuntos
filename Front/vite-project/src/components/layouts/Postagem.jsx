import React from 'react';
import ImagemPostagem from './ImagemPostagem';
import TextoPostagem from './TextoPostagem';
import Avaliacoes from './Avaliacoes';

function Postagem() {
  return (
    <div className="postagem">
      <ImagemPostagem />
      <TextoPostagem />
      <Avaliacoes />
    </div>
  );
}

export default Postagem;
