import React, { useState } from "react";
import Cabecalho from "../../components/layouts/Cabecalho";
import axios from "axios"; // Certifique-se de importar o axios para fazer as requisições HTTP
import "./Entrada.css";

export default function Entrada() {
  const [email, setEmail] = useState("");
  const [senha, setSenha] = useState("");

  const logInUser = async () => {
    try {
      const resp = await axios.post("http://localhost:5000/login_auth", {
        email,
        senha,
      });

      alert(resp.data.message);
      window.location.href = "/";
    } catch (error) {
      if (error.response && error.response.status === 401) {
        alert("Credenciais inválidas");
      } else {
        alert("Ocorreu um erro. Tente de novo mais tarde.");
      }
    }
  };

  return (
    <>
      <Cabecalho />
      <h2>Entre em sua conta!</h2>

      <section className="formGeral">
        <form>
          <div className="campo">
            <label>Email: </label>
            <input
              type="text"
              value={email}
              onChange={(e) => setEmail(e.target.value)}
              id="email"
            />
          </div>
          <div className="campo">
            <label>Senha: </label>
            <input
              type="password"
              value={senha}
              onChange={(e) => setSenha(e.target.value)}
              id="senha"
            />
          </div>
          <button type="button" onClick={logInUser}>
            Entrar
          </button>
        </form>
      </section>
    </>
  );
}
