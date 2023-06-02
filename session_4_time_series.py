# %%
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# %%
t_min = pd.to_datetime("2013-08-25")
t_max = pd.to_datetime("2013-12-15")

# %%
df0 = pd.read_csv("data/water_level_example.csv", parse_dates=["Date", "Time"])
print(df0.head())

# %%
df0 = pd.read_csv("data/water_level_example.csv")
df0 = df0.set_index(pd.to_datetime(df0["Date"].astype(str) + " " + df0["Time"].astype(str)))
print(df0.head())

# %%
df0 = df0.drop(["Date", "Time", "ms"], axis=1)
print(df0.head())

# %%
df0['LEVEL'].plot()

# %%
ax = df0['LEVEL'].plot()
ax.set_xlim("2013-09-15", "2013-10-15")

# %%
df0 = df0.interpolate()
ax = df0['LEVEL'].plot()
ax.set_xlim("2013-09-15", "2013-10-15")

# %%
dfm = pd.read_excel("data/manual_readings.xlsx", index_col=0, parse_dates=True)
# df0['LEVEL'] = -df0['LEVEL']
df0['manual'] = dfm / -100.

fig, ax = plt.subplots()
ax.plot(df0.index, df0['LEVEL'])
ax.plot(df0.index, df0['manual'], 'o')

# %%
wl_offset = np.nanmean(df0['manual'] - df0['LEVEL'])

fig, ax = plt.subplots()
ax.plot(df0.index, wl_offset + df0['LEVEL'])
ax.plot(df0.index, df0['manual'], 'o')

# %%
sheets_dict = pd.read_excel(
    "data/weather_data_by_month.xlsx", 
    index_col=0, 
    parse_dates=True,
    sheet_name=None,
)

# %%
dfd = pd.DataFrame()
for sheet_name, df in sheets_dict.items():
    dfd = pd.concat((dfd, df))

# %%
idx = (dfd.index >= t_min) & (dfd.index <= t_max)
dfd = dfd.loc[idx]


# %%
dfwl = wl_offset + df0["LEVEL"].resample('1D').mean()
dfd['wl'] = dfwl

# %%
p_func_V = np.poly1d(np.loadtxt("p_coef_V_linear.dat"))
p_func_A = np.poly1d(np.loadtxt("p_coef_A_linear.dat"))

dfd["volume"] = p_func_V(dfd["wl"])
dfd["area"] = p_func_A(dfd["wl"])


# %%
dfd.to_excel("daily_wl&meteo_data.xlsx")