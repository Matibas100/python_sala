"""
ATIVIDADE 02 - Model (tabela Aluno)

Execute:
  python 02_corrigir_model.py
"""

import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
pasta = os.path.abspath(os.path.dirname(__file__))
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + os.path.join(
    pasta, "exercicio.db"
)
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)


class Aluno(db.Model):  # feito
    __tablename__ = "alunos"  # feito

    id = db.Column(db.Integer, primary_key=True)  # feito
    nome = db.Column(db.String(100), nullable=False)  # feito
    email = db.Column(db.String(120), nullable=False)  # feito

    def __repr__(self):
        return f"<Aluno {self.id} {self.nome}>"


with app.app_context():
    db.create_all()  # feito


if __name__ == "__main__":
    with app.app_context():
        print("Tabelas:", db.metadata.tables.keys())
        aluno_teste = Aluno(nome="Teste", email="teste@mail.com")
        db.session.add(aluno_teste)
        db.session.commit()  # feito
        print("Aluno inserido:", aluno_teste)
