
#%%
import matplotlib.pyplot as plt
from matplotlib.pyplot import imshow, imread
from matplotlib.animation import ArtistAnimation

fig = plt.figure(figsize=(5,5), dpi=50)
ax = fig.add_axes([0, 0, 1, 1], frameon=False)
ax.set_xticks([])
ax.set_yticks([])

images = []

image1 = imshow(imread("monet.png"), animated=True)
images.append([image1])

image2 = imshow(imread("louvre_small.png"), animated=True)
images.append([image2])

image3 = imshow(imread("vangogh.png"), animated=True)
images.append([image3])

image4 = imshow(imread("persepalis.png"), animated=True)
images.append([image4])

ani = ArtistAnimation(fig, images, interval=2500, blit=False, repeat=True,
                                repeat_delay=1000)
ani.save("images.mp4")
plt.show()
#%%