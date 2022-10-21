# Užduotys
# Sukurti programą, kuri turėtų statinį puslapį, pvz. localhost:5000 su norimu tekstu 
# (rekomenduojama naudoti šablonus)
# Sukurti programą, kuri įvedus norimą žodį adreso eilutėje (po / simbolio) ir paspaudus ENTER, 
# atspausdintų jį penkis kartus.
# Sukurti programą, kuri puslapyje localhost:5000/keliamieji parodytų visus 
# keliamuosius metus nuo 1900 iki 2100 metų.
# Sukurti programą, kuri leistų įvesti metus ir paspaudus patvirtinimo mygtuką parodytų, 
# ar jie yra keliamieji.

from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def pagrindinis():
    return "Labas rytas"

@app.route("/ivesk_zodi/<zod>")
def penki(zod):
    zodziai = (zod + ' ')*5
    return f"{zodziai}"

# @app.route("/<zodis>")
# def penkis_kartus(zodis):
#     zodziai = []
#     for zod in range(6):
#         zodziai.append(zodis)
#     return f"{zodziai}"

@app.route("/keliamieji")
def keliamieji():
    keliamieji_metai = []
    for metai in range(1900, 2101):
        if metai % 4 == 0 and (metai % 100 != 0 or metai % 400 == 0):
            keliamieji_metai.append(metai)
    return render_template("keliamieji.html", keliamieji=keliamieji_metai)

# @app.route("/keliamieji")
# def keliamieji():
#     keliamieji = []
#     for metai in range(1900, 2101):
#         if metai % 4 == 0 and (metai % 100 != 0 or metai % 400 == 0):
#             keliamieji.append(metai)
#     return f"Visi keliamieji metai nuo 1900 iki 2100: {keliamieji}"

@app.route("/ar_keliamieji")
def ar_keliamieji():
    return render_template("ar_keliamieji.html")

@app.route("/ar_keliamieji_rezultatas")
def ar_keliamieji_rezultatas():
    ivesti_metai = int(request.args["metai"])
    if ivesti_metai % 4 == 0 and (ivesti_metai % 100 != 0 or ivesti_metai % 400 == 0):
        atsakymas = "keliamieji"
    else:
        atsakymas = "nekeliamieji"
    return render_template("ar_keliamieji_rezultatas.html", **request.args, atsakymas=atsakymas)

if __name__ == "__main__":
    app.run(debug=True)
