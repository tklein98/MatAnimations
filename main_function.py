
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from animations.anim1 import anim1, anim2
from animations.anim2 import moving_vertical, moving_vertical_left, moving_vertical_down, moving_vertical_up
from support_modules.grid import return_grid
from support_modules.tokenize import seperate_words

# plt.rcParams['axes.facecolor'] = 'black'

# Fixing random state for reproducibility
np.random.seed(19680801)

COUNT = 0

# Create new Figure and an Axes which fills it.
fig = plt.figure(figsize=(20, 10))
ax = fig.add_axes([0, 0, 1, 1], frameon=False)
ax.set_xlim(0, 1), ax.set_xticks([])
ax.set_ylim(0, 1), ax.set_yticks([])

# Setting the background color
fig.set_facecolor((0, 0, 0))

raw_text = ["Hallo Jannik".upper()]

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
linewidth = 1
scat = ax.scatter(rain_drops['position'][:, 0], rain_drops['position'][:, 1],
                  s=rain_drops['size'], lw=linewidth, edgecolors=rain_drops['frame'],
                  facecolors=(0.9, 0, 0.9, 0.9), marker='s')




def master(frame_number):
    '''This is where the owrder of all animations are controlled'''

    timestamps = [100,200,300]

    global n_drops
    global COUNT
    global linewidth    
    # Define how long every animation should last

    if COUNT <= timestamps[0]:
        anim1(frame_number, rain_drops, n_drops=30, scat=scat)
        COUNT += 1
    
    #TODO: Make every moving vertical/ horizontal function take the information from the previous grid to create seamless transitions + Up Animation does not work yet (deletion of last column has to be adjusted)
    
    elif timestamps[0] <= COUNT < timestamps[1]:
        # Create array once for animation
        arr = return_grid(n_drops)
        moving_vertical(frame_number, rain_drops, n_drops=450, scat=scat, arr=arr)
        COUNT += 1
        
    elif timestamps[1] <= COUNT < timestamps[2]:
        arr = return_grid(n_drops)
        moving_vertical_down(frame_number, rain_drops, n_drops=450, scat=scat, arr=arr)
        COUNT += 1
        # input_text = seperate_words(raw_text)
        # anim2(frame_number, rain_drops, n_drops=450, scat=scat, arr=arr, input_array=input_text[0], pause=0.2)

# Construct the animation, using the update function as the animation director.
animation = FuncAnimation(fig, master, interval=20)
plt.show()

