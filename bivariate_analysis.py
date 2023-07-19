# -*- coding: utf-8 -*-
"""
Created on Wed Jul 19 10:09:38 2023

@author: Utilisateur
"""
from cleaning_and_merging import cleaning_and_merging
import seaborn as sns
import matplotlib.pyplot as plt 

df_total = cleaning_and_merging()
print(df_total)


def bivariate_analysis(df_total):
    """
    

    Parameters
    ----------
    df_total : dataframe to use to make the bivariate analysis.

    Returns
    -------
    Plots "frequentation" by "potential features" to see if there's any correlation between them.

    """
    jour =['Lundi', 'Mardi', 'Jeudi', 'Vendredi']
    months = ['Janvier', 'Fevrier', 'Mars', 'Avril', 'Mai', 'Juin', 'Juillet',
       'Septembre', 'Octobre', 'Novembre', 'Decembre']
    def make_sorter(l):
        """
        

        Parameters
        ----------
        l : the parameters we want to sort by.

        Returns
        -------
        A sorter that sort by the parameters we want.

        """
        sort_order = {k:v for k,v in zip(l, range(len(l)))}
        return lambda s: s.map(lambda x: sort_order[x])
    df_total.sort_values(by=['mois','jour'], key=make_sorter(months+jour), inplace=True) #sort df_total by month and then day to so January to December and Monday to Friday to have a logic for the x-axis 
    col = ['annee_scolaire', 'jour', 'semaine', 'mois', 'veille_ferie', 'retour_ferie', 'retour_vacances','veille_vacances', 'fete_musulmane', 
       'ramadan', 'fete_chretienne', 'fete_juive', 'porc', 'viande','poisson', 'bio', 'noel', 'frites', 'an_chinois']

    fig, axes = plt.subplots(len(col), 1, figsize=(10, len(col)*5), sharey=True)
    
    for i, col_name in enumerate(col):
        sns.boxplot(x=df_total[col_name], y=df_total["frequentation"],ax=axes[i])
        axes[i].set_xticklabels(axes[i].get_xticklabels(), rotation=90)
    
    plt.tight_layout()
    
    plt.show()

bivariate_analysis(df_total)
