from flask import render_template, request, redirect, session, flash, url_for, jsonify
from models import *
from werkzeug.security import generate_password_hash
from app import app, db
from helpers import *
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt()

#Home
@app.route('/')
def index():
    ''' Exibe a página inicial, o feed.'''
    #return render_template('Home.jsx')
    pass        

# Registro de user
@app.route('/register')
def user_register():
    '''Exibe o formulário de registro.'''
    #return render_template('NovoRegistro.jsx')
    pass

@app.route("/register_create", methods=["POST"])
def register_create():
    email = request.json.get("email")
    senha = request.json.get("senha")
    nome = request.json.get("nome")

    if not email or not senha or not nome:
        return jsonify({"error": "Dados inválidos"}), 400

    user_exists = Usuarios.query.filter_by(email=email).first()
    if user_exists:
        return jsonify({"error": "Usuário já existe"}), 409

    hashed_password = bcrypt.generate_password_hash(senha).decode('utf-8')
    new_user = Usuarios(nome=nome, email=email, username=nome, password_hash=hashed_password)
    db.session.add(new_user)
    db.session.commit()

    return jsonify({"message": "Usuário criado com sucesso!"}), 201

# Login
from flask import request, jsonify
from flask_bcrypt import check_password_hash
from models import Usuarios  # Certifique-se de importar o modelo de usuário

@app.route("/login_auth", methods=["POST"])
def login_auth():
    email = request.json.get("email")
    senha = request.json.get("senha")

    if not email or not senha:
        return jsonify({"error": "Dados inválidos"}), 400

    user = Usuarios.query.filter_by(email=email).first()
    if not user or not check_password_hash(user.password_hash, senha):
        return jsonify({"error": "Credenciais inválidas"}), 401

    return jsonify({"message": "Login realizado com sucesso!", "user": user.nome}), 200


# Perfil
@app.route('/profile/<username>' )
def user_profile():
    '''Exibe o perfil do usuário e suas postagens.'''
    #return render_template('PerfilUsuarioPage.jsx')
    pass


# Avaliação local
@app.route('/place/<place_id>/rate', methods=['POST', ])
def post_rating():
    '''Envia avaliações para a postagem.'''
    pass

# Sugerir Local
@app.route('/place_suggestion')
def place_suggest():
    pass
