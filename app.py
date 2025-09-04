from flask import Flask, render_template, request
import math

app = Flask(__name__)

def magnitud(v):
    return round(math.sqrt(v["x"]**2 + v["y"]**2 + v["z"]**2), 3)

@app.route("/", methods=["GET", "POST"])
def index():
    # Valores iniciales
    v1 = {"x": 0, "y": 0, "z": 0}
    v2 = {"x": 0, "y": 0, "z": 0}
    resultados = None

    if request.method == "POST":
        try:
            # Vector 1
            v1["x"] = float(request.form.get("x1", 0))
            v1["y"] = float(request.form.get("y1", 0))
            v1["z"] = float(request.form.get("z1", 0))

            # Vector 2
            v2["x"] = float(request.form.get("x2", 0))
            v2["y"] = float(request.form.get("y2", 0))
            v2["z"] = float(request.form.get("z2", 0))

            # Operaciones
            suma = (v1["x"]+v2["x"], v1["y"]+v2["y"], v1["z"]+v2["z"])
            resta = (v1["x"]-v2["x"], v1["y"]-v2["y"], v1["z"]-v2["z"])
            producto_punto = v1["x"]*v2["x"] + v1["y"]*v2["y"] + v1["z"]*v2["z"]

            resultados = {
                "mag_v1": magnitud(v1),
                "mag_v2": magnitud(v2),
                "suma": suma,
                "resta": resta,
                "producto": producto_punto
            }

        except ValueError:
            pass

    return render_template("index.html", v1=v1, v2=v2, resultados=resultados)

if __name__ == "__main__":
    app.run(debug=True)
