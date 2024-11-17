import React from 'react';
import './CardMinhasViagens.css';

function CardMinhasViagens({ name, author, imageUrl }) {
  return (
    <div className="card-viagens">
      <img src={imageUrl} alt={name} />
    </div>
  );
}

export default CardMinhasViagens;