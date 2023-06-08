#load libraries
# %%
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import datetime, timedelta

import numpy as np
import pandas as pd
import os

# Set up directories 
# %%
dir_path = os.path.dirname(os.path.realpath(__file__))
dir_to_Save_results = r'D:\00_GPM\09_Tutorilas_notes\Python_Training_AWS\Outputs'

# create a new folder call "homework_results" to ave the excel file
path_to_save_results =os.path.join(dir_to_Save_results,r"homework_2_results")

if not os.path.exists(path_to_save_results):
        os.makedirs(path_to_save_results)
        print(r'Folder to save results did not exist and was created  !')

# load the input data 
folder_path_input_data =r'D:\00_GPM\09_Tutorilas_notes\Python_Training_AWS\Inputs\data'
file_to_open = 'weather_data_by_month.xlsx'

path_to_open = os.path.join(folder_path_input_data,file_to_open)
 
dfd = pd.read_excel(path_to_open, parse_dates=["date"])

# Make the calcualtions:
#%%

# References equiations: 
# https://awschool.talentlms.com/unit/view/id:6029

dfd['es'] = round(0.6108 * np.exp((17.27 * dfd['temperature']) / (dfd['temperature'] + 237.3)),3)
dfd['ea'] = round((dfd['rh']/100)* dfd['es'],3)
dfd['vpd']= round(dfd['es']-dfd['ea'],3)

# Save results in an excel file
#%%

file_name = "vapor_pressure_defficit_results.xlsx"
filePpath= os.path.join(path_to_save_results,file_name)
dfd.to_excel(filePpath, index=False)

#  Make plots
#%%
fig,ax = plt.subplots(3,1, figsize=(10,10))

ax[0].grid()
ax[1].grid()
ax[2].grid()

ax[0].plot(dfd['date'], dfd['es'])
ax[1].plot(dfd['date'], dfd['ea'])
ax[2].plot(dfd['date'], dfd['vpd'])

# Formatting x-axis
ax[0].xaxis.set_major_formatter(mdates.DateFormatter('%d-%m-%Y'))
ax[1].xaxis.set_major_formatter(mdates.DateFormatter('%d-%m-%Y'))
ax[2].xaxis.set_major_formatter(mdates.DateFormatter('%d-%m-%Y'))

fig.autofmt_xdate()
plt.show()

path_to_save_plot = os.path.join(path_to_save_results,"results_homework_2.png")
fig.savefig(path_to_save_plot, dpi=300)
# %%
