import numpy as np
import matplotlib.pyplot as plt
import matplotlib
from matplotlib.colors import Normalize, LinearSegmentedColormap, PowerNorm

colors = [(0, 0, 0), (0.57, 0.91, 0.96), (240, 78, 56), (255, 254, 246)]
colors = [(0.05, 0.05, 0.05), (0.57, 0.91, 0.96), (1, 1, 0.96)]
#colors = [(1, 0, 0), (0, 1, 0), (0, 0, 1)]

cmap = LinearSegmentedColormap.from_list("cmap", colors)
norm = Normalize(vmin=0, vmax=255)
#norm = PowerNorm(gamma=0.9, vmin=0, vmax=255)

beeld = np.load("./last_beeld_900_4.npy")
plt.imshow(beeld, cmap=cmap, norm=norm)
plt.xlim(800, 1200)
plt.ylim(600, 1000)
plt.colorbar()
plt.rcParams.update({'font.size': 32})
plt.rc('axes', labelsize=32)
plt.show()

