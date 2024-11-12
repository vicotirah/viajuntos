// src/pages/PostagemDetalhes.jsx
import React from 'react';
import { useParams } from 'react-router-dom';
//import ImagemPostagem from '../components/ImagemPostagem';
import TextoPostagem from '../components/layout/TextoPostagem';
import Avaliacoes from '../components/layout/Avaliacoes';
import PerfilUsuario from '../components/layout/PerfilUsuario';
import Comentarios from '../components/layout/Comentarios';
import FormularioComentario from '../components/layout/FormularioComentario';

function PostagemDetalhes() {
  const { id } = useParams();

  return (
    <div>
      <ImagemPostagem />
      <TextoPostagem />
      <Avaliacoes />
      <PerfilUsuario />
      <Comentarios />
      <FormularioComentario />
    </div>
  );
}

export default PostagemDetalhes;
