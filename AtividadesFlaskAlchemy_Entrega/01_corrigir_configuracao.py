"""
ATIVIDADE 01 - Configuracao Flask + SQLAlchemy

Execute:
  python 01_corrigir_configuracao.py
"""

import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy  # feito


app = Flask(__name__)
pasta = os.path.abspath(os.path.dirname(__file__))

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + os.path.join(
    pasta, "exercicio.db"
)  # feito
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)  # feito


if __name__ == "__main__":
    print("Configuracao OK! Banco:", app.config["SQLALCHEMY_DATABASE_URI"])
    print("Objeto db:", db)
