# This just has a new header hehe

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

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
n_drops = 8
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
#
scat = ax.scatter(rain_drops['position'][:, 0], rain_drops['position'][:, 1],
                  s=rain_drops['size'], lw=10, edgecolors=rain_drops['frame'],
                  facecolors=(0.9, 0, 0.9, 0.9))

# This is the master function controlling when to switch from one animation
# to another
def master(frame_number):

    if COUNT < 20:
        anim1(frame_number)


def anim1(frame_number):

    current_index = frame_number % n_drops

    # Updating size
    rain_drops['size'][current_index] = np.random.uniform(5, 30, 1) * \
    current_index**1.2

    # Updating position
    rain_drops['position'][current_index] = np.random.uniform(0, 1, 2)

    #Updating fill
    rain_drops['fill'][current_index] = (np.random.uniform(0.2, 1),
                                         np.random.uniform(0.6, 1),
                                         np.random.uniform(0, 0.4),
                                         1)

    # Updating frame
    rain_drops['frame'][current_index] = (np.random.uniform(0.2, 1),
                                          np.random.uniform(0.6, 1),
                                          np.random.uniform(0, 0.4),
                                          1)

    rain_drops['frame'][:, 3] -= 1.0/len(rain_drops)
    rain_drops['frame'][:, 3] = np.clip(rain_drops['frame'][:, 3], 0, 1)

    rain_drops['fill'][:, 3] -= 1.0/len(rain_drops)
    rain_drops['fill'][:, 3] = np.clip(rain_drops['fill'][:, 3], 0, 1)

    scat.set_edgecolors(rain_drops['frame'])
    scat.set_sizes(rain_drops['size'])
    scat.set_offsets(rain_drops['position'])
    scat.set_facecolors(rain_drops['fill'])

    global COUNT
    COUNT = COUNT+1

# Animation two
def anim2(frame_number):
    current_index = frame_number % n_drops


# Construct the animation, using the update function as the animation director.
animation = FuncAnimation(fig, master, interval=100)

plt.show()
