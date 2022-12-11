from flask import Flask, render_template, request
import calculator as calc

app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")

@app.route("/calculate", methods=["post"])
def calculate():
    num1 = int(request.form.get("num1"))
    num2 = int(request.form.get("num2"))
    result = calc.plus(num1, num2)
    return render_template("index.html", result=result)