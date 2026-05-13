from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def curriculo():
    dados = {
        "nome": "Matheus Gabriel Oliveira Martins",
        "telefone": "(31) 99289-9816",
        "email": "matheus@mundowap.com.br",
        "escolas": [
            "COTEMIG - Curso Tecnico em Informatica",
            "Escola anterior - Ensino Fundamental",
        ],
        "experiencias": [
            "Projeto escolar de desenvolvimento de sites em HTML e CSS",
            "Criacao de sistemas simples usando Python e Flask",
        ],
        "cursos": [
            "Logica de Programacao",
            "HTML e CSS",
            "Python basico",
            "Flask basico",
        ],
        "ingles": "Intermediario",
        "espanhol": "Basico",
    }

    return render_template("curriculo.html", dados=dados)


if __name__ == "__main__":
    app.run(debug=True)
