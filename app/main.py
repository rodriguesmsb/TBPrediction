from flask import Flask
from flask import request
from flask import render_template
from flask import jsonify
import pandas as pd
import lightgbm as lgb

#define a function for prediction
def prediction_prob(data):

    model = lgb.Booster(model_file = 'app/binary.txt')
    #model = lightgbm_classifier = LGBMClassifier(random_state = 42)
    #model.load_model("app/xgb.json")

    return(model.predict(data))



app = Flask(__name__)


@app.route("/", methods = ['GET','POST'])
def make_pred():

    #get user response
    if request.method == "POST":
        #foo

        result = request.form.to_dict(flat = False) #convert form to a dict

        #convert dict to a data frame
        result = pd.DataFrame.from_dict(result)
        
        for col in result.columns:
            result[col] = result[col].astype(int)

        #rename columns
        result.rename(columns = {"sex": "cs_sexo", "esc":"cs_escol_n", "tb":"tratamento",
                                 "alch":"agravalcoo", "drug":"agravdroga",
                                 "tobaco":"agravtabac"}, inplace = True)
        
        #"idade_(18, 35]":"Adult"
        #"idade_(50, 65]":"Older"
        result["Adult"] = result["age"].apply(lambda x: 1 if x >18 and x <= 35 else 0)
        result["Older"] = result["age"].apply(lambda x: 1 if x >50 and x <= 65 else 0)

        #drop age
    
        result.drop(columns = ["age"], inplace = True)


        #reorder columns
        result = result[["cs_sexo",	"cs_escol_n",	"tratamento",
                         "agravalcoo", "hiv", "agravdroga",	"agravtabac",
                         "Adult", "Older"]]
      

        print(result)
        #prob = prediction_prob(result)[0]

        
        data = [
            ("LTFU", 0.5),
            ("Cure", 1 - 0.5)
        ]

        #split data into two list
        labels = [row[0] for row in data]
        values = [row[1] for row in data]

        #return data to other form
      
        return render_template("graph.html", labels = labels, values = values)

    return render_template("index.html")