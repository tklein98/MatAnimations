import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Fixing random state for reproducibility
np.random.seed(19680801)

#key parameters
background_color = (0,0,0,1)
fill_color = (1,1,1,0.0)
line_width = 10
number_frames = 200

matrix_vertical = [(0.1,0.0625), 	(0.1,0.1875), 	(0.1,0.3125), 	(0.1,0.4375), 	(0.1,0.5625), 	(0.1,0.6875), 	(0.1,0.8125), 	(0.1,0.9375),
(0.3,0.0625), 	(0.3,0.1875), 	(0.3,0.3125), 	(0.3,0.4375), 	(0.3,0.5625), 	(0.3,0.6875), 	(0.3,0.8125), 	(0.3,0.9375),
(0.5,0.0625), 	(0.5,0.1875), 	(0.5,0.3125), 	(0.5,0.4375), 	(0.5,0.5625), 	(0.5,0.6875), 	(0.5,0.8125), 	(0.5,0.9375),
(0.7,0.0625), 	(0.7,0.1875), 	(0.7,0.3125), 	(0.7,0.4375), 	(0.7,0.5625), 	(0.7,0.6875), 	(0.7,0.8125), 	(0.7,0.9375),
(0.9,0.0625), 	(0.9,0.1875), 	(0.9,0.3125), 	(0.9,0.4375), 	(0.9,0.5625), 	(0.9,0.6875), 	(0.9,0.8125), 	(0.9,0.9375), ]

matrix_horizontal = [(0.0625,0.1),	(0.1875,0.1),	(0.3125,0.1),	(0.4375,0.1),	(0.5625,0.1),	(0.6875,0.1),	(0.8125,0.1),	(0.9375,0.1),
(0.0625,0.3),	(0.1875,0.3),	(0.3125,0.3),	(0.4375,0.3),	(0.5625,0.3),	(0.6875,0.3),	(0.8125,0.3),	(0.9375,0.3),
(0.0625,0.5),	(0.1875,0.5),	(0.3125,0.5),	(0.4375,0.5),	(0.5625,0.5),	(0.6875,0.5),	(0.8125,0.5),	(0.9375,0.5),
(0.0625,0.7),	(0.1875,0.7),	(0.3125,0.7),	(0.4375,0.7),	(0.5625,0.7),	(0.6875,0.7),	(0.8125,0.7),	(0.9375,0.7),
(0.0625,0.9),	(0.1875,0.9),	(0.3125,0.9),	(0.4375,0.9),	(0.5625,0.9),	(0.6875,0.9),	(0.8125,0.9),	(0.9375,0.9),]

# Create new Figure and an Axes which fills it.
fig = plt.figure(figsize=(7, 7))
ax = fig.add_axes([0, 0, 1, 1], frameon=False)
ax.set_xlim(0, 1), ax.set_xticks([])
ax.set_ylim(0, 1), ax.set_yticks([])
fig.set_facecolor(background_color)


# Create rain data
n_drops = 40
rain_drops = np.zeros(n_drops, dtype=[('position', float, 2),
                                      ('size',     float, 1),
                                      ('growth',   float, 1),
                                      ('color',    float, 4),
                                      ('linewidth',float,1)])

# Initialize the raindrops in random positions and with
# random growth rates.
rain_drops['position'] = (0.5,0.5)
rain_drops['growth'] = np.random.uniform(50, 200, n_drops)

# Construct the scatter which we will update during animation
# as the raindrops develop.
#
scat = ax.scatter(rain_drops['position'][:, 0], rain_drops['position'][:, 1],
                  s=rain_drops['size'], lw=rain_drops['linewidth'], edgecolors=rain_drops['color'],
                  facecolors=fill_color)

divider = np.random.randint(40,60)

#Master function calling all Animations
def animation_picker(frame_number):

#    current_index = frame_number % n_drops
#
#    choreos = [rowsup(frame_number),drops(frame_number),colorchanges(frame_number),rowsdown(frame_number),allatonce(frame_number)]
#
#    if frame_number < 40:
#        choreos[0]
#    else:
#        choreos[1]

    animationcount = 5

    if frame_number <number_frames*1/animationcount:
        rowsup(frame_number)
    elif 41 <=frame_number < number_frames*2/animationcount:
        circles(frame_number)
    elif 81 <=frame_number < number_frames*3/animationcount:
        rowsdown(frame_number)
    elif 121 <=frame_number < number_frames*4/animationcount:
        grid(frame_number)
    elif 161<= frame_number < number_frames*5/animationcount:
        color_change_current_circles(frame_number)

def rowsup(frame_number):
    # Get an index which we can use to re-spawn the oldest raindrop.
    current_index = frame_number % n_drops

    rain_drops['linewidth'][current_index] = 3

    # Make all colors more transparent as time progresses.
    rain_drops['color'][:, 3] -= 1/len(rain_drops)
    rain_drops['color'][:, 3] = np.clip(rain_drops['color'][:, 3], 0, 1)

    # Make all circles bigger. The bigger the range, the bigger the circle + space between circles

    rain_drops['size'] += rain_drops['growth']

    # Pick a new position for oldest rain drop, resetting its size,
    # color and growth factor.
    rain_drops['position'][current_index] = matrix_horizontal[current_index]

    rain_drops['size'][current_index] = 30
    rain_drops['color'][current_index] = (np.random.uniform(0.2,1),
    np.random.uniform(0.6,1), np.random.uniform(0,0.4), 1)
    rain_drops['growth'][current_index] = np.random.uniform(50, 200)

    # Update the scatter collection, with the new colors, sizes and positions.
    scat.set_edgecolors(rain_drops['color'])
    scat.set_sizes(rain_drops['size'])
    scat.set_offsets(rain_drops['position'])
    scat.set_linewidth(rain_drops['linewidth'])

