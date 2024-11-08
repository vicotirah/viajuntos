import React, { useState } from 'react';

function FormularioComentario() {
  const [comentario, setComentario] = useState("");

  const handleSubmit = (e) => {
    e.preventDefault();
    console.log("Comentário enviado:", comentario);
    setComentario("");
  };

  return (
    <form className="formulario-comentario" onSubmit={handleSubmit}>
      <input
        type="text"
        placeholder="Adicione um comentário"
        value={comentario}
        onChange={(e) => setComentario(e.target.value)}
      />
      <button type="submit">Enviar</button>
    </form>
  );
}

export default FormularioComentario;
