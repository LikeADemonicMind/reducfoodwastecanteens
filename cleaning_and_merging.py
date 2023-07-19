# -*- coding: utf-8 -*-
"""
Created on Wed Jul 19 09:53:40 2023

@author: Utilisateur
"""

#Import of needed librairies
import pandas as pd



def cleaning_and_merging() :
    """
    

    Parameters
    ----------
    

    Returns
    -------
    df_total : cleaning the dataframes after a univariate analysis (deleting non-sense values and outliers) and then merging the two dataframes by date to have a complete dataframe which allows to make further analysis (bivariate for example).

    """
    #Reading of csv files
    frequentation = pd.read_csv("frequentation.csv", index_col = "Unnamed: 0")
    menus = pd.read_csv("menus.csv", index_col = "Unnamed: 0")
    
    #Cleaning before merging. All choices have been made thanks to 
    #univariate analysis but won't be justified in this file. If you wanna see how
    #they have been made, I let you check the notebook file in main. 
    frequentation["frequentation"] = frequentation["reel"]/frequentation["effectif"]*100 #creating a new column which corresponds to the frequentation
    frequentation = frequentation[frequentation["prevision"] > 0] #keeping only prevision values which are > 0
    frequentation = frequentation[(60 < frequentation["frequentation"])] #keeping only frequention values which are > 60% (deleting outliers)
    frequentation.drop(frequentation[frequentation['vacances'] == 1].index, inplace = True) #deleting rows whose "vacations" are true since canteen is supposed to be closed in vacation
    frequentation.drop(frequentation[frequentation['greves'] == 1].index, inplace = True) #deleting rows whose "strike" are true since we can't predict them one month before
    frequentation.drop(frequentation[frequentation['jour'] == "Mercredi"].index, inplace = True) #deleting rows whose "wednesday" are true since canteen is supposed to be close on Wednesday
    #Merging the two dataframes
    df_total = frequentation.merge(menus, on = "date", how="inner")
    return df_total