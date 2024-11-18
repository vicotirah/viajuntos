import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import Home from './views/pages/Home';
import PerfilUsuarioPage from './views/pages/PerfilUsuarioPage';
import PostagemPage from './views/pages/PostagemPage';
import NovoRegistro from './views/pages/NovoRegistro'
import Entrada from './views/pages/Entrada';

function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/perfil" element={<PerfilUsuarioPage />} />
        <Route path="/postagem" element={<PostagemPage />} />
        <Route path="/registro" element={<NovoRegistro/>}/>
        <Route path="/login" element={<Entrada/>}/>
      </Routes>
    </Router>
  );
}

export default App;
