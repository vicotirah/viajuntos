from flask import render_template, request, redirect, session, flash, url_for, jsonify
from models import *
from werkzeug.security import generate_password_hash
from app import app, db
from helpers import *

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
    new_user = Usuarios(email=email, username=nome, password_hash=hashed_password)
    db.session.add(new_user)
    db.session.commit()

    return jsonify({"message": "Usuário criado com sucesso!"}), 201

# Login
@app.route('/login' )
def login():
    '''Exibe o formulário de login.'''
    '''form = FormularioUsuario()
    return render_template('Entrada.jsx', form=form)'''
    pass

@app.route('/login_auth', methods=['POST', ])
def login_auth():
    '''Realiza a autenticação do usuário.'''

    '''
    form = FormularioUsuario(request.form)
    usuario = Usuarios.query.filter_by(email=form.email.data).first()
    senha = Usuarios.query.filter_by(senha=form.senha.data)
    if usuario and senha: 
        session['Usuário logado'] = usuario.username
        flash(usuario.username + 'logado com sucesso')
        return redirect('Home.jsx') #ajustar com url_for
    else:
        flash('Usuário não logado')
        return redirect('Entrada.jsx') #ajustar com url_for'''
    pass
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
