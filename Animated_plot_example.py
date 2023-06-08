
#%%
import os
import matplotlib.pyplot as plt
from matplotlib.pyplot import imshow, imread
from matplotlib.animation import ArtistAnimation

# load the input data 
folder_path_input_data      =r'D:\00_GPM\09_Tutorilas_notes\Python_Training_AWS\Inputs\downloads'
folder_path_to_save_results =r'D:\00_GPM\09_Tutorilas_notes\Python_Training_AWS\Outputs'

fig = plt.figure(figsize=(5,5), dpi=100)
ax = fig.add_axes([0, 0, 1, 1], frameon=False)
ax.set_xticks([])
ax.set_yticks([])

images = []

image1 = imshow(imread(os.path.join(folder_path_input_data,"monet.png")), animated=True)
images.append([image1])

image2 = imshow(imread(os.path.join(folder_path_input_data,"louvre_small.png")), animated=True)
images.append([image2])

image3 = imshow(imread(os.path.join(folder_path_input_data,"vangogh.png")), animated=True)
images.append([image3])

image4 = imshow(imread(os.path.join(folder_path_input_data,"persepalis.png")), animated=True)
images.append([image4])

ani = ArtistAnimation(fig, images, interval=2500, blit=False, repeat=True,repeat_delay=1000)

ani.save(os.path.join(folder_path_to_save_results,"example_animations.mp4"))
print(r'Animation saved sucessfully at:' + str(folder_path_to_save_results))
plt.show()
#%%