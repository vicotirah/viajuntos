SECRET_KEY = 'viajuntos'

SQLALCHEMY_DATABASE_URI = \
    '{SGBD}://{usuario}:{senha}@{servidor}/{database}'.format(
    SGBD = 'mysql+mysqlconnector',
    usuario = 'root',
    senha = 'SUASENHA',
    servidor = '127.0.0.1',
    database = 'viajuntos'
    )   