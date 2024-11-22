import React, { useState } from "react";
import Cabecalho from "../../components/layouts/Cabecalho";
//import httpClient from "./httpClient";
import "./NovoPost.css";

export default function NovoPost() {
  const [resenha, setResenha] = useState("");
  const [imagem, setImagem] = useState(null);
  const [pontosTuristicos, setPontosTuristicos] = useState("");
  const [culinaria, setCulinaria] = useState("");
  const [hospitalidade, setHospitalidade] = useState("");
  const [avaliacaoGeral, setAvaliacaoGeral] = useState("");
  const [avaliacaoComunidade, setAvaliacaoComunidade] = useState("");

  const handleFileChange = (e) => {
    setImagem(e.target.files[0]);
  };

  const submitPost = async () => {
    const formData = new FormData();
    formData.append("resenha", resenha);
    formData.append("imagem", imagem);
    formData.append("pontosTuristicos", pontosTuristicos);
    formData.append("culinaria", culinaria);
    formData.append("hospitalidade", hospitalidade);
    formData.append("avaliacaoGeral", avaliacaoGeral);
    formData.append("avaliacaoComunidade", avaliacaoComunidade);

    try {
      const resp = await httpClient.post("//localhost:5000/novo_post", formData, {
        headers: { "Content-Type": "multipart/form-data" },
      });

      alert("Post criado com sucesso!");
      window.location.href = "/";
    } catch (error) {
      alert("Ocorreu um erro ao criar o post. Tente novamente mais tarde.");
    }
  };

  const renderRadioOptions = (name, value, setValue) => (
    <div className="radio-group">
      {[0, 1, 2, 3, 4, 5].map((score) => (
        <label key={score}>
          <input
            type="radio"
            name={name}
            value={score}
            checked={value === score.toString()}
            onChange={(e) => setValue(e.target.value)}
          />
          {score}
        </label>
      ))}
    </div>
  );

  return (
    <>
      <Cabecalho />
      <h2>Crie seu post!</h2>
      <section className="formGeral">
        
        <form>
          <div className="campo">
            <label>Imagem do Post:</label>
            <input type="file" onChange={handleFileChange} accept="image/*" />
          </div>
          <div className="campo">
            <label>Resenha:</label>
            <textarea
              value={resenha}
              onChange={(e) => setResenha(e.target.value)}
              placeholder="Escreva sua resenha..."
              rows="4"
            ></textarea>
          </div>
          <p>Dê uma nota para as seguintes competências: </p>
          <div className="campo">
            <label>Pontos Turísticos:</label>
            {renderRadioOptions("pontosTuristicos", pontosTuristicos, setPontosTuristicos)}
          </div>
          <div className="campo">
            <label>Culinária:</label>
            {renderRadioOptions("culinaria", culinaria, setCulinaria)}
          </div>
          <div className="campo">
            <label>Hospitalidade:</label>
            {renderRadioOptions("hospitalidade", hospitalidade, setHospitalidade)}
          </div>
          <div className="campo">
            <label>Avaliação Geral:</label>
            {renderRadioOptions("avaliacaoGeral", avaliacaoGeral, setAvaliacaoGeral)}
          </div>
          <div className="campo">
            <label>Avaliação da Comunidade:</label>
            {renderRadioOptions("avaliacaoComunidade", avaliacaoComunidade, setAvaliacaoComunidade)}
          </div>
          <button type="button" onClick={submitPost}>
            Enviar Post
          </button>
        </form>
      </section>
    </>
  );
}
