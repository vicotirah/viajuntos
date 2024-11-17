// components/MenuFiltro.js
import React from 'react';
import './MenuFiltro.css';

function MenuFiltro() {
  return (
    <aside className="menu-filtro">
      <h3>Filtrar por</h3>
      <select>
        <option>Mais popular</option>
        <option>Menos popular</option>
      </select>
      <div>
      <label className="brasil">Brasil</label>
        <label><input type="checkbox" /> Região Sul</label>
        <label><input type="checkbox" /> Região Sudeste</label>
        <label><input type="checkbox" /> Região Centro-Oeste</label>
        <label><input type="checkbox" /> Região Norte</label>
        <label><input type="checkbox" /> Região Nordeste</label>
      </div>
    </aside>
  );
}

export default MenuFiltro;
