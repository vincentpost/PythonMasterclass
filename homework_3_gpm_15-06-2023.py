#load libraries
# %%
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import datetime, timedelta

import numpy as np
import pandas as pd
import os

import sys
sys.path.append(r'D:\00_GPM\09_Tutorilas_notes\Python_Training_AWS\develop_gpm')

from isotopes import Isotope

# Set up directories 
# %%
execution_path = os.path.dirname(os.path.realpath(__file__))
dir_to_Save_results = r'D:\00_GPM\09_Tutorilas_notes\Python_Training_AWS\Outputs'

# create a new folder call "homework_results" to save the excel file
path_to_save_results =os.path.join(dir_to_Save_results,r"homework_3_results")

if not os.path.exists(path_to_save_results):
        os.makedirs(path_to_save_results)
        print(r'Folder to save results did not exist and was created  !')

# load the input data 
#%%
folder_path_input_data =r'D:\00_GPM\09_Tutorilas_notes\Python_Training_AWS\Inputs\data'
file_to_open = 'water_balance_data.xlsx'
path_to_open= os.path.join(folder_path_input_data,file_to_open)

# read the data from excel using pandas
df = pd.read_excel(path_to_open,
                   index_col=0,
                   parse_dates=True)

# Constants
#%%
pan_factor = 1.2
Cl_0 = 20 # g/m^3 = mg/l >> amount of chloride in the dam meassured in teh first day
Cl_rain = 5 # g/m^3 = mg/l >> amount of chloride in the rain

# Calculate  Evaporation, P, dV, and I 
#%%

df['E'] = df['area'] * df['evaporation'] / (1000. * pan_factor)
df['P'] = df['area'] * df['rain'] / 1000
df['dV'] = -df['volume'].diff(periods=-1)
df['I'] = df['P'] - df['E'] - df['dV']

# Check variabels before mass balance 
#%%

df[['rain', 'area']].plot(secondary_y='area', figsize=(8,2))

df[['P', 'E', 'I', 'dV']].plot(figsize=(8,2), grid=True)

# Water balance 
#%%

# create empty numpy arrays 
M_Cl_g = np.empty(len(df))
conc_Cl = np.empty(len(df))

# convert the data frame into numpy arrys to make the for loop faster
P = df["P"].to_numpy()
I = df["I"].to_numpy()
V = df["volume"].to_numpy()

# the zip fucntion helps you loop over 3 arrayss simultaneously
# enumerate() adds a counter in your foor loop starting at ZERO

for i, (Vi, Pi, Ii) in enumerate(zip(V, P, I)):
    if i == 0: # First day
        M_Cl_g[0] = Vi * Cl_0 # initial mass of chloride in grams meassured at day ZERO
        conc_Cl[0] = M_Cl_g[0] / Vi # Gives initial concentration aa day ZERO of course!
    else:
        M_Cl_g[i] = M_Cl_g[i - 1] + dM_P - dM_I
        conc_Cl[i] = M_Cl_g[i] / Vi
    
    # change in mass due to rainfall
    dM_P = Cl_rain * Pi
    dM_I = conc_Cl[i] * Ii

df["conc_Cl"] = conc_Cl


fig, ax = plt.subplots(figsize=(8,2))
ax.plot(df.index, df["conc_Cl"])
ax.plot(df.index, df["Cl_sample"], 'o')
# Formatting x-axis
ax.xaxis.set_major_formatter(mdates.DateFormatter('%d-%m-%Y'))
fig.autofmt_xdate()

################################################################################################
# Solution of homework
#%%
V = df["volume"].to_numpy()
P = df["P"].to_numpy()
E = df["E"].to_numpy()
I = df["I"].to_numpy()
Tc = df["temperature"].to_numpy()
RH = df["rh"].to_numpy() / 100.

Deuterium = Isotope("2H")

delta_2H_O = -17
delta_2H_rain =-17
delta_2H_atm= -120

M_2H = np.empty(len(df))
delta_2H = np.empty(len(df))

for i, (Vi, Pi, Ei, Ii, Tci, RHi) in enumerate(zip(V, P, E, I, Tc, RH)):
    if i == 0: # First day
        M_2H[0] = Vi * delta_2H_O
        delta_2H[0] = M_2H[0] / Vi # Gives delta_2H_O of course!
    else:
        M_2H[i] = M_2H[i - 1] + dM_P -dM_E - dM_I
        delta_2H[i] = M_2H[i] / Vi    

    dM_P = delta_2H_rain * Pi
    dM_E = Deuterium.delta_e(Tci, RHi, delta_2H[i], delta_2H_atm) * Ei
    dM_I = delta_2H[i] * Ii

df["delta_2H"] = delta_2H

# Check resutls vs observations
# %%
fig, ax = plt.subplots(figsize=(8,2))
ax.plot(df.index, df["delta_2H"])
ax.plot(df.index, df["delta_2H_sample"], 'o')

# Formatting x-axis
ax.xaxis.set_major_formatter(mdates.DateFormatter('%d-%m-%Y'))
fig.autofmt_xdate()


# %%
