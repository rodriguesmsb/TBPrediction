import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression



def point_prediction(new_point):
    X_train = pd.DataFrame.from_dict({"X": np.random.normal(0, 0.1, 10000)})
    y_train = pd.DataFrame.from_dict({"y": np.random.normal(0, 0.1, 10000)})


    model = LinearRegression()

    model.fit(X_train, y_train)


    X_test = np.array(new_point)
    X_test = X_test.reshape((1,-1))

    return model.predict(X_test)[0]

#point_prediction(new_point)

