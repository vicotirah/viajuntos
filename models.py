from app import db
from datetime import datetime, timezone
from sqlalchemy import Column, DateTime

class Usuarios(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(25), unique=True, nullable=False)
    nome = db.Column(db.String(50),  nullable=False)
    email = db.Column(db.String(60),  unique=True, nullable=False)
    password_hash = db.Column(db.String(100),  nullable=False)
    def __repr__(self): #representação de objeto
        return f'<Usuário: {self.username}>'
    
class Continentes(db.Model):
    __tablename__ = 'continents'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50),  nullable=False)
    def __repr__(self):
        return f'<Continente: {self.name}>'
    
class Subcontinentes(db.Model):
    __tablename__ = 'subcontinents'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    continent_id = db.Column(db.Integer, db.ForeignKey('continents.id'), nullable=False)
    name = db.Column(db.String(50),  nullable=False)
    def __repr__(self):
        return f'<Subcontinente: {self.name}>'
    
class Country(db.Model):
    __tablename__ = 'country'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    subcontinent_id = db.Column(db.Integer, db.ForeignKey('subcontinents.id'),nullable=False)
    name = db.Column(db.String(50),  nullable=False)
    def __repr__(self):
        return f'<País: {self.name}>'
    
class State(db.Model):
    __tablename__ = 'states'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    country_id = db.Column(db.Integer, db.ForeignKey('country.id'),nullable=False)
    name = db.Column(db.String(50),  nullable=False)
    def __repr__(self):
        return f'<Estado/Província: {self.name}>'
    
class City(db.Model):
    __tablename__ = 'city'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    state_id = db.Column(db.Integer, db.ForeignKey('states.id'),nullable=False)
    name = db.Column(db.String(50),  nullable=False)
    def __repr__(self):
        return f'<Cidade/Povoado: {self.name}>'
    
class Place(db.Model):
    __tablename__ = 'place'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    city_id = db.Column(db.Integer, db.ForeignKey('city.id'),nullable=False)
    name = db.Column(db.String(50),  nullable=False)
    def __repr__(self):
        return f'<Local: {self.name}>'

class Avaliacoes(db.Model):
    __tablename__ = 'avaliacoes'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    place_id= db.Column(db.Integer, db.ForeignKey('lugares.id'), nullable=False)
    user_id= db.Column(db.Integer, db.ForeignKey('usuarios.id'), nullable=False)
    security_rating = db.Column(db.Integer, nullable=False)
    solo_woman_rating = db.Column(db.Integer, nullable=False)
    hospitality_rating = db.Column(db.Integer, nullable=False)
    accessibility_rating = db.Column(db.Integer, nullable=False)
    cuisine_rating = db.Column(db.Integer, nullable=False)
    content = db.Column(db.Text, nullable=False)
    def __repr__(self):
        return f'<Avaliações {self.content}>'
    
class Comentarios(db.Model):
    __tablename__ = 'comentarios'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    place_id= db.Column(db.Integer, db.ForeignKey('lugares.id'), nullable=False)
    user_id= db.Column(db.Integer, db.ForeignKey('usuarios.id'), nullable=False)
    name = db.Column(db.String(150),  nullable=False)
    def __repr__(self):
        return f'<Comentários {self.content}>'

