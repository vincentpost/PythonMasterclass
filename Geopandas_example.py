

#%%
import os
import geopandas as gpd
import matplotlib.pyplot as plt

plt.style.use('dark_background')
# Downloaded from the Climate Change Knowledge portal by the World Bank Group
# Source URL: http://climate4development.worldbank.org/open/#precipitation

# Locations where Global Weather Stations are that monitor weather changes across the globe
# Though we use .shp file here, it requires corresponding .shx, .sbx etc. all the files part of 
# zip file should be unzipped and placed in working directory. Otherwise, this code fails.

# load the input data 
folder_path_input_data =r'D:\00_GPM\09_Tutorilas_notes\Python_Training_AWS\Inputs\downloads\shps'
file_to_open = 'GRDC.shp'
path_to_open = os.path.join(folder_path_input_data,file_to_open)
 
world_wc = gpd.read_file(path_to_open)
world_wc.head()

# Downloaded from thematicmapping.org
# Source URL http://thematicmapping.org/downloads/world_borders.php

file_to_open = 'TM_WORLD_BORDERS_SIMPL-0.3.shp'
path_to_open = os.path.join(folder_path_input_data,file_to_open)

world_borders = gpd.read_file(path_to_open)
world_borders.head()

# Initialize an figure and an axes as the canvas
fig,ax = plt.subplots(figsize=(12,9))

# Plot Global Weather Change data on ax
world_wc.plot(ax=ax)

# Draw the simple worldmap borders
world_borders.boundary.plot(ax=ax,color='#cccccc',linewidth=0.6)

plt.show()
#%%