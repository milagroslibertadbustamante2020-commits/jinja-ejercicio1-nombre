from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/saludar", methods=["POST"])
def saludar():
    nombre = request.form.get("nombre")
    if not nombre:
        return redirect(url_for("index"))
    return render_template("salida.html", nombre=nombre)

if __name__ == "__main__":
    app.run(debug=True)