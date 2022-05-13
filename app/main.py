from flask import Flask
from flask import request
from flask import render_template




app = Flask(__name__)


@app.route("/")
def hello():
    return render_template("index.html")
    

@app.route("/sub", methods = ['POST'])
def submit():
    #convert HTML info to python info
    if request.method == "POST":
        name = request.form["username"]

    #python -> HTML
    return render_template("sub.html", name = name)