def rowsdown(frame_number):
    # Get an index which we can use to re-spawn the oldest raindrop.
    current_index = frame_number % n_drops

    rain_drops['linewidth'][current_index] = 10

    # Make all colors more transparent as time progresses.
    rain_drops['color'][:, 3] -= 1/len(rain_drops)
    rain_drops['color'][:, 3] = np.clip(rain_drops['color'][:, 3], 0, 1)

    # Make all circles bigger. The bigger the range, the bigger the circle + space between circles

    rain_drops['size'] += rain_drops['growth']

    # Position of next cirlce on the grid
    rain_drops['position'][current_index] = matrix_horizontal[-current_index-1]

    #Attributes of newly created cirlce (color, size and growth rate)
    rain_drops['size'][current_index] = 30
    rain_drops['color'][current_index] = (np.random.uniform(0.6,1),
    np.random.uniform(0.1,1), np.random.uniform(0,0.6), 1)
    rain_drops['growth'][current_index] = np.random.uniform(50, 200)

    # Update the scatter collection, with the new colors, sizes and positions.
    scat.set_edgecolors(rain_drops['color'])
    scat.set_sizes(rain_drops['size'])
    scat.set_offsets(rain_drops['position'])
    scat.set_linewidth(rain_drops['linewidth'])

def drops(frame_number):
    # Get an index which we can use to re-spawn the oldest raindrop.
    current_index = frame_number % n_drops

    rain_drops['linewidth'][current_index] = 2

    # Make all colors more transparent as time progresses.
    rain_drops['color'][:, 3] -= 1.0/len(rain_drops)
    rain_drops['color'][:, 3] = np.clip(rain_drops['color'][:, 3], 0, 1)

    # Make all circles bigger.
    rain_drops['size'] += rain_drops['growth']

    # Pick a new position for oldest rain drop, resetting its size,
    # color and growth factor.
    rain_drops['position'][current_index] = np.random.uniform(0, 1, 2)
    rain_drops['size'][current_index] = 5
    rain_drops['color'][current_index] = (np.random.uniform(0,1),
    np.random.uniform(0,1), np.random.uniform(0,1), np.random.uniform(0.5,1))
    rain_drops['growth'][current_index] = np.random.uniform(50, 200)

    # Update the scatter collection, with the new colors, sizes and positions.
    scat.set_edgecolors(rain_drops['color'])
    scat.set_sizes(rain_drops['size'])
    scat.set_offsets(rain_drops['position'])
    scat.set_linewidth(rain_drops['linewidth'])

def circles(frame_number):

    current_index = frame_number % n_drops

    rain_drops['color'][:, 3] -= 1/len(rain_drops)
    rain_drops['color'][:, 3] = np.clip(rain_drops['color'][:, 3], 0, 1)

    rain_drops['size'] += rain_drops['growth']
    rain_drops['linewidth'][current_index] = 5

    rain_drops['position'][current_index] = (0.5,0.5)
    rain_drops['size'][current_index] = 5*current_index**3.4
    rain_drops['color'][current_index] = (np.random.uniform(0,1),
    np.random.uniform(0,1), np.random.uniform(0,1),1)

    scat.set_edgecolors(rain_drops['color'])
    scat.set_sizes(rain_drops['size'])
    scat.set_offsets(rain_drops['position'])
    scat.set_linewidth(rain_drops['linewidth'])

def color_change_current_circles(frame_number):

    current_index = frame_number % n_drops


    #rain_drops['position'][current_index] = matrix[current_index]




    rain_drops['size'] = 3000
    rain_drops['color'] = (np.random.uniform(0,1),
    np.random.uniform(0,1), np.random.uniform(0,1), 1)
    rain_drops['growth'] = np.random.uniform(50, 200)
    #rain_drops['linewidth'] = 5

    # Update the scatter collection, with the new colors, sizes and positions.

    #if current_index%5 == 0:

    scat.set_edgecolors(rain_drops['color'])
    scat.set_sizes(rain_drops['size'])
    scat.set_offsets(rain_drops['position'])
    scat.set_linewidth(rain_drops['linewidth'])
    #else:
        #None

def grid(frame_number):

    rain_drops['size'] = 4000

    for i in range (40):
        rain_drops['position'][i] = matrix_vertical[i]



    scat.set_edgecolors(rain_drops['color'])
    scat.set_sizes(rain_drops['size'])
    scat.set_offsets(rain_drops['position'])
    scat.set_linewidth(rain_drops['linewidth'])

def wave(frame_number):
    current_index = frame_number % n_drops

    rain_drops['color'] = (0,1,0,1)
    rain_drops['linewidth'] = 10

    for k in range(40):
        rain_drops['position'][k] = matrix_horizontal[k]


    for i in range (5):
        for j in range(8):
            rain_drops['size'][j*i+i] = 10*j

    scat.set_edgecolors(rain_drops['color'])
    scat.set_sizes(rain_drops['size'])
    scat.set_offsets(rain_drops['position'])
    scat.set_linewidth(rain_drops['linewidth'])

#Just adding a comment to see if this works

#Adding another comment




# Construct the animation, using the update function as the animation director.
#frames: Amount of frames; repeat=False frames will not be repeated
animation = FuncAnimation(fig, animation_picker, interval=90,frames=number_frames,repeat=True)

figManager = plt.get_current_fig_manager()
figManager.full_screen_toggle()

plt.show()
