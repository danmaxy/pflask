from flask import Flask, render_template


app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/sobre')
def sobre():
    return render_template('sobre.html')

@app.route('/contato')
def contato():
    return render_template('contato.html')


@app.route('/aluno')
def listar_aluno():
    lista_alunos = [
    (1, "Caio", 20, "Teresina"),
    (2, "Isaac", 21, "Teresina"),
    (3, "Robert", 53, "Teresina"),
    (4, "Samuel", 25, "Teresina"),
]

    return render_template('aluno/lista.html',lista_alunos=lista_alunos)






if __name__ == '__main__':
    app.run(debug=True)

