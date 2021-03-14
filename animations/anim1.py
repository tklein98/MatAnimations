import numpy as np
import time
import pandas as pd

starting_points = pd.read_csv('data/starting_points.csv')

def anim1(frame_number, rain_drops, n_drops, scat):
    rain_drops = rain_drops
    n_drops = n_drops
    scat = scat
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


# Animation two
def anim2(frame_number, rain_drops, n_drops, scat, arr):
    rain_drops = rain_drops
    n_drops = n_drops
    scat = scat
    current_index = frame_number % n_drops
    arr = arr
    input_word = 'Love'

    rain_drops['position'] = arr

    rain_drops['frame'][:, 0] = 0.5
    rain_drops['frame'][:, 1] = 0.0
    rain_drops['frame'][:, 2] = 0.0
    rain_drops['frame'][:, 3] = 1

    # rain_drops['fill'][:25+current_index, 0] = 0.0
    # rain_drops['fill'][:25+current_index, 1] = 0.8
    # rain_drops['fill'][:25+current_index, 2] = 0.0
    # rain_drops['fill'][:25+current_index, 3] = 1

    # rain_drops['fill'][160, 0] = 0.0
    # rain_drops['fill'][160, 1] = 0.8
    # rain_drops['fill'][160, 2] = 0.0
    # rain_drops['fill'][160, 3] = 1

    # Size of raindrops in grid
    rain_drops['size'][:] = 500

    # Retrieving the list of starting points (bottom left corner of input word)
    word_points = starting_points[f'{len(input_word)}']

    for i in range(len(input_word)):
        rain_drops['fill'][word_points[i], 0] = 0.0
        rain_drops['fill'][word_points[i], 1] = 0.8
        rain_drops['fill'][word_points[i], 2] = 0.0
        rain_drops['fill'][word_points[i], 3] = 1


    scat.set_edgecolors(rain_drops['frame'])
    scat.set_sizes(rain_drops['size'])
    scat.set_offsets(rain_drops['position'])
    scat.set_facecolors(rain_drops['fill'])

