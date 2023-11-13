from flask import Flask
from flask.cli import FlaskGroup

app = Flask(__name__)

app.config.from_object('config')
manager = FlaskGroup(app)

from app.controllers import default
from app.controllers import validar_cpf