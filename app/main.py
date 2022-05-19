from flask import Flask
from flask import request
from flask import render_template
import app.model_test as predictor



app = Flask(__name__)


@app.route("/", methods = ['GET','POST'])
def make_pred():

    if request.method == "POST":
        age = request.form["age"]

        print(age)
    
        #return render_template("index.html", prediction_value = prediction_result)
        return render_template("index.html")
    return render_template("index.html")
    
    

# @app.route("/sub", methods = ['POST'])
# def submit():
#     #convert HTML info to python info
#     if request.method == "POST":
#         name = request.form["username"]

#     #python -> HTML
#     return render_template("sub.html", name = name)

