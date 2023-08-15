# -*- coding: utf-8 -*-
"""
Created on Wed Jul 19 11:53:43 2023

@author: Utilisateur
"""
import pandas as pd
import numpy as np
def features(df_total) : 
    #Features engineering
    mois_dummies = pd.get_dummies(df_total.mois,dtype=float)
    jours_dummies = pd.get_dummies(df_total.jour,dtype=float)
    df_total = df_total.join(mois_dummies).join(jours_dummies)
    first_day = ('2010-09-02','2010-09-03', '2011-09-05','2011-09-06', '2012-09-04','2012-09-05','2013-09-03','2013-09-04','2014-09-01','2014-09-02',
                 '2015-08-31','2015-09-01' '2016-09-01', '2016-09-02','2017-09-04','2017-09-05','2018-09-03', '2018-09-04' )
    df_total["first_day"] = np.where(df_total['date'].isin(first_day), True, False) 
    #list = ["viande","poisson", "noel","Janvier","Decembre","Juillet","Juin","Lundi","Novembre","first_day"]
    #for i in list : 
    #    df_total[i] *= df_total["effectif"] #we make the product of each feature with the effectif to have a times coefficient and not a plus one bc whether the effectif changes a lot, it might be a source of error
    #Features choice
    school_years_all = ['2011-2012', '2012-2013', '2013-2014', '2014-2015',"2015-2016", "2016-2017","2017-2018","2018-2019","2019-2020"]
    pred_year = input("What year do you want to make predictions for? (ex: 2018-2019)")
    i = school_years_all.index(pred_year)
    school_years = school_years_all[2:i]
    print(school_years)
    features = ["effectif" ,"viande","poisson", "noel","Janvier","Decembre","Juillet","Juin","Lundi","Novembre","first_day"]
    #Train/test split
    X_train = df_total[df_total.annee_scolaire.isin(school_years)][features]
    X_test = df_total[df_total.annee_scolaire == pred_year][features]
    y_train = df_total[df_total.annee_scolaire.isin(school_years)]["reel"]
    y_test = df_total[df_total.annee_scolaire == pred_year]["reel"]
    return X_train, X_test, y_train, y_test
