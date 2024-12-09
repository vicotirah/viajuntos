from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api, Resource
from flask_cors import CORS
import os
from flask_migrate import Migrate

app = Flask(__name__, template_folder=os.path.join(os.path.dirname(__file__), 'Front\\vite-project\\src\\views\\pages'))
CORS(app)
CORS(app, origins=["http://localhost:5173"])

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:SUASENHA@localhost:3306/viajuntos'

basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'instance', 'app.db')

app.config.from_pyfile('config.py')

db = SQLAlchemy(app)    
migrate=Migrate(app, db)

from views import *

if __name__ == '__main__':
    app.run(debug=True)
