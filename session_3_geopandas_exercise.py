conda activate # %%
import geopandas as gpd
import matplotlib.pyplot as plt
import numpy as np
import os
import pandas as pd
from scipy.interpolate import griddata
import shapely.geometry as shg

# %%
# from pyproj.datadir import set_data_dir

# set_data_dir("c:/Users/vince/anaconda3/envs/geopandas_env/Library/share/proj/")
# set_data_dir("c:/Users/VincentPost/anaconda3/envs/geopandas_env/Library/share/proj/")

# %%
df = pd.read_excel(
    "data/dam_bathymetry.xlsx",
    skiprows=5,
    usecols="B,E,F",
    header=None,
    names=["z", "easting", "northing"],
)

# %%
idx = df['z'] == 0
df = df.loc[~idx]

# %%
pt_list = []
for index, row in df.iterrows():
    pt = shg.Point((row["easting"], row["northing"]))
    pt_list.append(pt)

# %%
gdf = gpd.GeoDataFrame(
    data=df["z"], 
    geometry=pt_list, 
    crs="epsg:32754",
)

# %%
# os.mkdir("data/dam_bathymetry/")
gdf.to_file("data/dam_bathymetry/dam_bathymetry.shp")

# %%
gdf_h = gpd.read_file("data/helper_poly/helper_poly.shp")

# %%
helper_poly = gdf_h['geometry'][0]
poly_vertices = helper_poly.exterior.xy

# %%
dfh = pd.DataFrame()
dfh['easting'] = poly_vertices[0]
dfh['northing'] = poly_vertices[1]
dfh['z'] = -20

# %%
df = pd.concat((df, dfh))

# %%
x = df['easting'].to_numpy()
y = df['northing'].to_numpy()
z = df['z'].to_numpy() / 100. # From cm to m

# %%
X_EASTING = 279967.34
Y_NORTHING = 6098781.6
dx = 0.5
dy = dx
xi = np.arange(-35., 40.5, dx) + X_EASTING
yi = np.arange(-35, 15.5, dy)  + Y_NORTHING

# %%
X, Y = np.meshgrid(xi, yi)

# %%
plt.plot(X, Y, 'k.')
plt.plot(x, y, 'r.');

# %%
cl_levels = np.arange(-2.75, 0, 0.25)
fig3d = plt.figure()
fig_contours, axs_contours = plt.subplots(ncols=3)
for i, method in enumerate(["nearest", "cubic", "linear"]):
    zi = griddata((x, y), z, (xi[None, :], yi[:, None]), method=method)

    ax = axs_contours[i]
    cs = ax.contourf(X, Y, zi, cl_levels)

    ax = fig3d.add_subplot(1, 3, i+1, projection='3d')
    ax.plot_wireframe(X, Y, zi, rstride=4, cstride=4)
    ax.scatter(x, y, z, color='k')
    
    # Helper points
    ax.scatter(x[z==-0.20], y[z==-0.20], z[z==-0.20], color='r')


# %%
lvl_lookup = dict(zip(cs.levels, cs.collections))

level_list = []
poly_list = []
for k, v in lvl_lookup.items():
    level_list.append(k)
    xys = v.get_paths()
    xy = xys[0].to_polygons()[0]
    poly_list.append(shg.Polygon(xy))

# %%
os.mkdir("data/interpolated_contours")
gdf = gpd.GeoDataFrame(data={'level': level_list}, geometry=poly_list, crs="epsg:32754")
gdf.to_file(f"data/interpolated_contours/interpolated_contours_{method}.shp")

# %%
z_min = int(np.nanmin(zi) * 100) / 100
wls = np.arange(-0.2, z_min, -0.01)

# %%
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

# %%
# Area
p_coef_A = np.polyfit(wls, A, 6)
p_func_A = np.poly1d(p_coef_A)

# Volume
p_coef_V = np.polyfit(wls, V, 4)
p_func_V = np.poly1d(p_coef_V)

# %%
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
