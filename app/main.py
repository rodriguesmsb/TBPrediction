from flask import Flask
from flask import request
from flask import render_template
import app.model as app_functions
import pandas as pd



app = Flask(__name__)

data = pd.read_csv("app/static/data/train.csv")
survived = data[(data['Survived']== 1) & (data["Age"].notnull())]


def calculate_percentage(val, total):
        """Calculates the percentage of a value over a total"""
        percent = np.divide(val, total)

        return percent


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
    
        #return render_template("index.html", prediction_value = prediction_result)
        return render_template("index.html")
    return render_template("index.html")


@app.route('/get_piechart_data')
def get_piechart_data():
    class_labels = ['Class I', 'Class II', 'Class III']
    pclass_percent = calculate_percentage(survived.groupby('Pclass').size().values, survived['PassengerId'].count())*100

    pieChartData = []
    for index, item in enumerate(pclass_percent):
        eachData = {}
        eachData['category'] = class_labels[index]
        eachData['measure'] =  round(item,1)
        pieChartData.append(eachData)

    return jsonify(pieChartData)
    

