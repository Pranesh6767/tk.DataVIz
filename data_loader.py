'''
MIT License
Copyright (c) 2021 Pranesh6767
Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:
The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
'''
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
