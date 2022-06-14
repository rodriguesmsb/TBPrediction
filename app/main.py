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

        ##encode race
        

        under_5, five_to_9, nine_to_12, more_than_12 = app_functions.convert_education(result["educ_cat"][0])
        cs_raca_white, cs_raca_mixed, cs_raca_black = app_functions.convert_race(result["cs_raca"][0])
        

        result.drop(columns = ["educ_cat", "cs_raca"], inplace = True)
        
        #add extra columns
     
        esc_names = ["educ_cat_12+ years", "educ_cat_5-9 years", "educ_cat_9-12 years", "educ_cat_under_5"]
        esc_val = [more_than_12, five_to_9, nine_to_12, under_5]
        for col, value in zip(esc_names, esc_val):
            result[col] = value

        raca_names = ["cs_raca_white", "cs_raca_mixed", "cs_raca_black"]
        raca_values = [cs_raca_white, cs_raca_mixed, cs_raca_black]

        for col, value in zip(raca_names, raca_values):
            result[col] = value
        
        print("estou predizendo sim")
        prob = app_functions.prediction_prob(result)[0]


    

        data = [
            ("Failure", prob),
            ("Sucess", 1 - prob)
        ]

        #split data into two list
        labels = [row[0] for row in data]
        values = [row[1] for row in data]
      

    
        return render_template("graph.html", labels = labels, values = values)
    return render_template("index.html")
