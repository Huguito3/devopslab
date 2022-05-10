# from flask import Flask

# app = Flask(__name__)

# @app.route("/")
# def pagina_inicial():
#     return "Hola Mundo - Hugo, Turma Full 03"

# if __name__ == '__main__':
#     app.run()
from flask import Flask
from flask_wtf.csrf import CSRFProtect

app = Flask(__name__)

csrf = CSRFProtect(app)                                                                                                                           

@app.route("/")
def pagina_inicial():
    return "Laboratório Pipeline DevOps"

if __name__ == '__main__':
    app.run()