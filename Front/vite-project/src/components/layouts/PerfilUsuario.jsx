import React from 'react';

function PerfilUsuario() {
  return (
    <div className="perfil-usuario">
      <img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTVMfWvzBOAJx9M-P7VDSrT0PhGP3UqTEjDNQp-6twHXvACCwhouMWmVTFEOujDYt6pIz0&usqp=CAU" alt="Foto do usuário" className="foto-usuario" />
      <p>Matheus Gois</p>
      <p>Olá, sou o Matheus e gosto muito de viajar</p>
      <button className="botao-adicionar">+</button>
    </div>
  );
}

export default PerfilUsuario;
