from flask import Flask
from flask import request
from flask import render_template
from flask import jsonify
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
        under_5, five_to_9, nine_to_12, more_than_12 = app_functions.convert_education(result["esc"][0])

        result.drop(columns = ["esc"], inplace = True)
        
        #add extra columns
        esc_names = ["educ_cat_12+ years", "educ_cat_5-9 years", "educ_cat_9-12 years", "educ_cat_under_5"]
        esc_val = [more_than_12, five_to_9, nine_to_12, under_5]
        for col, value in zip(esc_names, esc_val):
            result[col] = value

        
        data = [
            ("Failure", 0.85),
            ("Sucess", 0.15)
        ]

        #split data into two list

        labels = [row[0] for row in data]
        values = [row[1] for row in data]
      

    
        return render_template("graph.html", labels = labels, values = values)
    return render_template("index.html")
