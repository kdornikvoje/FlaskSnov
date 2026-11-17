from flask import Flask, render_template
import random
app = Flask(__name__)

MOSKA_IMENA = ["Luka", "Matej", "Jan", "Žan", "Marko", "Tine"]
ZENSKA_IMENA = ["Ana", "Maja", "Nika", "Eva", "Sara", "Lara"]

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/ljubezen")
def ljubezen():
    mosko_ime = random.choice(MOSKA_IMENA)
    zensko_ime = random.choice(ZENSKA_IMENA)
    odstotek = random.randint(0, 100)
    return render_template(
        "ljubezen.html",
        mosko_ime=mosko_ime,
        zensko_ime=zensko_ime,
        odstotek=odstotek,
    )

@app.route("/o-meni")
def about():
    return render_template("about.html")

@app.route("/met-kocke")
def metkocke():
    cifra = random.randint(1,6)
    return render_template("kocka.html", kocka=cifra)

@app.route("/met-kocke-n/<n>")
def metkocken(n):
    cifra = random.randint(1,int(n))
    return render_template("kocka.html", kocka=cifra)



app.run(debug=True)