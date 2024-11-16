import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import Home from './views/pages/Home';
import PerfilUsuarioPage from './views/pages/PerfilUsuarioPage';
import PostagemPage from './views/pages/PostagemPage';

function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/perfil" element={<PerfilUsuarioPage />} />
        <Route path="/postagem" element={<PostagemPage />} />
      </Routes>
    </Router>
  );
}

export default App;
