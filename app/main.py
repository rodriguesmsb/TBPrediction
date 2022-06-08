from flask import Flask
from flask import request
from flask import render_template
import app.model as app_functions
import pandas as pd



app = Flask(__name__)


@app.route("/", methods = ['GET','POST'])
def make_pred():

    #get user response
    if request.method == "POST":

        result = request.form.to_dict(flat = False) #convert form to a dict

        #convert dict to a data frame
        result = pd.DataFrame.from_dict(result)
        print(result)
        
    
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

