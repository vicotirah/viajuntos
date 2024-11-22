import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import Home from './views/pages/Home';
import PerfilUsuarioPage from './views/pages/PerfilUsuarioPage';
import PostagemPage from './views/pages/PostagemPage';
import NovoRegistro from './views/pages/NovoRegistro'
import Entrada from './views/pages/Entrada';
import NovoPost from './views/pages/NovoPost'

function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/perfil" element={<PerfilUsuarioPage />} />
        <Route path="/postagem" element={<PostagemPage />} />
        <Route path="/registro" element={<NovoRegistro/>}/>
        <Route path="/login" element={<Entrada/>}/>
        <Route path="/post/novopost" element={<NovoPost/>}/>
      </Routes>
    </Router>
  );
}

export default App;
