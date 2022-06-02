import pandas as pd
from tkinter import *

def adddata_fe(datasets_global_var, options_datasets):
    filename = filedialog.askopenfilename(initialdir="/", title="Select a CSV File",
                                          filetypes=(("CSV Files", "*.csv"),))
    if filename == '':
        return datasets_global_var, options_datasets
    df = pd.read_csv(filename)
    datasets_global_var.append(df)
    options_datasets.append(filename)
    return datasets_global_var, options_datasets

def getheaders_fe(clicked_option_data,datasets_global_var):
    data = datasets_global_var[clicked_option_data]
    return data.columns.to_list()
    #print(clicked_option_data)