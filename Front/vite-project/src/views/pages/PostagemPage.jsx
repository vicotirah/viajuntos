import React from 'react';
import Cabecalho from '../../components/layouts/Cabecalho';
import ImagemPostagem from '../../components/layouts/ImagemPostagem';
import TextoPostagem from '../../components/layouts/TextoPostagem';
import Avaliacoes from '../../components/layouts/Avaliacoes';
import Comentarios from '../../components/layouts/Comentarios';
import FormularioComentario from '../../components/layouts/FormularioComentario';
import AcoesNavegacao from '../../components/layouts/AcoesNavegacao';

const PostagemPage = () => {
  return (
    <div>
      <Cabecalho />
      <ImagemPostagem />
      <TextoPostagem />
      <Avaliacoes />
      <Comentarios />
      <FormularioComentario />
      <AcoesNavegacao />
    </div>
  );
};

export default PostagemPage;
