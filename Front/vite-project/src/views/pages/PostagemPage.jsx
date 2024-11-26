import React from 'react';
import Cabecalho from '../../components/layouts/Cabecalho';
import ImagemPostagem from '../../components/layouts/ImagemPostagem';
import TextoPostagem from '../../components/layouts/TextoPostagem';
import Avaliacoes from '../../components/layouts/Avaliacoes';
import Comentarios from '../../components/layouts/Comentarios';
import FormularioComentario from '../../components/layouts/FormularioComentario';

const PostagemPage = () => {
  return (
    <div>
      <Cabecalho />
      <ImagemPostagem />
      <TextoPostagem />
      <Avaliacoes />
      <Comentarios />
      <FormularioComentario />
    </div>
  );
};

export default PostagemPage;
