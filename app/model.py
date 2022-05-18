import pandas as pd
from xgboost import XGBClassifier

model = XGBClassifier()
model.load_model("model.json")

data_to_predict = pd.DataFrame.from_dict({"idade": [69], "cs_raca": [1], "cs_sexo": [1], "prior_tb": [1], "hiv": [1], "diabetes": [1], "other_dishx": [1],
                                          "drug_yn": [1], "alcohol_yn": [1], "tobacco_yn": [1], "benef_gov": [1], "educ_cat_12+ years": [0], 
                                          "educ_cat_5-9 years": [0], "educ_cat_9-12 years": [0], "educ_cat_under_5": [0]})
print(model.predict_proba(data_to_predict)[0][1])