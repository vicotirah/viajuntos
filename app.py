from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__,template_folder=os.path.join(os.path.dirname(__file__), 'Front/vite-project/templates'))

app.config.from_pyfile('config.py')

db = SQLAlchemy(app)

from views import *

if __name__ == '__main__':
    app.run(debug=True)

