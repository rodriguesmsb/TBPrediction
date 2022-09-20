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
        for col in result.columns:
            result[col] = result[col].astype(int)
        
        result.rename(columns = {"tb": "prior_tb", "drug":"drug_yn", "other":"other_dishx",
                                 "alch":"alcohol_yn", "tobaco":"tobacco_yn",
                                 "race": "cs_raca", "sex": "cs_sexo", "esc":"educ_cat",
                                 "age": "idade", "bf":"benef_gov",
                                 "jail": "pop_liber", "hom": "pop_rua"}, inplace = True)

        ##add new features
        result = app_functions.create_feature(result)
        print(result)


        prob = app_functions.prediction_prob(result)[0]

        
        data = [
            ("Desfavorável", prob),
            ("Favorável", 1 - prob)
        ]

        #split data into two list
        labels = [row[0] for row in data]
        values = [row[1] for row in data]
      
        return render_template("graph.html", labels = labels, values = values)

    return render_template("index.html")