from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/contatos")
def contatos():
    return render_template("contatos.html")


@app.route("/usuario/<nome_usuario>")
def usuario(nome_usuario):
    return render_template("usuario.html", nome_usuario=nome_usuario)


# colocar o site no at
if __name__ == '__main__':
    app.run(debug=True)

# servidor
