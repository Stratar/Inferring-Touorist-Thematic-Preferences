import numpy as np
import pandas as pd
from data_visualisation import corr_heatmap

def correlation(data, theme=None):
    corrs = []
    corr_matrix = data.corr()
    if theme:
        try:
            val_corr = data.corr()[theme]
            corrs.append(val_corr)
            print(theme)
            print(val_corr)
        except ValueError as e:
            print(e)
            
    corr_heatmap(corr_matrix)

def basic_statistics(data):
    correlation(data)
        

