from flask import Flask
from flask import request
from flask import render_template
import app.model as app_functions



app = Flask(__name__)


@app.route("/", methods = ['GET','POST'])
def make_pred():

    #get user response
    if request.method == "POST":
        age = request.form["age"]
        sex = request.form["sex"]
        raca = request.form["race"]
        escolaridade = request.form["esc"]
        escolaridade = app_functions.convert_education(escolaridade)
        bf = request.form["bf"]


        print(age)
        print(sex)
        print(raca)
        print(escolaridade)
    
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

