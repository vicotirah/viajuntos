import React from 'react';
import './CardViagens.css';

function CardViagens({ name, author, imageUrl }) {
  return (
    <div className="card-viagens">
      <img src={imageUrl} alt={name} />
      <h3>{name}</h3>
      <p>Por {author}</p>
    </div>
  );
}

export default CardViagens;