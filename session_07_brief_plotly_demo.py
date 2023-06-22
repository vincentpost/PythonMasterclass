# %%
import pandas as pd
import plotly.express as px

# %% 
# Read the data from excel using pandas
df = pd.read_excel('data/water_balance_data.xlsx',
                   index_col=0,
                   parse_dates=True)

pan_factor = 1.2

# %%
# Calculate the volumetric rates
df['P'] = df['area'] * df['rain'] / 1000.
df['E'] = df['area'] * df['evaporation'] / (1000. * pan_factor)
df['dV'] = -df['volume'].diff(periods=-1)
df['I'] = df['P'] - df['E'] - df['dV']

# %%
# Draw a ternary diagram with the water balance components
fig0 = px.scatter_ternary(df[['P', 'E', 'I']], a="P", b="E", c="I")
fig0.show();

# %%
# Draw a stacked bar diagram of the water balance components
fig1 = px.bar(df, x=df.index, y=["P", "E", "I"], title="Water balance components")
fig1.show();