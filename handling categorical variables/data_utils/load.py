# -*- coding: utf-8 -*-
"""
Created on Wed Jun  1 09:59:53 2016

@author: vitaliyradchenko
"""

import pandas as pd


def load_data(file_name):
    data = pd.read_csv(file_name)
    for i in data.columns:
        if (sum(pd.isnull(data[i])) > 0) and (data[i].dtype == 'O'):
            data[i].fillna('MissingCategory',inplace=True)
        elif (sum(pd.isnull(data[i])) > 0) and (data[i].dtype == 'float64'):
            data[i].fillna(data[i].mode()[0],inplace=True)
            data[i] = data[i].astype(int)
    return data
    
def beautiful_head(df, size_chunk_columns=6, n_rows=5):
    from IPython.core.display import display, HTML

    if type(size_chunk_columns) is list:
        current_column = 0
        for i in size_chunk_columns:
            display(HTML('<style> .df thead tr { background-color: #B0B0B0; } </style>' +
                         df.iloc[:,current_column:current_column+i].head(n_rows).to_html(classes='df')))
            current_column += i
    elif type(size_chunk_columns) is int:
        for i in range(0, df.shape[1], size_chunk_columns):
            display(HTML('<style> .df thead tr { background-color: #B0B0B0; } </style>' +
                         df.iloc[:,i:i+size_chunk_columns].head(n_rows).to_html(classes='df')))