#%%
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Read the Data, two product test scores, and result 1 means accepted and 0 means rejected
folder_path_to_load_inputs =r'D:\00_GPM\09_Tutorilas_notes\Python_Training_AWS\Inputs\downloads'
file_to_load = os.path.join(folder_path_to_load_inputs,'test_scores_results.txt')
scores_data = pd.read_csv(file_to_load,header=None)

# Add columns labels to the data
columns = ['Test1_Score', 'Test2_Score', 'Accepted']
scores_data = np.array(scores_data)
df = pd.DataFrame(data=scores_data, columns=columns)

# Separate Accepted and Rejected cases
df_accepted = df[(df['Accepted'] == 1.0)]
df_rejected = df[(df['Accepted'] == 0.0)]

# split scores to x and y co-ordinates to be able to plot in 2D
accepted_score1 = np.array(df_accepted)[:,0]
accepted_score2 = np.array(df_accepted)[:,1]
rejected_score1 = np.array(df_rejected)[:,0]
rejected_score2 = np.array(df_rejected)[:,1]

# Plot the data for visualisation
fig = plt.figure(figsize=(12,8))

ax = fig.add_subplot(121)
ax.plot(accepted_score1, accepted_score2, 'gD', label='Accepted')
ax.plot(rejected_score1, rejected_score2, 'ro', label='rejected')

plt.xlabel('Test1 Score')
plt.ylabel('Test2 Score')
plt.legend(loc='best')

ax = fig.add_subplot(122, projection='3d')

ax.scatter(accepted_score1, accepted_score2, zs=-0.75, zdir='z', s=50, color='g', marker='D', label='Accepted')
ax.scatter(rejected_score1, rejected_score2, zs=0.75, zdir='y', s=50, color='r', marker='o', label='rejected')

ax.set_xlabel('Test1 Score')
ax.set_ylabel('Test2 Score')
ax.set_zlabel('Test2 Score')
ax.set_zlim(-1, 1)
ax.legend(loc='best')

plt.show()
# %%
