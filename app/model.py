import pandas as pd
from xgboost import XGBClassifier

def convert_education(education):
    if education == "under_5":
        return [1,0,0,0]
    elif education == "five_to_nine":
        return [0,1,0,0]
    elif education == "nine_to_twelve":
        return [0,0,1,0]
    elif education == "nine_to_twelve":
        return [0,0,0,1]


def prediction_prob(idade, raca, sexo, prior_tb, hiv, diabetes, outra_disf, droga, alcool, fuma, bf, educacao = []):

    under_5, five_to_9, nine_to_12, more_than_12 = educacao
    model = XGBClassifier()
    model.load_model("app/model.json")

    data_to_predict = pd.DataFrame.from_dict({"idade": [idade], "cs_raca": [raca], "cs_sexo": [sexo], "prior_tb": [prior_tb], "hiv": [hiv], 
                                              "diabetes": [diabetes], "other_dishx": [outra_disf], "drug_yn": [droga], 
                                              "alcohol_yn": [alcool], "tobacco_yn": [fuma], "benef_gov": [bf], 
                                              "educ_cat_12+ years": [more_than_12], 
                                              "educ_cat_5-9 years": [five_to_9], "educ_cat_9-12 years": [nine_to_12], "educ_cat_under_5": [under_5]})
    return model.predict_proba(data_to_predict)[0][1]

print(prediction_prob(18, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, [1, 0, 0, 0]))