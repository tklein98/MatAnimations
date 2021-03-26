
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from animations.anim1 import anim1
from animations.anim1 import anim2
from support_modules.grid import return_grid
from support_modules.tokenize import seperate_words

# plt.rcParams['axes.facecolor'] = 'black'

# Fixing random state for reproducibility
np.random.seed(19680801)

COUNT = 0

# Create new Figure and an Axes which fills it.
fig = plt.figure(figsize=(13, 7.5))
ax = fig.add_axes([0, 0, 1, 1], frameon=False)
ax.set_xlim(0, 1), ax.set_xticks([])
ax.set_ylim(0, 1), ax.set_yticks([])

# Setting the background color
fig.set_facecolor((0, 0, 0))

raw_text = ["And if the snow buries my My neighborhood And if my parents are crying Then I'll dig a tunnel From my window to yours Yeah a tunnel from my window to yours".upper()]

# Create rain data
n_drops = 450
rain_drops = np.zeros(n_drops, dtype=[('position', float, 2),
                                      ('size',     float, 1),
                                      ('growth',   float, 1),
                                      ('frame',    float, 4),
                                      ('fill', float, 4)])

# Initialize the raindrops in random positions and with
# random growth rates.
rain_drops['position'] = np.random.uniform(0, 1, (n_drops, 2))
rain_drops['growth'] = np.random.uniform(50, 200, n_drops)

# Construct the scatter which we will update during animation
# as the raindrops develop.
linewidth = 5
scat = ax.scatter(rain_drops['position'][:, 0], rain_drops['position'][:, 1],
                  s=rain_drops['size'], lw=linewidth, edgecolors=rain_drops['frame'],
                  facecolors=(0.9, 0, 0.9, 0.9), marker='s')

# This is the master function controlling when to switch from one animation
# to another
def master(frame_number):
    timestamps = [50,1000]

    global n_drops
    global COUNT
    global linewidth
    # Define how long every animation should last

    if COUNT <= timestamps[0]:
        anim1(frame_number, rain_drops, n_drops=30, scat=scat)
        COUNT += 1
    if timestamps[0] < COUNT < timestamps[1]:
        # Create array once for animation
        arr = return_grid(n_drops)
        input_text = seperate_words(raw_text)
        anim2(frame_number, rain_drops, n_drops=450, scat=scat, arr=arr, input_array=input_text[0], pause=0.8)

# Construct the animation, using the update function as the animation director.
animation = FuncAnimation(fig, master, interval=20)
plt.show()

