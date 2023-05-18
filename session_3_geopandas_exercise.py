#%%
#########################################################

# load libraries:

import geopandas as gpd
import matplotlib.pyplot as plt
import numpy as np
import os
import pandas as pd
from scipy.interpolate import griddata
import shapely.geometry as shg
import openpyxl
print("All libraries loaded successfully !")

##########################################################

# Load input data:
print("Changing working fodler...")
from pyproj.datadir import set_data_dir
new_wf= r'D:/00_GPM/09_Tutorilas_notes/Python_Training_AWS/Inputs/data'
set_data_dir(new_wf)
print("new working folder: "  + new_wf)

print( "reading input data file...")
file_name=r'dam_bathymetry.xlsx'
file_path =os.path.join(new_wf,file_name)
df = pd.read_excel(file_path,skiprows=5,usecols="B,E,F",header=None,names=["z", "easting", "northing"],)
print( "File loaded successfully !!")

idx = df['z'] == 0
df = df.loc[~idx]

# create an empty list that will contain touples of points
pt_list = []
for index, row in df.iterrows():
    pt = shg.Point((row["easting"], row["northing"]))
    pt_list.append(pt)

# Create a Geodataframe with the list of points:
gdf = gpd.GeoDataFrame(
    data=df["z"], 
    geometry=pt_list, 
    crs="epsg:32754",
)

#Create the folder to save the shp output:
folder_path_save_points="D:/00_GPM/09_Tutorilas_notes/Python_Training_AWS/Outputs/dam_bathymetry"

if not os.path.exists(folder_path_save_points):
    os.makedirs(folder_path_save_points)
    print('Folder :' + folder_path_save_points + r' was created !')

folder_path_results = r"D:/00_GPM/09_Tutorilas_notes/Python_Training_AWS/Outputs/dam_bathymetry"
shp_name = r"dam_bathymetry.shp"
shp_path =os.path.join(folder_path_results,shp_name)

#save the geodataframe to a shapefile
if not os.path.exists(shp_path):
    gdf.to_file(shp_path)
    print('Layer :' + shp_path + r' did not exits and was created !')


print(r"Shapefile crated successfully at :" + shp_path)

# %%
###################################################################################################
# Load a shapefile with a helper polygon
path_to_load =os.path.join (new_wf,r"helper_poly")
path_shp_helper =os.path.join(path_to_load, r"helper_poly.shp")
gdf_h = gpd.read_file(path_shp_helper)
print("Helper polygon layer loaded successfully !")

# get the geoemtry of this layer:
helper_poly = gdf_h['geometry'][0]
poly_vertices = helper_poly.exterior.xy

print("Geometry of polygon border extracted successfully !")
print("creating a new df with the coordiantes fo the vertices of the helper polygon...")
dfh = pd.DataFrame()
dfh['easting'] = poly_vertices[0]
dfh['northing'] = poly_vertices[1]
dfh['z'] = -20
print("df with the geoemtry of the helper shp created successfully !")

# %%
##############################################################################################
# Create a single df with all the points 

# here you join the df you have created from excel with the one created with the helper !
df = pd.concat((df, dfh))
print( "the two dfs have been merged ! " )
print('Now your df have the original points + the points in the border...')

# This is innecficient but easy to udenrtand
# create arrays for each diemnsion of the shp file
x = df['easting'].to_numpy()
y = df['northing'].to_numpy()
z = df['z'].to_numpy() / 100. # From cm to m

# Now you need to create a grid mesh object to plot

X_EASTING = 279967.34
Y_NORTHING = 6098781.6
dx = 0.5
dy = dx
xi = np.arange(-35., 40.5, dx) + X_EASTING
yi = np.arange(-35, 15.5, dy)  + Y_NORTHING

X, Y = np.meshgrid(xi, yi)

print(r'Plotting the points in a gridmesh...')

plt.plot(X, Y, 'k.')
plt.plot(x, y, 'r.')
print(r'Plot created successfully !')


#%%
######################################################################################
# 2D Interpolation of elevation points + 3D plots of different interpolations methods

folder_path_results = r"D:/00_GPM/09_Tutorilas_notes/Python_Training_AWS/Outputs"

cl_levels = np.arange(-2.75, 0, 0.25)
fig3d = plt.figure()
fig_contours, axs_contours = plt.subplots(ncols=3)

list_of_methods = ["nearest", "cubic", "linear"]

for i, method in enumerate(list_of_methods):
    zi = griddata((x, y), z, (xi[None, :], yi[:, None]), method=method)

    ax = axs_contours[i]
    cs = ax.contourf(X, Y, zi, cl_levels)

    # create 3D figure  
    ax = fig3d.add_subplot(1, 3, i+1, projection='3d')
    ax.plot_wireframe(X, Y, zi, rstride=4, cstride=4) # rstride & cstride control the number fo lines 
    ax.scatter(x, y, z, color='k')
    
    # Helper points
    ax.scatter(x[z==-0.20], y[z==-0.20], z[z==-0.20], color='r')


