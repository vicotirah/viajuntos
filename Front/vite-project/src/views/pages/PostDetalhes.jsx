// src/pages/PostagemDetalhes.jsx
import React from 'react';
import { useParams } from 'react-router-dom';
//import ImagemPostagem from '../components/ImagemPostagem';
import TextoPostagem from '../components/layouts/TextoPostagem';  
import Avaliacoes from '../components/layouts/Avaliacoes';
import PerfilUsuario from '../components/layouts/PerfilUsuario';
import Comentarios from '../components/layouts/Comentarios';
import FormularioComentario from '../components/layouts/FormularioComentario';

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
