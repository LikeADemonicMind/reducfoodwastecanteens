# -*- coding: utf-8 -*-
"""
Created on Wed Jul 19 11:52:44 2023

@author: Utilisateur
"""
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import pandas as pd
import numpy as np
def linear_regression(X_train, X_test, y_train, y_test, df_total):
    regr = LinearRegression(fit_intercept = False)
    # Train the model using the training sets
    regr.fit(X_train, y_train)
    
    # Make predictions using the testing set
    y_pred_train = regr.predict(X_train)
    y_pred = regr.predict(X_test)
    
    # The coefficients
    print("Coefficients: \n", regr.coef_)
    # The mean squared error
    print("Mean squared error: %.2f" % mean_squared_error(y_test, y_pred))
    # The coefficient of determination: 1 is perfect prediction
    print("Coefficient of determination jeu de test: %.2f" % r2_score(y_test, y_pred))
    print("Coefficient of determination jeu d'entraînement: %.2f" % r2_score(y_train, y_pred_train))
    y_reel_pred = pd.DataFrame()
    y_reel_pred["reel"] = y_test
    y_reel_pred["prediction"] = y_pred
    y_reel_pred["prediction"] = y_reel_pred["prediction"].apply(np.ceil)
    y_reel_pred = y_reel_pred.merge(df_total["prevision"], how="inner",left_index=True, right_index=True)
    y_reel_pred["difference_prediction_reel"] = y_reel_pred["prediction"] - y_reel_pred["reel"]
    y_reel_pred["difference_prevision_reel"] = y_reel_pred["prevision"] - y_reel_pred["reel"]
    alpha = ((y_reel_pred[y_reel_pred["difference_prediction_reel"] == y_reel_pred["difference_prediction_reel"].min()]["reel"])-200)/(y_reel_pred[y_reel_pred["difference_prediction_reel"] == y_reel_pred["difference_prediction_reel"].min()]["prediction"])
    alpha = alpha.values
    y_reel_pred["prediction_marge"] = y_reel_pred["prediction"]*alpha
    y_reel_pred["prediction_marge"] = y_reel_pred["prediction_marge"].apply(np.ceil)
    y_reel_pred["difference_prediction_marge_reel"] = y_reel_pred["prediction_marge"] - y_reel_pred["reel"]
    difference_prediction_marge_prevision = (y_reel_pred[y_reel_pred["difference_prediction_marge_reel"]>0]["difference_prevision_reel"].sum()) - (y_reel_pred[y_reel_pred["difference_prediction_marge_reel"]>0]["difference_prediction_marge_reel"].sum())
    gaspillage_evite = difference_prediction_marge_prevision/(y_reel_pred[y_reel_pred["difference_prediction_marge_reel"]>0]["difference_prevision_reel"].sum())*100
    print("Ainsi, on pourrait éviter",np.ceil(gaspillage_evite),"% de gaspillage alimentaire.") 
    x_ax = range(len(y_test))
    plt.plot(x_ax, y_test, linewidth=1, label="original")
    plt.plot(x_ax, y_reel_pred['prediction_marge'], linewidth=1.1, label="predicted")
    plt.plot(x_ax, y_reel_pred['prevision'], linewidth=1.1, label="previsions from canteens")
    plt.title("y-test and y-predicted data with linear regression")
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.legend(loc='best',fancybox=True, shadow=True)
    plt.grid(True)
    plt.show()