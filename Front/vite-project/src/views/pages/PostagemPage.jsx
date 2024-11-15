import React from 'react';
import Cabecalho from '../../components/layouts/Cabecalho';
import Postagem from '../../components/layouts/Postagem';
import ImagemPostagem from '../../components/layouts/ImagemPostagem';
import TextoPostagem from '../../components/layouts/TextoPostagem';
import Comentarios from '../../components/layouts/Comentarios';
import FormularioComentarios from '../../components/layouts/FormularioComentario';

const PostagemPage = () => {
    return (
        <div>
            <Cabecalho />
            <Postagem>
                <ImagemPostagem />
                <TextoPostagem />
            </Postagem>
            <Comentarios />
            <FormularioComentarios />
        </div>
    );
};

export default PostagemPage;
