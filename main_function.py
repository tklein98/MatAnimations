# This just has a new header hehe

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from animations.anim1 import anim1
from animations.anim1 import anim2

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

# Create rain data
n_drops = 500
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
linewidth = 3
scat = ax.scatter(rain_drops['position'][:, 0], rain_drops['position'][:, 1],
                  s=rain_drops['size'], lw=linewidth, edgecolors=rain_drops['frame'],
                  facecolors=(0.9, 0, 0.9, 0.9))

# This is the master function controlling when to switch from one animation
# to another
def master(frame_number):
    timestamps = [10,100]

    global n_drops
    global COUNT
    global linewidth
    # Define how long every animation should last

    if COUNT <= timestamps[0]:
        linewidth = 10
        anim1(frame_number, rain_drops, n_drops=3, scat=scat)
        COUNT += 1
    if timestamps[0] < COUNT < timestamps[1]:
        linewidth = 10
        anim2(frame_number, rain_drops, n_drops=500, scat=scat)

# Construct the animation, using the update function as the animation director.
animation = FuncAnimation(fig, master, interval=100)
plt.show()

