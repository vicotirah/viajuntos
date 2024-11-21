import React, { useState } from "react";
import Cabecalho from "../../components/layouts/Cabecalho";
//import httpClient from "../httpClient";
import "./NovoRegistro.css"
export default function NovoRegistro() {
  const [email, setEmail] = useState("");
  const [senha, setSenha] = useState("");
  const [nome, setNome] = useState("");

  const registerUser = async () => {
    try {
      const resp = await httpClient.post("//localhost:5000/register_create", {
        email,
        senha,
        nome,
      });

      window.location.href = "/";
    } catch (error) {
      if (error.response && error.response.status === 401) {
        alert("Credenciais inválidas");
      } else {
        alert("Ocorreu um erro. Tente de novo mais tarde");
        window.location.href = "/";
      }
    }
  };

  return (
    <>
      <Cabecalho/>
       <h2>Crie uma conta!</h2>
      <section class="formGeral">
       
        <form>
          <div class="campo">
            <label>Email: </label>
            <input
              type="text"
              value={email}
              onChange={(e) => setEmail(e.target.value)}
              id="email"
            />
          </div>
          <div class="campo">
            <label>senha: </label>
            <input
              type="senha"
              value={senha}
              onChange={(e) => setSenha(e.target.value)}
              id="senha"
            />
          </div>
          <div class="campo">
            <label>Nome: </label>
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
};

