from flask import Flask, render_template

app = Flask(__name__)

@app.route("/") # su siuo dekoratorium nurodom adresa "/" pagrindinio katalogo pagrindinis puslapis
def home():
    return "Veikia"

@app.route("/sveikas/<name>") # narsykleje tarpas yra %20
def user(name):
    return f"Sveikas, {name}"

@app.route("/grazi_diena")
def grazi_diena():
    return render_template("grazi_diena.html")

@app.route("/zmones")
def zmones():
    zmones = ["Justina", "Darius", "Linas", "Arnoldas", "Ingrida", "Ana", "Sergejus", "Simas"]
    return render_template("zmones.html", zmones=zmones)


if __name__ == "__main__":
    app.run(debug=True)

