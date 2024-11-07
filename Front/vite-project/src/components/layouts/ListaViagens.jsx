import React from 'react';
import CardViagens from './CardViagens';
import './ListaViagens.css';

const destinos = [
  { name: 'Rio de Janeiro', author: 'Matheus Gois', imageUrl: 'https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.melhoresdestinos.com.br%2Fo-que-fazer-no-rio-de-janeiro.html&psig=AOvVaw3_fgfrjSuRe48ZuUfy2z4F&ust=1731109648595000&source=images&cd=vfe&opi=89978449&ved=0CBQQjRxqFwoTCPjsiJm0y4kDFQAAAAAdAAAAABAE' },
  { name: 'Nova Iorque', author: 'Victoria Rocha', imageUrl: 'https://www.google.com/imgres?q=nova%20iorque&imgurl=https%3A%2F%2Fdescubraeua.com.br%2Fwp-content%2Fuploads%2F2020%2F06%2Fmanhattan-nova-york-1024x576.jpg&imgrefurl=https%3A%2F%2Fdescubraeua.com.br%2Fnova-york%2Fonde-fica-nova-york%2F&docid=IcdEbDiLNZ9pvM&tbnid=rXDXcgt04diRrM&vet=12ahUKEwjF0rS_tMuJAxWpH7kGHbUiCZUQM3oECFoQAA..i&w=1024&h=576&hcb=2&ved=2ahUKEwjF0rS_tMuJAxWpH7kGHbUiCZUQM3oECFoQAA' },
  { name: 'Paris', author: 'Pedro Guédes', imageUrl: 'link_da_imagem_3' },
  { name: 'Lençóis Maranhenses', author: 'Thales Miranda', imageUrl: 'link_da_imagem_4' },
  { name: 'Salvador', author: 'Julia Silva', imageUrl: 'link_da_imagem_5' },
  { name: 'Japão', author: 'Vitor Souza', imageUrl: 'link_da_imagem_6' },
];

function ListaViagens() {
  return (
    <section className="lista-viagens">
      <h2>Viagens Populares</h2>
      <div className="card-grid">
        {destinos.map((dest, index) => (
          <CardViagens key={index} {...dest} />
        ))}
      </div>
    </section>
  );
}

export default ListaViagens;