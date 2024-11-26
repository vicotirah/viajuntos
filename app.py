from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api, Resource
from flask_cors import CORS
import os

app = Flask(__name__,template_folder=os.path.join(os.path.dirname(__file__), 'Front\vite-project\src\views'))
CORS(app)

app.config.from_pyfile('config.py')

db = SQLAlchemy(app)

from views import *

if __name__ == '__main__':
    app.run(debug=True)

