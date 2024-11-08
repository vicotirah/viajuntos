import React from 'react';

function PerfilUsuario() {
  return (
    <div className="perfil-usuario">
      <img src="caminho-da-imagem-do-usuario.jpg" alt="Foto do usuário" className="foto-usuario" />
      <p>Matheus Gois</p>
      <button className="botao-adicionar">+</button>
    </div>
  );
}

export default PerfilUsuario;
