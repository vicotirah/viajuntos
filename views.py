from flask import render_template, request, redirect, session, flash, url_for
from models import Usuarios, Postagens, Avaliacoes, Comentarios, Seguidores
from app import app, db



#Home
@app.route('/')
def index():
    ''' Exibe a página inicial, o feed.'''
    return render_template('index.html')

# Registro de user
@app.route('/register')
def user_register():
    '''Exibe o formulário de registro.'''
    pass

@app.route('/register_create', methods=['POST', ])
def user_create():
    '''Cria um novo usuário.'''
    pass

# Login
@app.route('/login' )
def login():
    '''Exibe o formulário de login.'''
    pass

@app.route('/login_auth', methods=['POST', ])
def login_auth():
    '''Realiza a autenticação do usuário.'''
    pass

# Perfil
@app.route('/profile/<username>' )
def user_profile():
    '''Exibe o perfil do usuário e suas postagens.'''
    pass

# Criar postagem
@app.route('/post/new' )
def new_post():
    '''Exibe o formulário para criar uma nova postagem.'''
    pass

@app.route('/post/posting', methods=['POST', ] )
def posting():
    '''Cria uma nova postagem.'''
    pass

# Editar postagem
@app.route('/post/edit_post/<post_id>')
def edit_post():
    '''Exibe o formulário para editar a postagem.'''
    pass
@app.route('/post/edit_post/auth/')
def edit_post_auth():
    '''Atualiza a postagem.'''
    pass

# Excluir postagem
@app.route('/post/delete/<post_id>')
def delete_post():
    '''Exclui a postagem.'''
    pass

# Avaliação postagem
@app.route('/post/<post_id>/rate', methods=['POST', ])
def post_rating():
    '''Envia avaliações para a postagem.'''
    pass

#Comentarios
@app.route('/post/<post_id>/comment', methods=['POST', ])
def post_comment():
    '''Adiciona um comentário à postagem.'''
    pass

#Seguidores
@app.route('/follow/<username>')
def follow():
    '''Permite que um usuário siga outro.'''
    pass
