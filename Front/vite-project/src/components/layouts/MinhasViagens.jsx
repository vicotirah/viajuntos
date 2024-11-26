import React from 'react';
import CardMinhasViagens from './CardMinhasViagens';
import './MinhasViagens.css';

const destinos = [
  { name: 'Rio de Janeiro', author: 'Matheus Gois', imageUrl: 'https://plus.unsplash.com/premium_photo-1671211307997-f4f552b0601c?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MXx8UklPJTIwREUlMjBKQU5FSVJPfGVufDB8fDB8fHww' },
  { name: 'Nova Iorque', author: 'Victoria Rocha', imageUrl: 'https://images.unsplash.com/photo-1621693247912-767f47a3c382?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8NHx8c2FsdmFkb3IlMjBiYWhpYXxlbnwwfHwwfHx8MA%3D%3D' },
  { name: 'Paris', author: 'Pedro Guédes', imageUrl: 'https://lh5.googleusercontent.com/proxy/tg03dNssTCYM790rnvZk0WgSftWf9AbXsFO2_qfGgOF3kKSNb10YF5CgHukbkrsQsbVRPXeL6dFvUA6tAiEY7HzoEdDcEq1NvcqQ-b63jQmHkQqbv5dGOtPi71DZWhV2YafKgu44uTPV_A' },
  { name: 'Lençóis Maranhenses', author: 'Thales Miranda', imageUrl: 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQo4uOEBH-uYhsVlMzXRsct6yseifmX90tx7A&s' },
  { name: 'Salvador', author: 'Julia Silva', imageUrl: 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQGkY6TcSsvikfVKVbuHX1dxei6bCVQe4C3Bw&s' },
  { name: 'Japão', author: 'Vitor Souza', imageUrl: 'https://images.unsplash.com/photo-1524413840807-0c3cb6fa808d?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8Mnx8amFwJUMzJUEzb3xlbnwwfHwwfHx8MA%3D%3D' },
];

function MinhasViagens() {
  return (
    <section className="lista-viagens">
      <h2>Minhas Viagens</h2>
      <div className="card-grid">
        {destinos.map((dest, index) => (
          <CardMinhasViagens key={index} {...dest} />
        ))}
      </div>
    </section>
  );
}

export default MinhasViagens;
