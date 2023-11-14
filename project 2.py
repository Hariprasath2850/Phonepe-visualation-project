# project 
import pandas as pd
import mysql.connector as sql
import streamlit as st
import plotly.express as px
import json
import os
os.environ["GIT_PYTHON_REFRESH"] = "quiet"
import git
import numpy as np
# !pip install streamlit_option_menu
# !pip install GitPython
from streamlit_option_menu import option_menu
from PIL import Image

#Cloning from Github
#Using GitBash: cd "C:\Users\harip\OneDrive\Documents\Phonepe"

#git clone "https://github.com/PhonePe/pulse.git"

#Data Transformation
#Dataframe of Aggregated Transactions
path1 = r"C:\Users\harip\OneDrive\Documents\Phonepe\pulse\data\aggregated\transaction\country\india\state"
agg_trans_list = os.listdir(path1)

columns1 = {'State': [], 'Year': [], 'Quarter': [], 'Transaction_type': [], 'Transaction_count': [],
            'Transaction_amount': []}
for state in agg_trans_list:
    cur_state = path1 + "/" + state 
    agg_year_list = os.listdir(cur_state)
    
    for year in agg_year_list:
        cur_year = cur_state + "/" + year 
        agg_file_list = os.listdir(cur_year)
        
        for file in agg_file_list:
            cur_file = cur_year  + "/"+ file
            data = open(cur_file, 'r')
            A = json.load(data)
            
            for i in A['data']['transactionData']:
                name = i['name']
                count = i['paymentInstruments'][0]['count']
                amount = i['paymentInstruments'][0]['amount']
                columns1['Transaction_type'].append(name)
                columns1['Transaction_count'].append(count)
                columns1['Transaction_amount'].append(amount)
                columns1['State'].append(state)
                columns1['Year'].append(year)
                columns1['Quarter'].append(int(file.strip('.json')))
                
df_agg_trans = pd.DataFrame(columns1)
print(df_agg_trans)
#Dataframe of Aggregated User
