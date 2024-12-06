import React, { useState } from "react";
import Cabecalho from "../../components/layouts/Cabecalho";
import "./NovoRegistro.css";
import axios from "axios";

export default function NovoRegistro() {
  const [email, setEmail] = useState("");
  const [senha, setSenha] = useState("");
  const [nome, setNome] = useState("");

  const registerUser = async () => {
    try {
      const response = await axios.post("http://localhost:5000/register_create", {
        email,
        senha,
        nome,
      });

      alert("Usuário cadastrado com sucesso!");
      window.location.href = "/";
    } catch (error) {
      if (error.response?.status === 409) {
        alert("Usuário já existe.");
      } else {
        alert("Erro ao cadastrar usuário. Tente novamente.");
      }
    }
  };

  return (
    <>
      <Cabecalho />
      <h2>Crie uma conta!</h2>
      <section className="formGeral">
        <form>
          <div className="campo">
            <label>Email:</label>
            <input
              type="text"
              value={email}
              onChange={(e) => setEmail(e.target.value)}
              id="email"
            />
          </div>
          <div className="campo">
            <label>Senha:</label>
            <input
              type="password"
              value={senha}
              onChange={(e) => setSenha(e.target.value)}
              id="senha"
            />
          </div>
          <div className="campo">
            <label>Nome:</label>
            <input
              type="text"
              value={nome}
              onChange={(e) => setNome(e.target.value)}
              id="nome"
            />
          </div>
          <button type="button" onClick={registerUser}>
            Criar conta
          </button>
        </form>
      </section>
    </>
  );
}
