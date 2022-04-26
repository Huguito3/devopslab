from flask import Flask

app = Flask(__name__)

@app.route("/")
def pagina_inicial():
    return "Hola Mundo - Hugo, Turma Full 03"

if __name__ == '__main__':
    app.run()