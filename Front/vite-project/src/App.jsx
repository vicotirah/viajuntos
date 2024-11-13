import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Cabecalho from './components/layouts/Cabecalho';
import BarraPesquisa from './components/layouts/BarraPesquisa';
import ListaViagens from './components/layouts/ListaViagens';
import MenuFiltro from './components/layouts/MenuFiltro';

// Importação das páginas com o caminho atualizado
import Home from './views/pages/Home';
import PostagemDetalhes from './views/pages/PostDetalhes';
import PerfilUsuario from './components/layouts/PerfilUsuario';

function App() {
  return (
    <Router>
      <div>
        <Cabecalho />
        <BarraPesquisa />
        <div className="main-container">
          <MenuFiltro />
          <ListaViagens />
        </div>

        {/* Rotas para as páginas */}
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/postagem/:id" element={<PostagemDetalhes />} />
          <Route path="/perfil/:userId" element={<PerfilUsuario />} />
        </Routes>
      </div>
    </Router>
  );
}

export default App;
