import pandas as pd
from xgboost import XGBClassifier

def convert_education(education):
    if education == 0:
        return [1,0,0,0]
    elif education == 1:
        return [0,1,0,0]
    elif education == 2:
        return [0,0,1,0]
    elif education == 3:
        return [0,0,0,1]

def create_feature(data):

    #add number of comorb.
    data["n_of_morb"] = data[["prior_tb", "hiv", "diabetes", "other_dishx"]].sum(axis = 1)

    #add number of sub abuse
    data["n_sub_abuse"] = data[["drug_yn", "alcohol_yn", "tobacco_yn"]].sum(axis = 1)

    #social index
    data["vulnerability_mix"] = data[["cs_raca", "cs_sexo", "educ_cat"]].sum(axis = 1)

    return data





# def prediction_prob(idade, raca, sexo, prior_tb, hiv, diabetes, outra_disf, droga, alcool, fuma, bf, educacao = []):

#     under_5, five_to_9, nine_to_12, more_than_12 = educacao
#     model = XGBClassifier()
#     model.load_model("app/model.json")
#     return model.predict_proba(data_to_predict)[0][1]

# print(prediction_prob(18, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, [1, 0, 0, 0]))