# here you create a hash list / dictionary to make the interpolation
lvl_lookup = dict(zip(cs.levels, cs.collections))

level_list = []
poly_list = []
for k, v in lvl_lookup.items():
    level_list.append(k)
    xys = v.get_paths()
    xy = xys[0].to_polygons()[0]
    poly_list.append(shg.Polygon(xy))

# Folder to create teh 3d interpolations:
folder_path_contours = os.path.join(folder_path_results,r'interpolated_contours')

if not os.path.exists(folder_path_contours):
    os.makedirs(folder_path_contours)
    print('Folder :' + folder_path_contours + r' was created !')

gdf = gpd.GeoDataFrame(data={'level': level_list}, geometry=poly_list, crs="epsg:32754")

# create the files with the resutls of each interpolation method:
for method in list_of_methods:
    shp_file_name = r'interpolated_contours_' + str(method) + r'.shp'
    shp_path =os.path.join(folder_path_contours,shp_file_name)
    gdf.to_file(shp_path)
print( r'All the interpoaltion alternatives were saved at: ' + folder_path_contours)


#%%
######################################################################################
# 2D Interpolation of elevation points + 3D plots of different interpolations methods

folder_path_results = r"D:/00_GPM/09_Tutorilas_notes/Python_Training_AWS/Outputs"

cl_levels = np.arange(-2.75, 0, 0.25)
fig3d = plt.figure()
fig_contours, axs_contours = plt.subplots(ncols=3)

list_of_methods = ["nearest", "cubic", "linear"]

for i, method in enumerate(list_of_methods):
    zi = griddata((x, y), z, (xi[None, :], yi[:, None]), method=method)

    ax = axs_contours[i]
    cs = ax.contourf(X, Y, zi, cl_levels)

    # create 3D figure  
    ax = fig3d.add_subplot(1, 3, i+1, projection='3d')
    ax.plot_wireframe(X, Y, zi, rstride=4, cstride=4) # rstride & cstride control the number fo lines 
    ax.scatter(x, y, z, color='k')
    
    # Helper points
    ax.scatter(x[z==-0.20], y[z==-0.20], z[z==-0.20], color='r')


# here you create a hash list / dictionary to make the interpolation
lvl_lookup = dict(zip(cs.levels, cs.collections))

level_list = []
poly_list = []
for k, v in lvl_lookup.items():
    level_list.append(k)
    xys = v.get_paths()
    xy = xys[0].to_polygons()[0]
    poly_list.append(shg.Polygon(xy))

# Folder to create teh 3d interpolations:
folder_path_contours = os.path.join(folder_path_results,r'interpolated_contours')

if not os.path.exists(folder_path_contours):
    os.makedirs(folder_path_contours)
    print('Folder :' + folder_path_contours + r' was created !')

gdf = gpd.GeoDataFrame(data={'level': level_list}, geometry=poly_list, crs="epsg:32754")

# create the files with the resutls of each interpolation method:
for method in list_of_methods:
    shp_file_name = r'interpolated_contours_' + str(method) + r'.shp'
    shp_path =os.path.join(folder_path_contours,shp_file_name)
    gdf.to_file(shp_path)
print( r'All the interpoaltion alternatives were saved at: ' + folder_path_contours)


#%%
###############################################################################################################

z_min = int(np.nanmin(zi) * 100) / 100
wls = np.arange(-0.2, z_min, -0.01)

A = []
V = []
for wl in wls:
    wd = wl - zi
    idx = wd > 0
    A.append(np.sum(idx) * dx ** 2)
    V.append(np.sum(wd[idx] * dx ** 2))

df = pd.DataFrame(index=wls)
df['V'] = V
df['A'] = A

# Area
p_coef_A = np.polyfit(wls, A, 6)
p_func_A = np.poly1d(p_coef_A)

# Volume
p_coef_V = np.polyfit(wls, V, 4)
p_func_V = np.poly1d(p_coef_V)


fig_lines, axs = plt.subplots(ncols=2)

# Area
ax = axs[0]
ax.plot(wls, A, 'C0.')
ax.plot(wls, p_func_A(wls), 'C0')
ax.set_ylabel("Area (m$^2$)")

# Volume
ax = axs[1]
ax.plot(wls, V, 'C0.')
ax.plot(wls, p_func_V(wls), 'C0')
ax.set_ylabel("Volume (m$^3$)")

# Set some properties for both graphs
for ax in axs:
    ax.set_xlabel("Water level (m)")
    ax.grid(ls=":")

# %%
