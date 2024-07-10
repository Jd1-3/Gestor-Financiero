from flask import Flask, render_template, request
import Conexion as cn


app = Flask(__name__)

@app.route("/")
def raiz():
    
    return render_template("index.html")






















@app.route("/Gastos", methods=["POST","GET"])
def gastos():
    
    return render_template("gastos.html")

@app.route("/Ingresos", methods=["POST","GET"])
def ingresos():
    
    return render_template("ingresos.html")


if __name__ == "__main__":
    app.run(debug = True, port = 5000)
    
