# -*- coding: utf-8 -*-
"""
Created on Wed Jul 19 09:52:57 2023

@author: Utilisateur
"""

from cleaning_and_merging import cleaning_and_merging
from features import features
from linearregression import linear_regression

def main():
    df_total=cleaning_and_merging()
    print(df_total)
    X_train, X_test, y_train, y_test = features(df_total)
    print(X_train, X_test, y_train, y_test)
    linear_regression(X_train, X_test, y_train, y_test, df_total)
    
if __name__ == "__main__":
    main()
    